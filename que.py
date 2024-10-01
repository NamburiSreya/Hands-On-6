import random
import time
import matplotlib.pyplot as plt
import statistics

def partition_sort_fixed(arr):
    """
    Quicksort implementation with fixed pivot (middle element)
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return partition_sort_fixed(lesser) + equal + partition_sort_fixed(greater)

def partition_sort_random(arr):
    """
    Quicksort implementation with random pivot
    """
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return partition_sort_random(lesser) + equal + partition_sort_random(greater)

def measure_performance(sort_algorithm, datasets, iterations=5):
    """
    Measure the performance of a sorting algorithm over multiple iterations
    """
    performance_times = []
    for dataset in datasets:
        iteration_times = []
        for _ in range(iterations):
            start = time.time()
            sort_algorithm(dataset.copy())  # Use a copy to preserve original dataset
            end = time.time()
            iteration_times.append(end - start)
        performance_times.append(statistics.mean(iteration_times))
    return performance_times

# Configuration
MAX_ARRAY_SIZE = 200
ARRAY_SIZES = list(range(1, MAX_ARRAY_SIZE + 1))

# Generate datasets
optimal_case = [list(range(1, n + 1)) for n in ARRAY_SIZES]
pessimal_case = [list(range(n, 0, -1)) for n in ARRAY_SIZES]
typical_case = [random.sample(range(1, n + 1), n) for n in ARRAY_SIZES]

# Set up the plot
plt.figure(figsize=(12, 6))

# Plot fixed pivot quicksort performance
plt.subplot(1, 2, 1)
plt.plot(ARRAY_SIZES, measure_performance(partition_sort_fixed, optimal_case), label='Optimal Case')
plt.plot(ARRAY_SIZES, measure_performance(partition_sort_fixed, pessimal_case), label='Pessimal Case')
plt.plot(ARRAY_SIZES, measure_performance(partition_sort_fixed, typical_case), label='Typical Case')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Fixed Pivot Quicksort Performance')
plt.legend()

# Plot random pivot quicksort performance
plt.subplot(1, 2, 2)
plt.plot(ARRAY_SIZES, measure_performance(partition_sort_random, optimal_case), label='Optimal Case')
plt.plot(ARRAY_SIZES, measure_performance(partition_sort_random, pessimal_case), label='Pessimal Case')
plt.plot(ARRAY_SIZES, measure_performance(partition_sort_random, typical_case), label='Typical Case')
plt.xlabel('Array Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Random Pivot Quicksort Performance')
plt.legend()

plt.tight_layout()
plt.show()