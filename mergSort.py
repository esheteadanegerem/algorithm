import random
import time

def merge_sort(arr):
    """
    Implementation of the merge sort algorithm.
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

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
    Runs tests on the merge sort algorithm with varying array sizes and presortedness levels.
    
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
                time_taken = measure_time(merge_sort, arr_copy)
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
    with open("merge_sort_results.txt", "w") as f:
        for result in results:
            f.write(f"Size: {result[0]}, Presortedness: {result[1]}, Avg Time: {result[2]}\n")
