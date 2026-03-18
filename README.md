# Wyatt's Archive format for Multipurpose Use
this is a project i made (Mostly out of boredom) to make my own archive format. It is pretty much just a Tarball but
under a different name. 


## Installation
~~~bash
pip install wyattsarchiveutils
~~~
Usage can be seen below.

# Benchmarks
I know this is what most of you are here for. These tests were done on a 2024 M3 Macbook Air with 16 GB of RAM and 512 GB of Storage (312/494 GB Used). In order to run these tests yourself, Use the -b option when running the scrips
## Linux Codebase (As of 2/28/2026 @ 11:19 PM) (Clone depth = 1) (1.87 GB)
https://github.com/torvalds/linux.git
Seeing as the linux codebase changes about once every 30 minutes i cant just say "Linux Codebase". So here is the
performance of the program to create an archive for it and reconstruct it.

Writing: 15.44 Seconds
Reconstruction: 1200.21 seconds
## Usage
Writer:
~~~bash
wau-writer {option}
~~~
Options:
Directory
Output
-b (Benchmark)
Reconstructor:
~~~bash
wau-reconstructer {option}
~~~
Options:
Archive
-b (Benchmark)

## AI Usage
This project was assisted in creation by the Pycharm Autocomplete plugin. Along with a small amount of help from Claude (Raycast) when i got stuck.
The majority of this project was human written. 

## Demo Vid
https://drive.google.com/file/d/1gcUvsz7iuU142PqjKQzFl-n92xnfXSvA/view?usp=sharing