import subprocess


# os.system("lc0")

# subprocess.run([""])

# command = 'whoami'
command = 'lc0'

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, error = process.communicate("isready\n")

while True:
    stream = process.stderr
    output = stream.readline().decode('utf-8')
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())

rc = process.poll()
if rc == 0:
    print("Command succeeded.")
else:
    error = process.stderr.read().decode()
    print(f"Command failed ({rc}): {error}")
