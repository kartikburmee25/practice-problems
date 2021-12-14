import time
import os

def fib(n, arr):
  if len(arr)>n:
    return arr[n-1]
  if n==0 or n==1:
    arr.append(1)
    return arr[n-1]
  else:
    k=fib(n-1,arr) + fib(n-2,arr)
    arr.append(k)
    return k

if __name__ == '__main__':
  arr=[]
  print (fib(40,arr))


