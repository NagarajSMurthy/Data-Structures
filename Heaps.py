
from heapq import heappop, heappush, heapify

heap = []       # To store the items
nums = [12, 3, -2, 6, 7, 90, 23]

for num in nums:
    heappush(heap, num)  # push data from nums to the heap

while heap: # while heap is not null(empty)
    print(heappop(heap))  # heappop - pops(returns) the data from the root node


# Apart from heappush and heappop, heapify also does the same thing

heapify(nums)  # creates a heap (not min or max heap) from the nums array 

print(nums)
