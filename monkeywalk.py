import sys

def calculatePoints():
    counter=0
    for i in range(0,100):
        x,y=0,0
        for j in range(0,100):
            for s in range(0,len(str(i))):
                if str(i)[s] is not '-':
                    x+=int(str(i)[s])
                if str(j)[s] is not '-':
                    y+=int(str(j)[s])
                if x+y<20:
                    print 'x: '+str(i)
                    print 'y: '+str(j)


if __name__ == "__main__":
    calculatePoints()
