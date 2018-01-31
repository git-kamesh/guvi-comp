import subprocess

# Author : Kamesh S <1234.kamesh@gmail.com>
# Notes : Use python version 3.5 or above

def run_command(command,ip=''):
    p = subprocess.Popen(command.split(),stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,stdin=subprocess.PIPE)
    grep_stdout = p.communicate(input=ip.encode())[0]
    p.wait(5) # wait maximum 5 seconds to tackle infinite loop
    return grep_stdout.decode()

def compile():
    return run_command("gcc cprog.c -o guvic")

def test(case_):
    try:
        op = run_command("./guvic",case_[0])
        if op.encode() == case_[1].encode():
            return True
        return False
    except:
        print("Execution limit reached")
        return False

if "error" in compile():
    print("Error in the code")
else:
    data = [
        "5\n3\n", # Input
        "Enter two numbers:\n\nSum : 8\n" # Expected output
        ]
    print(test(data))

# Just provided sample , can be made to check multiple testcases
