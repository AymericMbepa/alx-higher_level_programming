#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if len(sys.argv) == 2:
            print("{:d} argument:".format(len(sys.argv) - 1))
            print("{:d}: {:s}".format(len(sys.argv) - 1, sys.argv[1]))
        else:
            print("{:d} arguments:".format(len(sys.argv)))
            for i in range(1, len(sys.argv)):
                print("{:d}: {:s}".format(i, sys.argv[i]))
    else:
        print("{:d} arguments.".format(0))
