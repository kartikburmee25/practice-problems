'''
merge sort
'''


def merge(arr1, arr2):
	print (arr1,arr2)
	arr=[]
	l1=len(arr1)
	l2=len(arr2)
	i,j=0,0
	while(i<l1 and j<l2):
		#print('i',i,'j',j)
		if arr1[i]<=arr2[j]:
			arr.append(arr1[i])
			i+=1
		else:
			arr.append(arr2[j])
			j+=1
	if i<l1:
		for k in range(i,l1):
			arr.append(arr1[k])
	else:
		for k in range(j,l2):
			arr.append(arr2[k])
	#print(arr)
	return arr

def merge_sort(arr):

	if len(arr)==1:
		return arr

	mid=len(arr)//2
	print(mid)
	#print (mid)
	x=merge_sort(arr[:mid])
	y=merge_sort(arr[mid:])
	result=merge(x,y)

	return result

if __name__ == '__main__':
	l=[7,7,7,6,5,4,3,2,1]
	print (merge_sort(l))