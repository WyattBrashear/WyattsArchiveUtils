import os
import argparse
import time

input_dir = input("Enter the directory to be transformed into a WAM file: ")
output = input("Enter the output WAM file name: ")
benchmark_mode = input("Do you want to benchmark the script? (y/n): ")

start = 0
if benchmark_mode.lower() == 'y':
    start = time.time()
dirs_tobe = []
files_dirs = []
try:
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            dirs_tobe.append(os.path.join(root, file))
            files_dirs.append(root)
    with open(f"{output}.wam", 'w') as f:
        f.write("")
    with open(f"{output}.wam", 'ab') as f:
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
    if benchmark_mode.lower() == 'y':
        print(f"Writer successfully wrote {output}.wam in {time.time() - start:.2f}")
except:
    print("An error occured while attempting to write the WAM file")
