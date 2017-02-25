# python3


class HeapBuilder:
    def __init__(self):
        self.swaps = []
        self.array = []

    @property
    def size(self):
        return len(self.array)

    def ReadData(self):
        n = int(input())
        self.array = [int(s) for s in input().split()]
        assert n == self.size

    def printout(self):
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])

    def cright(self, index):
        cright = (2 * index) + 2
        if cright >= self.size:
            return -1
        return cright

    def cleft(self, index):
        cleft = (2 * index) + 1
        if cleft >= self.size:
            return -1
        return cleft


    def shiftdown(self, i):
        min_index = i
        l = self.cleft(i)
        r = self.cright(i)

        if l != -1 and self.array[l] < self.array[min_index]:
            min_index = l

        if r != - 1 and self.array[r] < self.array[min_index]:
            min_index = r

        if i != min_index:
            self.swaps.append((i, min_index))
            self.array[i], self.array[min_index] = \
                self.array[min_index], self.array[i]
            self.shiftdown(min_index)

    def generate_swaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
        for i in range(self.size // 2, -1, -1):
            self.shiftdown(i)

    def solve(self):
        self.ReadData()
        self.generate_swaps()
        self.printout()


if __name__ == "__main__":
    heap_builder = HeapBuilder()
    heap_builder.solve()