class MinHeap:
    def __init__(self, item = []):
        self.heapList = item

    def bubbleUp(self, item):
        while item // 2 > 0:
            if self.heapList[item] < self.heapList[item // 2]:
                tmp = self.heapList[item // 2]
                self.heapList[item // 2] = self.heapList[item]
                self.heapList[item] = tmp
                item = item // 2
            else:
                item = 0

    def bubbleDown(self, item):
        while (item * 2+1) <= self.heapSize:
            mc = self.minChild(item)
            if self.heapList[item] > self.heapList[mc]:
                tmp = self.heapList[item]
                self.heapList[item] = self.heapList[mc]
                self.heapList[mc] = tmp
            item = mc

    def insert(self, node):
        self.heapList.append(node)
        self.heapSize += 1
        self.bubbleUp(self.heapSize)

    def minChild(self,item):
        if item * 2 + 1 > self.heapSize:
            return item
        else:
            if self.heapList[item*2+1] < self.heapList[item*2+2]:
                return item * 2+1 #left
            else:
                return item * 2 + 2 #right children

    def delMin(self):
        retval = self.heapList[0]
        self.heapList[0] = self.heapList[self.heapSize]
        self.heapSize = self.heapSize - 1
        self.heapList.pop()
        self.bubbleDown(0)
        return retval

    def buildHeap(self,alist):
        print(alist)
        i = len(alist) // 2
        self.heapSize = len(alist)
        self.heapList = [] + alist[:]
        while (i > 0):
            self.bubbleDown(i)
            i = i - 1


    def __str__(self):
        return "{}".format(self.data)

    def peak(self):
        if self.is_empty():
            return "Heap is empty"
        return self.heapList[0]

    def is_empty(self):
        return len(self.heapList) == 0

    def pop(self):
        if self.is_empty():
            return "Heap is empty"
        else:
            return self.heapList.pop()

mh = MinHeap()
mh.buildHeap([12,4,7,9,10,2,1])
print(mh.delMin(0))
print(mh.delMin(1))
print(mh.delMin(2))
