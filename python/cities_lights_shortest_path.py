import os
from collections import deque

def shortest_time(n, graph, t, c):
	q=deque()
	i=0
	q.append(1)
	visited=[1]
	while q:
		print(q)
		for x in range(len(q)):
			current=q.popleft()
			print (current)
			if current==n:
				return ((c*i)+(i-1))
			#visited.append(current)
			for nbr in graph[current]:
				if nbr not in visited:
					q.append(nbr)
					visited.append(nbr)
		i+=1

print (shortest_time(6, {1:[2,3,4], 2:[4,5], 3:[1], 4:[1,2], 5:[2,], 6:[5]}, 3, 5))