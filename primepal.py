import sys
import math

def main():
    for i in range(1,1000):
        if str(1000-i)[0] is str(1000-i)[2] and isprime(1000-i):
            print 1000-i
            break

def isprime(n):
    for i in range(2,n):
        if n % i is 0:
            return False
    return True
        

if __name__ == "__main__":
    main()
