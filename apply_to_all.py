#!/usr/bin/python2
from file_util import scandir
import sys
import subprocess
from multiprocessing import Pool


def callMain(filename):
    return subprocess.call(['./main.py "'+filename+'"'], shell=True)


def main():
    p = Pool(10)
    path = '.'
    if len(sys.argv) > 1:
        path = sys.argv[1]
    baglist = scandir(path)
    p.map(callMain, baglist)
    print("Finished")


if __name__ == "__main__":
    main()
