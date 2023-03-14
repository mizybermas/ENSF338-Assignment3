import requests
import json
import time
import matplotlib.pyplot as plt
import timeit

dataUrl = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2data.json"

searchTasksUrl = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment3/ex2tasks.json"


def binary_search(arr, target, initial_midpoint):

    low, high = 0, len(arr) - 1

    while low <= high:
        # set mid to initial_midpoint for first iteration
        if low == 0 and high == len(arr) - 1:
            mid = initial_midpoint
        else:
            mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found in array


data = json.loads(requests.get(dataUrl).text)

searchTasks = json.loads(requests.get(searchTasksUrl).text)

x = []
y = []

for i in searchTasks:

    result = timeit.timeit(stmt="binary_search(data, i, 0)",
                           globals=globals(), number=5000)

    x.append(i)
    y.append(result/5000)

plt.title("Midpoint set to beginning of array")
plt.xlabel("Search target value")
plt.ylabel("Time(s)")
plt.scatter(x, y)
plt.savefig("midpoint_beginning.png")
plt.clf()

x = []
y = []

for i in searchTasks:

    result = timeit.timeit(stmt="binary_search(data, i, len(data) - 1)",
                           globals=globals(), number=5000)

    x.append(i)
    y.append(result/5000)

plt.title("Midpoint set to end of array")
plt.xlabel("Search target value")
plt.ylabel("Time(s)")
plt.scatter(x, y)
plt.savefig("midpoint_end.png")
plt.clf()

x = []
y = []

for i in searchTasks:

    result = timeit.timeit(stmt="binary_search(data, i, len(data) // 2)",
                           globals=globals(), number=5000)

    x.append(i)
    y.append(result/5000)

plt.title("Midpoint set to middle of array")
plt.xlabel("Search target value")
plt.ylabel("Time(s)")
plt.scatter(x, y)
plt.savefig("midpoint_mid.png")
plt.clf()


x = []
y = []

for i in searchTasks:

    result = timeit.timeit(stmt="binary_search(data, i, int(len(data)//(4/3)))",
                           globals=globals(), number=5000)

    x.append(i)
    y.append(result/5000)

plt.title("Midpoint set to 3/4 of array")
plt.xlabel("Search target value")
plt.ylabel("Time(s)")
plt.scatter(x, y)
plt.savefig("midpoint_3quarters.png")
plt.clf()

x = []
y = []

for i in searchTasks:

    result = timeit.timeit(stmt="binary_search(data, i, len(data)//4)",
                           globals=globals(), number=5000)

    x.append(i)
    y.append(result/5000)

plt.title("Midpoint set to 1/4 of array")
plt.xlabel("Search target value")
plt.ylabel("Time(s)")
plt.scatter(x, y)
plt.savefig("midpoint_1quarter.png")
plt.clf()
