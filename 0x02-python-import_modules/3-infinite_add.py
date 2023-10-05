#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    argnum = 0
    for num in argv[1:]:
        argnum = argnum + int(num)
    print(argnum)
