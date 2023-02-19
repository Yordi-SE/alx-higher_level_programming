#!/usr/bin/python3

def main():
    import sys
    if len(sys.argv) == 2:
        print("{} argument:".format(1))
        print("1: {}".format(sys.argv[1]))
    elif len(sys.argv) == 1:
        print("{} arguments.".format(0))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
