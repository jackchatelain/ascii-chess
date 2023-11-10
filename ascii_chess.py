import pexpect
import subprocess
import string
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT
from time import sleep
from os import linesep
#import chess
#import termcolor

command = "lc0"
moves = []
log = ["started"]
board = [("rook", "white"), ("knight", "white"), ("bishop", "white"), ("queen", "white"), ("king", "white"), ("bishop", "white"), ("knight", "white"), ("rook", "white"),
         ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("rook", "black"), ("knight", "black"), ("bishop", "black"), ("queen", "black"), ("king", "black"), ("bishop", "black"), ("knight", "black"), ("rook", "black"),
         ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black")
         ]


def parse_output(child):
    expected = child.after.decode()
    if "bestmove" in str(expected):
        expectedTruncated = str(str(expected).replace("bestmove ", ""))
        expectedTruncated = str(str(expectedTruncated).replace("ponder", ""))
        expectedTruncated = f"{expectedTruncated[0]}{expectedTruncated[1]}{expectedTruncated[2]}{expectedTruncated[3]}"
        print(f"Engine: {expectedTruncated}")
        moves.append(str(expectedTruncated))

def send_input(input, child):
    child.sendline(input)

def printboard(moves):
    board_index = 1
    piece_names = {
        ("king", "white"): "♔",
        ("queen", "white"): "♕",
        ("rook", "white"): "♖",
        ("bishop", "white"): "♗",
        ("knight", "white"): "♘",
        ("pawn", "white"): "♙",

        ("king", "black"): "♚",
        ("queen", "black"): "♛",
        ("rook", "black"): "♜",
        ("bishop", "black"): "♝",
        ("knight", "black"): "♞",
        ("pawn", "black"): "♟︎",

        ("", ""): "▢"
    }
    for entry in board:
        print(f"{piece_names.get(entry)} ", end="")
        if board_index % 8 == 0 and board_index != 0:
            print("\n", end="")
        board_index += 1
    #output = colored(letter, colorNone)

def main():
    child = pexpect.spawn(command)

    child.expect(".+_", timeout=2)
    parse_output(child)

    child.expect(".+2023", timeout=2)
    parse_output(child)
    send_input("isready", child)

    child.expect("readyok", timeout=2)
    parse_output(child)
    send_input("ucinewgame", child)

    child.expect("Found pb network file.+", timeout=6)
    parse_output(child)
    child.expect("Initialized.+", timeout=6)
    parse_output(child)
    send_input(f"position startpos", child)
    send_input("go", child)
    print("Engine: Thinking...")
    sleep(0.5)
    send_input("stop", child)
    child.expect("bestmove.+", timeout=1000)
    parse_output(child)

    while True:
        printboard(moves)
        mymove = str(input("Enter your move: "))
        if mymove == "quit":
            print("Quitting")
            quit()
        moves.append(mymove)
        send_input(f"position startpos moves {' '.join(moves)}", child)
        send_input("go", child)
        print("Engine: Thinking...")
        sleep(0.5)
        send_input("stop", child)
        child.expect("bestmove.+", timeout=1000)
        parse_output(child)

main()
