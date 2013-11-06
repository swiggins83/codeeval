import sys

def fizzbuzz(pathname):
    """Replaces numbers in a string if it is divisible by params."""

    for line in open(pathname, 'r').readlines():
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
    for arg in sys.argv[1:]:
        fizzbuzz(arg)
