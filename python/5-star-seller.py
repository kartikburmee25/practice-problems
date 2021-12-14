"""
5 star sellers question

input:
list of 5-start/reviews per product
threshold

output:
min no. of 5 star ratings required

steps:

1. calculate the improvement if we add one 5star review for each product.
2. push it to heap (improvement,p0,p1)
3. while you don't reach threshhold:
		pop element
		modify element and push back in heap

"""
from heapq import heappush, heappop

def num_ratings(products, threshold):

	heap = []
	k=0
	for p in products:

		ratio = p[0]/p[1]
		k+=ratio
		improvement = (p[0]+1)/(p[1]+1) - ratio
		heappush (heap, (-improvement,p[0],p[1]))

	k = k/len(products)
	result = 0
	while k<threshold/100.0:

		_,p0,p1 = heappop(heap)

		improv = (p0+1)/(p1+1) - p0/p1
		k+=improv/len(products)
		p0+=1
		p1+=1
		improv = (p0+1)/(p1+1)-p0/p1
		heappush(heap, (-improv, p0,p1))
		result+=1
	return result

if __name__ == '__main__':

	products = [[4,4], [1,2], [3,6]]
	threshold = 77

	print (num_ratings(products,threshold))











