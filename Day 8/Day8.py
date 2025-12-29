# PART 1

from math import sqrt
import heapq
from collections import Counter

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

with open('input.txt', 'r', encoding='utf-8') as f:
    matrix = [[int(num) for num in line.rstrip('\n').split(',')] for line in f]

heap = []
for i in range(len(matrix) - 1):
    for j in range(i+1, len(matrix)):
        coord1, coord2 = matrix[i], matrix[j]
        heapq.heappush(heap, (distance(coord1, coord2), i, j))

circuits = []

counter = Counter()
count = 0
while count < 1000:
    dist, i, j = heapq.heappop(heap)
    counter[i] += 1
    counter[j] += 1
    added = False
    new_circuits = []
    new_circuit = set()
    temp_circuits = circuits.copy()
    for circuit in circuits:
        if i in circuit or j in circuit:
            temp_circuits.remove(circuit)
            circuit.add(i)
            circuit.add(j)
            added = True
            if len(new_circuit) == 0:
                new_circuit = circuit
            else:
                new_circuit = new_circuit | circuit
    if not added:
        new_circuit = {i, j}
    new_circuits.append(new_circuit)
    temp_circuits += new_circuits
    circuits = temp_circuits
    count += 1

circuits.sort(key=lambda x: len(x), reverse=True)

print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))


