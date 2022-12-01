#!/usr/bin/python3
if __name__ == "__main__":
    if len(argv) > 1:
        if len(argv) == 2:
            print("{:d} argument:".format(len(argv) - 1))
            print("{:d}: {:s}".format(len(argv) - 1, argv[1]))
        else:
            print("{:d} arguments:".format(len(argv)))
            for i in range(1, len(argv)):
                print("{:d}: {:s}".format(i, argv[i]))
    print("{:d} arguments.".format(0))
