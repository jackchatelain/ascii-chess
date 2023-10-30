import subprocess
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

from os import linesep
import pexpect

# command = 'whoami'
command = 'lc0'

# def parse_output(output):
#     print(f"<<{output}")
#     if output.endswith("2023"):
#         return "isready"

# def send_input(input, stdin):
#     print(f">>{input}")
#     stdin.write(b"{input}\n")
#     stdin.flush()

# def main():
#     process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)

#     output_stream = process.stderr
#     error_stream = process.stdout

#     while True:
#         output = output_stream.readline().decode('utf-8')
#         if output == '' and process.poll() is not None:
#             break
#         if output:
#             input = parse_output(output.strip())
#             if input is not None:
#                 send_input(input, process.stdin)

#     rc = process.poll()
#     if rc == 0:
#         print("Command succeeded.")
#     else:
#         error = error_stream.read().decode()
#         print(f"Command failed ({rc}): {error}")

# main()


child = pexpect.spawn(command)
child.expect('.*Jul 22 2023', timeout=300)
print(child.before.decode() + child.after.decode())
child.sendline('isready')
child.expect('.*readyok', timeout=300)
print(child.before.decode() + child.after.decode())   # Print the result of the command.
