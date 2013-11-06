import sys

def main():
    for arg in sys.argv[1:]:
        lowbigmult(arg)


def lowbigmult(pathname):

    f = open(str(pathname),'r')

    for line in f.readlines():
        x = int(line.split(",")[0])
        n = int(line.split(",")[1])

        i = 0
        while(n*i < x):
            i+=1
        print n*i

if __name__ == "__main__":
    main()
