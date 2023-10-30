import subprocess
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

from os import linesep
import pexpect

command = 'lc0'

def parse_output(child):
    expected = child.after.decode()
    # Print full command
    print(f"<<{child.before.decode()}{expected}")
    return expected

def send_input(input, child):
    print(f">>{input}")
    child.sendline(input)

def main():
    child = pexpect.spawn(command)

    child.expect('.+_', timeout=10)
    parse_output(child)

    child.expect('.+2023', timeout=10)
    parse_output(child)
    send_input('isready', child)

    child.expect('readyok', timeout=10)
    parse_output(child)
    send_input('ucinewgame', child)

    child.expect('Found pb network file.+', timeout=10)
    parse_output(child)
    send_input('quit', child)

main()
