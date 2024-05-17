import random
import time

def partition(arr, low, high):
    """
    Helper function to partition the array around a pivot.
    
    :param arr: The array to partition.
    :param low: The starting index of the partition range.
    :param high: The ending index of the partition range.
    :return: The index of the pivot element after partitioning.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    """
    Implementation of the quick sort algorithm.
    
    :param arr: The array to be sorted.
    :param low: The starting index of the array segment to be sorted.
    :param high: The ending index of the array segment to be sorted.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def generate_array(size, presortedness):
    """
    Generates an array of the given size with a specified level of presortedness.
    
    :param size: The size of the array to generate.
    :param presortedness: The degree to which the array is presorted (0 to 1).
    :return: A list of integers.
    """
    arr = list(range(size))
    if presortedness == 0:
        # Reverse the array for minimum presortedness
        arr.reverse()
    elif presortedness == 1:
        # Already sorted array for maximum presortedness
        pass
    else:
        # Shuffle the array for random disorder
        random.shuffle(arr)
        presorted_elements = int(size * presortedness)
        arr[:presorted_elements] = sorted(arr[:presorted_elements])
    return arr

def measure_time(func, *args):
    """
    Measures the time taken to execute a given function with the provided arguments.
    
    :param func: The function to measure.
    :param args: The arguments to pass to the function.
    :return: The time taken in seconds.
    """
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

def run_tests(values_start, values_stop, steps, presortedness_values, rep):
    """
    Runs tests on the quick sort algorithm with varying array sizes and presortedness levels.
    
    :param values_start: The starting size of the arrays.
    :param values_stop: The maximum size of the arrays.
    :param steps: The number of intervals to divide the size range.
    :param presortedness_values: A list of presortedness levels to test.
    :param rep: The number of repetitions for each test.
    :return: A list of tuples containing the size, presortedness, and average time taken.
    """
    results = []
    step_size = (values_stop - values_start) // steps
    sizes = range(values_start, values_stop + 1, step_size)
    
    for size in sizes:
        for presortedness in presortedness_values:
            times = []
            for _ in range(rep):
                arr = generate_array(size, presortedness)
                arr_copy = arr[:]
                time_taken = measure_time(quick_sort, arr_copy, 0, len(arr_copy) - 1)
                times.append(time_taken)
            avg_time = sum(times) / rep
            results.append((size, presortedness, avg_time))
            print(f'Size: {size}, Presortedness: {presortedness}, Avg Time: {avg_time}')
    return results

if __name__ == "__main__":
    # Define parameters
    values_start = 0  # Minimum number of entries to sort
    values_stop = 100000  # Maximum number of entries to sort
    steps = 1000  # Number of intervals
    presortedness_values = [0, 0.05, 0.5, 1]  # Presortedness levels to test
    rep = 10  # Number of repetitions for each test
    
    # Run the tests and gather results
    results = run_tests(values_start, values_stop, steps, presortedness_values, rep)
    
    # Write results to a file for further analysis
    with open("quick_sort_results.txt", "w") as f:
        for result in results:
            f.write(f"Size: {result[0]}, Presortedness: {result[1]}, Avg Time: {result[2]}\n")
