import random
import time
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(arr):
    """
    Implementation of the merge sort algorithm.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def generate_array(size, presortedness):
    """
    Generates an array of the given size with a specified level of presortedness.
    
    :param size: The size of the array to generate.
    :param presortedness: The degree to which the array is presorted (0 to 1).
    :return: A list of integers.
    """
    arr = list(range(size))
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
    Runs tests on the merge sort algorithm with varying array sizes and presortedness levels.
    
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
                time_taken = measure_time(merge_sort, arr_copy)  # Measure time taken to sort
                times.append(time_taken)  # Record time
            avg_time = sum(times) / rep  # Calculate average time
            results[presortedness].append(avg_time)  # Store average time
            print(f'Size: {size}, Presortedness: {presortedness}, Avg Time: {avg_time:.5f}')  # Print results
    
    # Plot results
    for presortedness, times in results.items():
        plt.plot(sizes, times, label=f"Presortedness = {presortedness}")

    plt.xlabel('Array Size')
    plt.ylabel('Time (seconds)')
    plt.title('Merge Sort Performance')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    values_start = 1000  # Minimum number of entries to sort
    values_stop = 200000  # Maximum number of entries to sort
    steps = 20  # Number of intervals
    presortedness_values = [0, 0.5, 1]  # Presortedness levels to test
    rep = 5  # Number of repetitions for each test
    
    run_tests(values_start, values_stop, steps, presortedness_values, rep)  # Run tests
