import sys

def main():
    summ = []
    j=2
    while(len(summ) != 1000):
        if isprime(j):
            summ.append(j)
        j+=1
    print sum(summ)

def isprime(n):
    for i in range(2,n):
        if n % i is 0:
            return False
    return True


if __name__ == "__main__":
    main()
