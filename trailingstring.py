import sys

def main(pathname):
	for line in open(pathname, 'r').readlines():
		s = line.split(",")
		if s[1] in s[0]+"\n":
			print 1
		else:
			print 0

if __name__ == "__main__":
	for arg in sys.argv[1:]:
		main(arg)
