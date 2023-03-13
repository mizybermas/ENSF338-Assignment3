import random
import timeit
import matplotlib.pyplot as plt

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr = [i for i in range(1000)]
target = random.randint(0, 999)

linear_times = []
binary_times = []

for i in range(100):
    linear_time = timeit.timeit(lambda: linear_search(arr, target), number=1000)
    binary_time = timeit.timeit(lambda: binary_search(arr, target), number=1000)
    linear_times.append(linear_time)
    binary_times.append(binary_time)

plt.hist(linear_times, bins=20, alpha=0.5, label='Linear Search')
plt.hist(binary_times, bins=20, alpha=0.5, label='Binary Search')
plt.legend(loc='upper right')
plt.savefig('sorted_array.png')
plt.show()

print("Linear Search Time (min):", min(linear_times))
print("Binary Search Time (min):", min(binary_times))