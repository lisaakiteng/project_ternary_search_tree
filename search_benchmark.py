import random
import time
import matplotlib.pyplot as plt
from ternary_search_tree import TernarySearchTree

random.seed(42)

with open('data/search_trees/corncob_lowercase.txt') as file:
    words = [line.strip() for line in file]


sizes = [100, 500, 1_000, 5_000]

samples = [
    random.sample(words, k=size) for size in sizes
]

# for searching

nr_runs = 3
times = {}
search_sample = random.sample(words, k=20)
for sample in samples:
    tstree = TernarySearchTree()
    for word in sample:
        tstree.insert(word)
    times[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = time.time_ns()
        for word in search_sample:
            tstree.search(word)
        end_time = time.time_ns()
        times[len(sample)] += end_time - start_time
    times[len(sample)] /= nr_runs*1_000_000.0
times

print("Average searching times (ns) per dataset size:")
for size, avg_time in times.items():
    print(f"{size} words: {avg_time:.3f} ns")

# Plotting
plt.plot(times.keys(), times.values(), marker='o', markersize=2)
plt.xlabel('Number of Words in Ternary Search Tree')
plt.ylabel('Average Searching Time (ns)')
plt.title('Ternary Search Tree Searching Time Performance')
plt.grid(False)
plt.show()