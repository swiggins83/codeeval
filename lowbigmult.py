import sys

def lowbigmult(pathname):

    for line in open(pathname, 'r').readlines():
        x = int(line.split(",")[0])
        n = int(line.split(",")[1])

        i = 0
        while(n*i < x):
            i+=1
        print n*i

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        lowbigmult(arg)
