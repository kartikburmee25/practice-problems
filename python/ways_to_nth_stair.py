import time
import os
import sys

def ways(n):
	if n<0:
		return 0
	if n==0:
		return 1
	w = ways(n-1) + ways(n-2) + ways(n-3)
	return w

if __name__=='__main__':
	n = sys.argv[1]
	print (str(ways(int(n))))