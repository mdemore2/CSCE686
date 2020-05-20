import random
import numpy as np

random.seed()
numVerts = 20
density = 1  # likelihood a node is connected to each other

adjmaj = np.zeros((numVerts, numVerts), dtype=int)
for i in range(numVerts):
    for j in range(i):  # allows looping with i + 1
        adjmaj[i, j] = 0 if random.random() > density else 1

adjmaj = adjmaj + adjmaj.T  # makes symmetric

print(adjmaj)
print(f'Expected edges: {numVerts*(numVerts-1)*density}\nTotal edges: {sum(sum(adjmaj))}\n')
with open('pygraph.txt', 'w') as f:
    f.write('N  //directed\n')
    f.write('N  //weighted\n')
    f.write(f'{numVerts} //number of vertices\n')
    for i in range(numVerts):
        degree = sum(adjmaj[i])
        f.write(f'{degree}  //(out) degree of vertex {i+1}\n')
        for j in range(numVerts):
            if adjmaj[i, j] == 1:
                f.write(f'{j+1}\n')
