import sys

def main():
    for arg in sys.argv[1:]:
        f = open(arg,'r')
        
        for line in f.readlines():
            summ = 0
            for i in range(0,len(line)-1):
                summ += int(line[i])
            print summ

if __name__ == "__main__":
    main()
