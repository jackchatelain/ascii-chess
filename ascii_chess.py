import pexpect
import subprocess
import string
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT
from time import sleep
from os import linesep
import chess

command = "lc0"
moves = []
log = ["started"]

def logthis(logtext):
    log.append(str(logtext))
    #print(f"LOG:{logtext}")

def parse_output(child):
    expected = child.after.decode()
    logthis(f"Full output: {child.before.decode()}SEP{expected} end full command")
    if "bestmove" in str(expected):
        logthis("Output contains bestmove")
        expectedTruncated = str(expected).replace("bestmove ", "")
        logthis(f"Removed phrase bestmove:{expectedTruncated}")
        expectedTruncated = expectedTruncated.replace("ponder", "")
        logthis(f"Removed phrase ponder:{expectedTruncated}")
        expectedTruncated = f'{expectedTruncated[0]}{expectedTruncated[1]}{expectedTruncated[2]}{expectedTruncated[3]}'
        logthis(f"Removed all except first 4 chars:{expectedTruncated}")
        print(f"Engine: {expectedTruncated}")
        moves.append(str(expectedTruncated))
    else:
        logthis("Output doesn't contain bestmove")
    #return expected

def send_input(input, child):
    #print(f">>{input}>inputend")
    child.sendline(input)
    logthis(f"Sent line: {input}")

def main():
    child = pexpect.spawn(command)
    logthis(f"PExpect spawned: {command}")

    child.expect('.+_', timeout=5)
    logthis("Expecting: .+_")
    parse_output(child)

    child.expect('.+2023', timeout=5)
    logthis("Expecting: .+2023")
    parse_output(child)
    send_input('isready', child)

    child.expect('readyok', timeout=5)
    logthis("Expecting: readyok")
    parse_output(child)
    send_input('ucinewgame', child)

    child.expect('Found pb network file.+', timeout=10)
    logthis("Expecting: Found pb network file.+")
    parse_output(child)
    child.expect('Initialized.+', timeout=10)
    logthis("Expecting: Initialized.+")
    parse_output(child)
    send_input('position startpos', child)
    send_input('go wtime 10000 btime 10000', child)
    child.expect('bestmove.+', timeout=1000)
    logthis("Expecting: bestmove.+")
    parse_output(child)

    while True:
        logthis("Player prompt shown")
        mymove = str(input("Enter your move: "))
        if mymove == "quit":
            logthis("Player quitted")
            quit()
        logthis(f"Player entered: {mymove}")
        moves.append(mymove)
        logthis("Appended entry to moves")
        logthis("Sending position to lc0")
        send_input(f'position startpos moves {" ".join(moves)}', child)
        logthis("Sending go to lc0")
        send_input('go', child)
        logthis("lc0 thinking")
        print("Engine: Thinking...")
        sleep(0.5)
        send_input('stop', child)
        logthis("Expecting timeout=11: bestmove.+")
        child.expect('bestmove.+', timeout=1000)
        logthis("lc0 outputted bestmove")
        parse_output(child)
        logthis("parsed bestmove")

main()
