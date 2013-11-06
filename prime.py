import sys


def main():
    primes(sys.argv[1:])

def primes(pathname):

    dontuse = []
    for line in open(pathname,'r').readlines():
        n = int(line.split("\n")[0])

        for i in range(1,n):
            if i in dontuse:
                print 'dont'
            else:
                if isprime(i,dontuse):
                    print i


def isprime(n,dontuse):
    if n is 2:
        return True
    else:
        for j in range(3,n):
            if n % j is 0:
                dontuse.append(j)
                return False
        return True


if __name__ == "__main__":
    main()
