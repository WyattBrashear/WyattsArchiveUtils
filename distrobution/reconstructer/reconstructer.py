import os
import argparse
import time

archive = input("Enter the path to the archive file: ")
benchmark_mode = input("Do you want to benchmark the script? (y/n): ")

start = 0
if benchmark_mode.lower() == 'y':
    start = time.time()
try:
    with open(archive, 'rb') as f:
        reading_filemap = False
        reading_dirmap = False
        reading_payload = False
        path = ""
        filepaths = []
        final_path = False
        filemap_selection = 0
        for line in f:
            if line == b'!DIRMAP\n':
                reading_dirmap = True
                f.readline()
            if line == b'!FILEMAP\n':
                reading_dirmap = False
                reading_filemap = True
                f.readline()
            if line == b'!PAYLOAD\n':
                reading_dirmap = False
                reading_filemap = False
                reading_payload = True
                f.readline()
            if reading_payload:
                if line.startswith(b'!FILE|'):
                    path = line.decode().split('|')[1].replace('\n', '')
                    f.readline()
                    if not final_path:
                        filemap_selection += 1
                    else:
                        pass

            if reading_dirmap:
                try:
                    if not line.decode().startswith("!DIRMAP"):
                        os.makedirs(line.decode().replace('\n', ''))
                except:
                    pass
            if reading_filemap and not line.decode().startswith("!FILEMAP"):
                with open(line.decode().replace('\n', ''), 'w') as file_creation:
                    file_creation.write("")
            try:
                if not path.startswith('!FILE|'):
                    with open(path, 'ab') as file_writer:
                        if not line.startswith(b'!FILE|'):
                            file_writer.write(line)
            except:
                pass
except:
    print("An error occurred while processing the archive file.")
    exit(0)
if benchmark_mode.lower() == 'y':
    print(f"Script successfully reconstructed data from {archive} in {time.time() - start:.2f}")