import sys


def main():

    for arg in sys.argv[1:]:
        fizzbuzz(arg)


def fizzbuzz(pathname):
    """Replaces numbers in a string if it is divisible by params."""

    # open file
    f = open(pathname, 'r')

    # iterate through files lines
    for line in f.readlines():
        split = str(line).split(" ")
        for i in range(1,int(split[2])+1):

            if (i % int(split[0]) is 0) and (i % int(split[1]) is 0):
                sys.stdout.write('FB ')
            elif i % int(split[1]) is 0:
                sys.stdout.write('B ')
            elif i % int(split[0]) is 0:
                sys.stdout.write('F ')
            else:
                sys.stdout.write(str(i) + ' ')

        print


if __name__ == "__main__":
    main()
