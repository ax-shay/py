import heapq

class heapTutorial:
    def __init__(self, heap=[]):
        self.heap = heap

    def heapify(self):
        heapq.heapify(self.heap)
        print("Heapfiy:", self.heap)

    def heappush(self, elements):
        for elem in elements:
            heapq.heappush(heap, elem)
        print("Min-Heap:", heap)

    def heappop(self):
        sorted_elements = []
        """Using a for loop will give incorrect result as it is evaluated at the begining 
        for length and indices and as heap reshuflles itself after every pop to maintain the tree struct,
        the indices and length of self.heap will change"""
        while self.heap:
            e = heapq.heappop(self.heap)
            sorted_elements.append(e)
        print("Popped elements:", sorted_elements)

    def heappushpop(self, elem):
        """More efficient than pushing and popping individually"""
        e = heapq.heappushpop(self.heap, elem)
        print("After Push, and pop of smallest elem: ", self.heap)

    def heapreplace(self, elem):
        e = heapq.heapreplace(self.heap, elem)
        print("After Pop of smallest elem, and Push of elem: ", self.heap)


if __name__ == '__main__':
    heap = [2, 4, 6, 1, 3, 7]
    h = heapTutorial(heap)
    h.heapify()
    h.heappush([0, 10, -2, 5, 8, -8])
    h.heappop()
    h.heappush([0, 10, -2, 5, 8, -8])
    h.heappushpop(-3)
    h.heapreplace(4)
