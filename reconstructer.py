import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('archive', help='path to the WAM file ')
args = parser.parse_args()

with open(args.archive, 'rb') as f:
    file_path = ''
    for line in f:
        line_bin = False
        print(line)
        try:
            line.decode("utf-8")
            line_bin = False
        except:
            line_bin = True
            continue
        if not line_bin:
            if line.decode().startswith('!DIRECTORY'):
                try:
                    os.makedirs(line.decode().replace('!DIRECTORY|', '').replace('\n', ''))
                except:
                    pass
            if line.decode().startswith('!PATH'):
                with open(line.decode().replace('!PATH|', '').replace('\n', ''), 'wb') as file:
                    file.write(b'')
                    file_path = line.decode().replace('!PATH|', '').replace('\n', '')
            if line.decode().startswith('!FILE_PAYLOAD'):