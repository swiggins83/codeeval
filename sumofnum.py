import sys

def main(pathname):
	for line in open(pathname, 'r').readlines():
		summ = 0
		for i in range(0,len(line)-1):
			summ += int(line[i])
		print summ

if __name__ == "__main__":
    for arg in sys.argv[1:]:
		main(arg)
