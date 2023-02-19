#!/usr/bin/python3

def main():
    import sys
    summation = 0
    for i in range(1, len(sys.argv)):
        summation = summation + int(sys.argv[i])
    print(summation)


if __name__ == "__main__":
    main()
