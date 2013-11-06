import sys

def mth(arg):
	for line in open(arg, 'r').readlines():
		s = line.split(' ')
		m = -1*int(s[-1])-1
		if m > -1*(len(s)+1):
			print s[m]

if __name__ == '__main__':
	for arg in sys.argv[1:]:
		mth(arg)
