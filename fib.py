import sys

def init(pathname):
    """Find answer to fibonacci sequence of number n read in from a file."""

    for line in open(pathname, 'r').readlines():
        print fib(int(line.split("\n")[0]))

def fib(n):
    """Make fibonacci sequence."""

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        init(arg)
