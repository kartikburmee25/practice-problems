import time
import os


def fib(n):
  if n==0 or n==1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
  #n = int(input('which fib no. do you wish to calculate'))
  print (fib(40))
