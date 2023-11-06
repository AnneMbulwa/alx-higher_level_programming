#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1

    if num_args == 0:
        print("{} arguments".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
    else:
        print("{} arguments:".format(num_args))
    for num in range(num_args):
        print("{}: {}".format(num + 1, argv[num + 1]))
