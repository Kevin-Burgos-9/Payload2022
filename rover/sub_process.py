import subprocess

# Command to run (replace 144.39M with the correct frequency for your region)
command = "rtl_fm -f 144.9M -g 42 -s 22050 -l 20 - | multimon -t raw -a AFSK1200 /dev/stdin"

# Run the command and capture the output
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

# Open the output file and write the output
with open("output.txt", "w") as file:
    for line in process.stdout:
        #file.write(line)
        print(line, end="")

# Wait for the process to finish
process.wait()
