import random
import heapq
import timeit
import matplotlib.pyplot as plt

def insertion_extraction(arr, x):
    heapq.heappush(arr, x)
    min_val = heapq.heappop(arr)
    return min_val

class PriorityQueue:
    def __init__(self):
        self._heap = []
    
    def insert(self, x):
        heapq.heappush(self._heap, x)
    
    def extract_min(self):
        if not self._heap:
            return None
        return heapq.heappop(self._heap)


arr = [random.randint(0, 100000) for _ in range(1000)]
pq = PriorityQueue()
insertion_extraction_times = []
extract_min_times = []

for i in range(1000):
    insertion_extraction_time = timeit.timeit(lambda: insertion_extraction(arr, i), number=10000)
    extract_min_time = timeit.timeit(lambda: pq.extract_min(), number=10000)
    insertion_extraction_times.append(insertion_extraction_time)
    extract_min_times.append(extract_min_time)

plt.hist(insertion_extraction_times, bins=20, alpha=0.5, label='Insertion and extraction')
plt.hist(extract_min_times, bins=20, alpha=0.5, label='Extract min')
plt.legend(loc='upper right')
plt.xlabel('Execution time (seconds)')
plt.ylabel('Frequency')
plt.savefig('insertion.png')
plt.show()

print(f"Insertion and extraction time: {min(insertion_extraction_times):.6f} seconds")
print(f"Extract min time: {min(extract_min_times):.6f} seconds")
