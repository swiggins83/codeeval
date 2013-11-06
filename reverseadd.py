import sys

def init(pathname):
    for n in open(pathname,'r').readlines():
		n = n.split("\n")[0]
		i = 0
		while n[len(n)/2::] != n[::len(n)/2]:
			n = int(n) + int(n[::-1])
			print n


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        init(arg)
