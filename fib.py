import sys

def main():
    for arg in sys.argv[1:]:
        init(arg)

def init(pathname):
    """Find answer to fibonacci sequence of number n read in from a file."""

    f = open(pathname,'r')

    for line in f.readlines():
        n = int(line.split("\n")[0])
        print fib(n)

def fib(n):
    """Make fibonacci sequence."""

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    main()
