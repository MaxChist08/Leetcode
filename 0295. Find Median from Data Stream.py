class MedianFinder:
    def __init__(self):
        self.lst = list()

    def addNum(self, num):
        start = 0
        finish = len(self.lst) - 1

        while start <= finish:
            middle = (start + finish) // 2
            if self.lst[middle] <= num:
                start = middle + 1
            else:
                finish = middle - 1

        self.lst.insert(start, num)

    def findMedian(self):
        if len(self.lst) % 2 == 0:
            return (self.lst[len(self.lst) // 2 - 1] + self.lst[len(self.lst) // 2]) / 2
        return self.lst[len(self.lst) // 2]