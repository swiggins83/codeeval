import sys
import math

x = 0
y = 0

def main():
    spiralp(sys.argv[1:])


def spiralp(pathname):
    """Returns a matrix of numbers printed in a spiral pattern. Read in from a file."""

    for line in open(pathname,'r').readlines():
        matrix = []
        i=0
        params = line.split(";")
        x = int(params[0])
        y = int(params[1])
        while i < len(params[2].split(" ")):
            oldi = i
            i += x
            matrix.append(params[2].split(" ")[oldi:i])

        matrix[x-1][y-1] = matrix[x-1][y-1].split("\n")[0]


        for i in range(0,x*y):
            



        j=2
        for i in range(0,x*y):
            if i in range(0,x):
                sys.stdout.write(matrix[0][i] + " ")
            elif i in range(x+1,x+y):
                sys.stdout.write(matrix[i-x][y-1] + " ")
            elif i in range(x+y+1,x+y+x):
                sys.stdout.write(matrix[x-1][y-j] + " ")
                j+=1
            #elif i in range(x+y+x,x+y+x+y-2):
                #sys.stdout.write(matrix[
        print
        


    
if __name__ == "__main__":
    main()
