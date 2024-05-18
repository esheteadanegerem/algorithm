import random
import time
import numpy as np
import matplotlib.pyplot as plt

def generate_array(size, presortedness):
    arr = list(range(size))
    if presortedness == 1:
        return arr
    elif presortedness == 0:
        return arr[::-1]
    else:
        random.shuffle(arr)
        return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def measure_time(sort_function, arr):
    start_time = time.perf_counter()
    sort_function(arr.copy())  # use a copy to avoid sorting in place
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    start = 0  # Start from 1000 to avoid size 0
    stop = 1000
    steps = 100
    presortedness_levels = [0, 0.5, 1]
    rep = 5

    sizes = list(range(start, stop + 1, steps))
    results = {level: [] for level in presortedness_levels}

    for size in sizes:
        for presortedness in presortedness_levels:
            total_time = 0
            for _ in range(rep):
                arr = generate_array(size, presortedness)
                total_time += measure_time(insertion_sort, arr)
            avg_time = total_time / rep
            results[presortedness].append(avg_time)
            print(f"Size: {size}, Presortedness: {presortedness}, Time: {avg_time:.5f}")

    for presortedness, times in results.items():
        plt.plot(sizes, times, label=f"Presortedness = {presortedness}")

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Insertion Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
