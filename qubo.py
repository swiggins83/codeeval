import sys

def main():
    quBoard(sys.argv[1:])

def quBoard(pathname):

    matrix = [[0 for x in range(0,32)] for y in range(0,32)]

    for line in open(pathname).readlines():
        line = line.split(" ")
        if line[0] is 'SetCol':
            print
            if line[1] > -1 and line[1] < 256 and line[2] > -1 and line[2] < 32:
                for x in range(0,32):
                    matrix[x][line[1]] = line[2]
        elif line[0] is 'SetRow':
            if line[1] > -1 and line[1] < 256 and line[2] > -1 and line[2] < 32:
                for x in range(0,32):
                    matrix[line[1]][x] = line[2]
        elif line[0] is 'QueryCol':
            print sum(matrix[x][line[1]])
        elif line[0] is 'QueryRow':
            print sum(matrix[line[1]][x])


if __name__ == "__main__":
    main()
