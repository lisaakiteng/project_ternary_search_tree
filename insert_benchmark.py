import random
import time
import matplotlib.pyplot as plt
from ternary_search_tree import TernarySearchTree

random.seed(42)

with open('data/search_trees/corncob_lowercase.txt') as file:
    words = [line.strip() for line in file]

sizes = [100, 500, 1_000, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000]
samples = [random.sample(words, k=size) for size in sizes]

nr_runs_list = [30]
k_insert_list = [20]

all_results = {}

for nr_runs in nr_runs_list:
    for k_insert in k_insert_list:
        print(f"\nBenchmark for nr_runs={nr_runs}, k_insert={k_insert}")
        times = {}
        insert_sample = random.sample(words, k=k_insert)
        for sample in samples:
            tstree = TernarySearchTree()
            for word in sample:
                tstree.insert(word)

            size = len(sample)
            total_time_ns = 0
            for _ in range(nr_runs):
                start_time = time.time_ns()
                for word in insert_sample:
                    tstree.insert(word)
                end_time = time.time_ns()
                total_time_ns += end_time - start_time

            avg_time_ms = total_time_ns / (nr_runs * 1_000_000.0)
            times[size] = avg_time_ms

        all_results[(nr_runs, k_insert)] = times

        print(f"{'Size (words)':>12} | {'Avg insertion time (ms)':>25}")
        print("-" * 40)
        for size in sorted(times.keys()):
            print(f"{size:12} | {times[size]:25.6f}")


plt.figure(figsize=(12, 7))
for (nr_runs, k_insert), result in all_results.items():
    label = f"Words: {k_insert}"
    plt.plot(result.keys(), result.values(), marker='o', markersize=1, label=label)

plt.xlabel('Number of Words in Ternary Search Tree')
plt.ylabel('Average Insertion Time (ms)')
plt.title('Ternary Search Tree Insertion Performance')
plt.legend()
plt.grid(False)
plt.tight_layout()
plt.show()

plt.savefig("insertion_benchmark_plot.png")
