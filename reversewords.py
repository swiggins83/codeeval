import sys

def main():
    for arg in sys.argv[1:]:
        reversewords(arg)


def reversewords(pathname):
    """Reverse two words separated by a whitespace."""

    f = open(pathname,'r')

    for line in f.readlines():
        if len(line) > 0:                
            split = str(line).split(" ")
            for i in range(0,len(split)):
                if "\n" in split[len(split)-1-i]:
                    sys.stdout.write(split[len(split)-1-i].split("\n")[0] + ' ')
                else:
                    sys.stdout.write(split[len(split)-1-i] + ' ')

            print

if __name__ == "__main__":
    main()
