import random
import time
import matplotlib.pyplot as plt
from ternary_search_tree import TernarySearchTree

with open('data/search_trees/corncob_lowercase.txt') as file:
    words = [line.strip() for line in file]

random.seed(42)

sizes = [100, 500, 1_000, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000]
samples = [random.sample(words, k=size) for size in sizes]

nr_runs_list = [30]
k_search_list = [50, 500, 1_500, 5_500, 10_000, 20_000, 30_000]

all_results = {}

for nr_runs in nr_runs_list:
    for k_search in k_search_list:
        print(f"\nBenchmark for nr_runs={nr_runs}, k_search={k_search}")
        times = {}
        search_sample = random.sample(words, k=k_search)
        for sample in samples:
            tstree = TernarySearchTree()
            for word in sample:
                tstree.insert(word)

            size = len(sample)
            total_time_ns = 0
            for _ in range(nr_runs):
                start_time = time.time_ns()
                for word in search_sample:
                    tstree.search(word)
                end_time = time.time_ns()
                total_time_ns += end_time - start_time

            avg_time_ms = total_time_ns / (nr_runs * 1_000_000.0)
            times[size] = avg_time_ms

        all_results[(nr_runs, k_search)] = times

        print(f"{'Size (words)':>12} | {'Avg search time (ms)':>25}")
        print("-" * 40)
        for size in sorted(times.keys()):
            print(f"{size:12} | {times[size]:25.6f}")

plt.figure(figsize=(12, 7))
for (nr_runs, k_search), result in all_results.items():
    label = f"Words: {k_search}"
    plt.plot(result.keys(), result.values(), marker='o', markersize=1, label=label)

plt.xlabel('Number of Words in Ternary Search Tree')
plt.ylabel('Average Search Time (ms)')
plt.title('Ternary Search Tree Search Performance')
plt.legend()
plt.grid(False)
plt.tight_layout()
plt.show()

plt.savefig("searching_benchmark_plot.png")