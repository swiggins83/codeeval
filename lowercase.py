import sys
import string

def main(pathname):
	for line in open(pathname, 'r').readlines():
		print line.lower()

if __name__ == "__main__":
    for arg in sys.argv[1:]:
		lower(arg)
