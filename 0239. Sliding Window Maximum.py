class Heap:
    def __init__(self):
        self.values = []

    def insert(self, data):
        self.values.append(data)
        self.siftUp(len(self.values) - 1)

    def siftUp(self, n):
        while n > 0:
            if n % 2 == 0:
                if self.values[(n - 2) // 2] < self.values[n]:
                    self.values[(n - 2) // 2], self.values[n] = self.values[n], self.values[(n - 2) // 2]
                    n = (n - 2) // 2
                else:
                    break
            else:
                if self.values[(n - 1) // 2] < self.values[n]:
                    self.values[(n - 1) // 2], self.values[n] = self.values[n], self.values[(n - 1) // 2]
                    n = (n - 1) // 2
                else:
                    break

    def the_biggest(self):
        return self.values[0]

    def get(self):
        self.values[0], self.values[len(self.values) - 1] = self.values[len(self.values) - 1], self.values[0]
        self.values.pop()
        self.siftDown(0)

    def siftDown(self, n):
        while n * 2 + 1 < len(self.values):
            if (n * 2 + 2 < len(self.values)) and (self.values[n * 2 + 2] > self.values[n * 2 + 1]) and (self.values[n * 2 + 2] > self.values[n]):
                self.values[n * 2 + 2], self.values[n] =  self.values[n], self.values[n * 2 + 2]
                n = n * 2 + 2
            elif self.values[n * 2 + 1] > self.values[n]:
                self.values[n * 2 + 1], self.values[n] = self.values[n], self.values[n * 2 + 1]
                n = n * 2 + 1
            else:
                break

def max_sliding_window(nums, k):
    dict_of_cur_nums = dict()
    heap_of_cur_nums = Heap()
    ans = list()

    for i in range(k):
        if nums[i] in dict_of_cur_nums:
            dict_of_cur_nums[nums[i]] += 1
        else:
            dict_of_cur_nums[nums[i]] = 1
        heap_of_cur_nums.insert(nums[i])
    ans.append(heap_of_cur_nums.the_biggest())

    for i in range(k, len(nums)):
        dict_of_cur_nums[nums[i - k]] -= 1
        heap_of_cur_nums.insert(nums[i])
        if nums[i] in dict_of_cur_nums:
            dict_of_cur_nums[nums[i]] += 1
        else:
            dict_of_cur_nums[nums[i]] = 1

        while dict_of_cur_nums[heap_of_cur_nums.the_biggest()] == 0:
            heap_of_cur_nums.get()
        ans.append(heap_of_cur_nums.the_biggest())

    return ans