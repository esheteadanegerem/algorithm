import numpy as np
import time
import matplotlib.pyplot as plt
from heapq import heapify, heappop

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Heap Sort
def heap_sort(arr):
    arr = list(arr)  # Convert numpy array to list
    heapify(arr)
    sorted_arr = [heappop(arr) for _ in range(len(arr))]
    arr[:] = sorted_arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Utility functions to create test arrays
def create_array(size, presortedness):
    arr = np.arange(size)
    if presortedness == 0:
        arr = arr[::-1]
    elif presortedness == 0.5:
        np.random.shuffle(arr)
    return arr

def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Parameters
start = 0
stop = 1000
steps = 100
presortedness_values = [0, 0.5, 1]
reps = 5

# Running the tests
sizes = range(start, stop + 1, steps)
sort_functions = {
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Heap Sort": heap_sort,
    "Quick Sort": quick_sort,
    "Selection Sort": selection_sort
}

# Store results
results = {name: {ps: [] for ps in presortedness_values} for name in sort_functions.keys()}

for size in sizes:
    for ps in presortedness_values:
        for _ in range(reps):
            arr = create_array(size, ps)
            for name, sort_function in sort_functions.items():
                time_taken = measure_sorting_time(sort_function, arr)
                results[name][ps].append(time_taken)

# Averaging the results
avg_results = {name: {ps: [] for ps in presortedness_values} for name in sort_functions.keys()}
for name, presortedness_data in results.items():
    for ps, times in presortedness_data.items():
        avg_results[name][ps] = [np.mean(times[i:i+reps]) for i in range(0, len(times), reps)]

# Plotting the results
plt.figure(figsize=(15, 10))

for name, presortedness_data in avg_results.items():
    for ps, avg_times in presortedness_data.items():
        plt.plot(sizes, avg_times, label=f"{name}, Presortedness={ps}")

plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.title('Sorting Algorithms Performance')
plt.legend()
plt.grid(True)
plt.show()
