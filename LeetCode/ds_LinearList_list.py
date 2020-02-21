
class SequenceList:
    def __init__(self, maxsize):
        self.max_size = maxsize
        self.seq_list = [None] * maxsize

    def create(self, nums):
        """the element nums is small than maxsize"""
        for i in range(len(nums)):
            self.seq_list[i] = nums[i]

    def length(self):
        """element None represents free space"""
        i = 0
        for i in range(self.max_size):
            if not self.seq_list[i]:
                break
        return i

    def is_empty(self):
        if len(self.seq_list):
            return False
        return True

    def get_elem(self, index):
        length = self.length()
        if length == 0 or index < 0 or index > length-1:
            return 'Error'
        return self.seq_list[index]

    def insert(self, index, num):
        length = self.length()
        if length == self.max_size:  # 线性表已满
            return 'error'
        if index < 0 or index > length-1:  # index不在范围内
            return 'error'
        for i in range(length, index, -1):
            self.seq_list[i] = self.seq_list[i-1]
        self.seq_list[index] = num

    def delete(self, index):
        length = self.length()
        if length == 0:
            return 'error'
        if index < 0 or index > length-1:
            return 'error'
        if index == length-1:
            self.seq_list[index] = None
        else:
            for i in range(index, length-1):
                self.seq_list[i] = self.seq_list[i+1]
            self.seq_list[length-1] = None


if __name__ == '__main__':
    seq_list = SequenceList(20)
    nums = [3, 2, 6, 7, 9, 1]
    seq_list.create(nums)

    length = seq_list.length()
    print('length', length)
    element = seq_list.get_elem(1)
    print('element', element)
    seq_list.insert(2, 10)
    print(seq_list.seq_list)
    length = seq_list.length()
    print('length', length)
    seq_list.delete(2)
    print(seq_list.seq_list)