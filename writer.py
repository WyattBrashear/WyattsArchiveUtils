import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('directory', help="directory to be transformed into an archive")
parser.add_argument('output', help="output archive name")
args = parser.parse_args()

dirs_tobe = []
files_dirs = []

for root, dirs, files in os.walk(args.directory):
    for file in files:
        dirs_tobe.append(os.path.join(root, file))
        files_dirs.append(root)
with open(f"{args.output}.wam", 'w') as f:
    f.write("")
with open(f"{args.output}.wam", 'ab') as f:
    for i in range(len(dirs_tobe)):
        f.write(f"!DIRECTORY|{files_dirs[i]}\n".encode("utf-8"))
        f.write(f"!PATH|{dirs_tobe[i]}\n".encode("utf-8"))
        f.write(f'!FILE_PAYLOAD|'.encode("utf-8"))
        print(dirs_tobe[i])
        with open(dirs_tobe[i], 'rb') as file:
            file_text = file.read()
            f.write(f'{sum(1 for line in file)}\n"""\n'.encode("utf-8"))
            print(sum(1 for line in file))
            print(file_text)
            f.write(file_text)
        f.write('\n"""\n!EOF\n---\n'.encode("utf-8"))