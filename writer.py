import os
import argparse
import time

parser = argparse.ArgumentParser()

parser.add_argument('directory', help="directory to be transformed into an archive")
parser.add_argument('output', help="output archive name")
parser.add_argument('-b', '--benchmark', action='store_true', help="Start a timer for running a benchmark on the writer")
args = parser.parse_args()
start = 0
if args.benchmark:
    start = time.time()
dirs_tobe = []
files_dirs = []

for root, dirs, files in os.walk(args.directory):
    for file in files:
        dirs_tobe.append(os.path.join(root, file))
        files_dirs.append(root)
with open(f"{args.output}.wam", 'w') as f:
    f.write("")
with open(f"{args.output}.wam", 'ab') as f:
    f.write("!DIRMAP".encode())
    is_dir = False
    for path in files_dirs:
        f.write(f"\n{path}".encode())
    f.write("\n!FILEMAP".encode())
    for path in dirs_tobe:
        f.write(f"\n{path}".encode())
    f.write("\n!PAYLOAD".encode())
    for path in dirs_tobe:
        with open(path, 'rb') as f2:
            file_contents = f2.read()
        f.write(f"\n!FILE|{path}\n!_!\n".encode())
        f.write(file_contents)
if args.benchmark:
    print(f"Writer successfully wrote {args.output}.wam in {time.time() - start:.2f}")