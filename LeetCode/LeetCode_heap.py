import heapq

class Heap:
    def __init__(self, k, nums):
        self.k = k
        self.heap = self.k_largest(nums)
        heapq.heapify(self.heap)

    def pop(self):
        pile = heapq.heappop(self.heap)  # 弹出最小值，更新堆
        return pile

    def peek(self):
        return self.heap[0]

    def push(self, num):
        heapq.heappush(self.heap, num)  # 插入到数组最后, 无返回值
        heapq.heapify(self.heap)  # 转化为堆，无返回值

    def replace(self, num):
        return heapq.heapreplace(self.heap, num)  # 替换最小值

    def k_largest(self, nums):
        return heapq.nlargest(self.k, nums)

    def k_smallest(self, nums):
        return heapq.nsmallest(self.k, nums)

if __name__ == '__main__':
    k = 5
    nums = [1, 8, 2, 23, 7, -4, 18]
    heap = Heap(k, nums)
    print(heap.heap)
    heap.pop()
    print(heap.heap)
    print(heap.peek())
    print(heap.heap)
    heap.push(1)
    print(heap.heap)












# k_largest = heapq.nlargest(k, nums)  # 最大根堆
# k_smallest = heapq.nsmallest(k, nums)  # 最小根堆
#
# print(k_largest)
# print(k_smallest)
#
#
# heap = nums
# heapq.heapify(heap)
# print(heap)
#
# c = heapq.heappop(heap)
# print(c)
#
# heapq.heappush(heap, -5)
# print(heap)







# def heap_adjust(array, start, end):
#     temp = array[start]
#     child = 2 * start
#     while child <= end:
#         if child < end and array[child] < array[child + 1]:
#             child += 1
#         if temp >= array[child]:
#             break
#         array[start] = array[child]
#         start = child
#         child *= 2
#     array[start] = temp
#
#
# def heap_sort(array):
#     # 从最后一个有孩子结点的结点开始调整最大堆
#     first = len(array) // 2 - 1
#     for start in range(first, -1, -1):
#         heap_adjust(array, start, len(array) - 1)
#
#     # 将最大的数放到堆的最后一个位置，并继续调整排序
#     for end in range(len(array) - 1, 0, -1):
#         array[0], array[end] = array[end], array[0]
#         heap_adjust(array, 0, end - 1)
#
#
# if __name__ == "__main__":
#     array = [1, 4, 5, 0, 2, 7, 9, 10, 3, 6]
#     heap_sort(array)
#     print(array)