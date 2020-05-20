from random import *

def genG(n):
	#initial setup / allocation
	adj = []
	for i in range(n):
		adj.append([])
		for j in range(n):
			adj[i].append(0)

	seed()
	
	# gen edges (not digraph)
	for i in range(n):
		for j in range(i+1, n):
			adj[i][j] = randint(0, 1)
			adj[j][i] = adj[i][j]

	final_string = 'N\nN\n' + str(n) + '\n'

	for i in range(n):
		s = 0
		l = []
		for j in range(n):
			s += adj[i][j]
			if(adj[i][j] == 1):
				l.append(j)
		final_string += str(s) + '\t // degree of vertex ' + str(i + 1) + '\n'
		for x in l:
			final_string += str(x + 1) + '\n'

	print(final_string)
		
genG(10)	
