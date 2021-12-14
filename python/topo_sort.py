import collections

"""
topological sort.

input: 
output: 

"""

def is_cyclic(node,graph,visited,rec_stack):

	visited[node]=True
	rec_stack.append(node)
	for n in graph[node]:
		if visited[n]==False:
			if is_cyclic(n,graph,visited,rec_stack)==True:
				return True
		elif visited[n]==True:
			if n in rec_stack:
				return True
	rec_stack.pop()
	return False

if __name__=='__main__':
	n=6
	cycle = False
	rec_stack=[]
	op_stack = []
	visited = collections.defaultdict(bool)
	edges = [[5,2], [5,0], [4,0], [4,1], [2,3], [3,1],[4,3]]
	graph = collections.defaultdict(list)
	for edge in edges:
		graph[edge[0]].append(edge[1])
	print (graph)
	cycle=False
	for node in range(6):
		if visited[node]==False:
			if is_cyclic(node,graph,visited,rec_stack):
				cycle=True
				break
	print (cycle)
	




