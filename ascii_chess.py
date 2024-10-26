import pexpect
import subprocess
import string
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT
from time import sleep
from os import linesep
from helpers import index_for_move
#import chess
#import termcolor

# Configuration
allowIllegalMoves = False
command = "lc0"
engineThinkTime = 0.5

# Set up starting position
moves = []
board = [
         ("rook", "black"), ("knight", "black"), ("bishop", "black"), ("queen", "black"), ("king", "black"), ("bishop", "black"), ("knight", "black"), ("rook", "black"),
         ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"), ("pawn", "black"),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""), ("", ""),
         ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"), ("pawn", "white"),
         ("rook", "white"), ("knight", "white"), ("bishop", "white"), ("queen", "white"), ("king", "white"), ("bishop", "white"), ("knight", "white"), ("rook", "white"),
         ]

# Parse output from the engine
def parse_output(child):
    expected = child.after.decode()
    if "bestmove" in str(expected):
        expectedTruncated = str(str(expected).replace("bestmove ", ""))
        expectedTruncated = str(str(expectedTruncated).replace("ponder", ""))
        expectedTruncated = f"{expectedTruncated[0]}{expectedTruncated[1]}{expectedTruncated[2]}{expectedTruncated[3]}"
        print(f"Engine: {expectedTruncated}")
        moves.append(str(expectedTruncated))

# Send input to the engine
def send_input(input, child):
    child.sendline(input)

fileNums = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}

# def index_for_move(file_letter, rank):
#     file1 = fileNums.get(file_letter)
#     index = int(file1) + ((8 - (int(rank))) * 8) + 1
#     print(f"{file_letter}{rank}={index}")
#     return index

# Display a chessboard in the terminal
def updateBoard(moves, board):
    if moves != []:
        move = moves[-1]
        print(move)
        print(moves)
        print(board)
        print(f"{fileNums.get(move[0])}times{move[1]}")
        start_index = index_for_move(move[0], move[1])
        end_index = index_for_move(move[2], move[3])
        print(f"Debugbeforedebug{start_index} {end_index}")
        start_item = board[start_index - 2]
        end_item = board[end_index - 2]
        print(f"Debug{start_index} {end_index} {start_item} {end_item}")
        pieceindex = 1
        board2 = []
        for piece in board:
            pieceindex += 1
            if pieceindex == start_index:
                board2.append(("", ""))
            elif pieceindex == end_index:
                board2.append(start_item)
            else:
                board2.append(piece)

    if moves != []:
        return board2
    else:
        return board

def print_board(moves, board):
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

        ("", ""): "▢",
    }

    for entry in board:
        print(f"{piece_names.get(entry)} ", end="")
        if board_index % 8 == 0 and board_index != 0:
            print("\n", end="")
        board_index += 1

# Play Chess
child = pexpect.spawn(command)

child.expect(".+_", timeout=2)
parse_output(child)

child.expect(".+2024", timeout=2)
parse_output(child)
send_input("isready", child)

child.expect("readyok", timeout=2)
parse_output(child)
send_input("ucinewgame", child)

child.expect("Found pb network file.+", timeout=6)
parse_output(child)
child.expect("BLAS max batch size.+", timeout=6)
parse_output(child)
send_input(f"position startpos", child)
send_input("go", child)
print("Engine: Thinking...")
sleep(engineThinkTime)
send_input("stop", child)
child.expect("bestmove.+", timeout=1000)
parse_output(child)

while True:
    board3 = updateBoard(moves, board)
    board = board3
    print_board(moves, board)
    
    # Player move
    mymove = str(input("Enter your move: "))
    if mymove == "quit":
        print("Quitting")
        quit()
    moves.append(mymove)
    board3 = updateBoard(moves, board)
    board = board3
    print_board(moves, board)
    
    # Computer move
    send_input(f"position startpos moves {' '.join(moves)}", child)
    send_input("go", child)
    print("Engine: Thinking...")
    sleep(engineThinkTime)
    send_input("stop", child)
    child.expect("bestmove.+", timeout=1000)
    parse_output(child)
