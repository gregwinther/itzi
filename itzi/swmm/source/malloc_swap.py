from glob import glob

files = glob("./*.c")
for filepath in files:
    # Read in the file
    with open(filepath, "r") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace("<malloc.h>", "<stdlib.h>")

    # Write the file out again
    with open(filepath, "w") as file:
        file.write(filedata)