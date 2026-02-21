import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('directory', help="directory to be transformed into an archive")
parser.add_argument('output', help="output archive name")
args = parser.parse_args()

dirs_tobe = []

for root, dirs, files in os.walk(args.directory):
    for file in files:
        dirs_tobe.append(os.path.join(root, file))
print(dirs_tobe)

with open(args.output, 'ab') as f:
    for directory in dirs_tobe:
        f.write(f"!PATH|'{directory}'\n".encode("utf-8"))
        with open(directory, 'rb') as file:
            f.write(file.read())
        f.write("\n!EOF\n".encode("utf-8"))