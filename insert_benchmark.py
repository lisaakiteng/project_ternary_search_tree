import random
import time
import matplotlib.pyplot as plt
from ternary_search_tree import TernarySearchTree

with open('data/search_trees/corncob_lowercase.txt') as file:
    words = [line.strip() for line in file]

random.seed(42)
sizes = [100, 500, 1_000, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000]

samples = [
    random.sample(words, k=size) for size in sizes
]

# checking for insertion 

nr_runs = 10
times = {}
insert_sample = random.sample(words, k=20)
for sample in samples:
    tstree = TernarySearchTree()
    for word in sample:
        tstree.insert(word)
    times[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = time.time_ns() 
        for word in insert_sample:
            tstree.insert(word)
        end_time = time.time_ns()
        times[len(sample)] += end_time - start_time
    times[len(sample)] /= nr_runs*1_000_000.0
times


print("Average insertion times (ns) per dataset size:")
for size, avg_time in times.items():
    print(f"{size} words: {avg_time:.3f} ns")

# Plotting
plt.plot(times.keys(), times.values(), marker='o', markersize=2)
plt.xlabel('Number of Words in Ternary Search Tree')
plt.ylabel('Average Insertion Time (ms)')
plt.title('Ternary Search Tree Insertion Time Performance')
plt.grid(False)
plt.show()