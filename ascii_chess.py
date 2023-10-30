import subprocess
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

from os import linesep
import pexpect

command = 'lc0'

def parse_output(before, after):
    expected = after.decode()
    output = before.decode() + expected
    # Print full command
    print(f"<<{output}")

    if expected.endswith("2023"):
        return "isready"

def main():
    child = pexpect.spawn(command)

    child.expect('.+_', timeout=10)
    parse_output(child.before, child.after)

    child.expect('.+2023', timeout=10)
    input = parse_output(child.before, child.after)
    if input is not None:
        child.sendline(input)

    child.expect('readyok', timeout=10)
    parse_output(child.before, child.after)

main()
