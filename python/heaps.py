'''
library to perform heap operations.
'''

import os
import sys

class heap:
	
	def __init__(self):
		pass

	def min_heapify(i,list_heap):
		
		i=len(l)-1
		while (i>0):
			parent=int((i-1)/2)
			print("i="+str(i)+" parent="+str(parent))
			if list_heap[parent]>list_heap[i]:
				
				list_heap[parent],list_heap[i]=list_heap[i],list_heap[parent]
				
				i=parent
			else:
				break
		return

	def build_min_heap(list_of_elements):
		for x in range(len(list_of_elements)-1,0,-1):
			heap.min_heapify(x,list_of_elements)
		return

if __name__=='__main__':
	l=[22,33,44,55,66,88,99]
	l.append(1)
	heap.min_heapify(len(l)-1,l)
	print (l)
			