import random
import time
import numpy as np
import matplotlib.pyplot as plt

def heapify(arr, n, i):
    """
    Helper function to maintain the heap property of a subtree rooted at index i.
    
    :param arr: The array representing the heap.
    :param n: The size of the heap.
    :param i: The root index of the subtree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child is larger than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child is larger than the largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heap_sort(arr):
    """
    Implementation of the heap sort algorithm.
    
    :param arr: The array to be sorted.
    """
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)  # Heapify the root element

def generate_array(size, presortedness):
    """
    Generates an array of the given size with a specified level of presortedness.
    
    :param size: The size of the array to generate.
    :param presortedness: The degree to which the array is presorted (0 to 1).
    :return: A list of integers.
    """
    arr = list(range(size))  # Generate a list of integers from 0 to size-1
    if presortedness == 0:
        arr.reverse()  # Reverse the array for minimum presortedness
    elif presortedness == 1:
        pass  # Already sorted array for maximum presortedness
    else:
        random.shuffle(arr)  # Shuffle the array for random disorder
        presorted_elements = int(size * presortedness)
        arr[:presorted_elements] = sorted(arr[:presorted_elements])  # Partially sort based on presortedness
    return arr

def measure_time(func, *args):
    """
    Measures the time taken to execute a given function with the provided arguments.
    
    :param func: The function to measure.
    :param args: The arguments to pass to the function.
    :return: The time taken in seconds.
    """
    start = time.time()  # Start time
    func(*args)  # Execute function
    end = time.time()  # End time
    return end - start  # Time taken

def run_tests(values_start, values_stop, steps, presortedness_values, rep):
    """
    Runs tests on the heap sort algorithm with varying array sizes and presortedness levels.
    
    :param values_start: The starting size of the arrays.
    :param values_stop: The maximum size of the arrays.
    :param steps: The number of intervals to divide the size range.
    :param presortedness_values: A list of presortedness levels to test.
    :param rep: The number of repetitions for each test.
    :return: A dictionary containing the average time taken for each presortedness level.
    """
    results = {level: [] for level in presortedness_values}  # Initialize results dictionary
    step_size = (values_stop - values_start) // steps  # Calculate step size
    sizes = range(values_start, values_stop + 1, step_size)  # Generate sizes to test
    
    for size in sizes:
        for presortedness in presortedness_values:
            times = []
            for _ in range(rep):
                arr = generate_array(size, presortedness)  # Generate array
                arr_copy = arr[:]  # Copy array to avoid in-place sorting issues
                time_taken = measure_time(heap_sort, arr_copy)  # Measure time taken to sort
                times.append(time_taken)  # Record time
            avg_time = sum(times) / rep  # Calculate average time
            results[presortedness].append(avg_time)  # Store average time
            print(f'Size: {size}, Presortedness: {presortedness}, Avg Time: {avg_time:.5f}')  # Print results
    
    # Plot results
    for presortedness, times in results.items():
        plt.plot(sizes, times, label=f"Presortedness = {presortedness}")

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Heap Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    values_start = 0  # Minimum number of entries to sort
    values_stop = 1000  # Maximum number of entries to sort
    steps = 100  # Number of intervals
    presortedness_values = [0, 0.5, 1]  # Presortedness levels to test
    rep = 5  # Number of repetitions for each test
    
    run_tests(values_start, values_stop, steps, presortedness_values, rep)  # Run tests
