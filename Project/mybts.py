# Python3 implementation of Max Heap
import sys
from TNode import *
import numpy as np
def parent(pos):
    return pos // 2


def right_child(pos):
    return (2 * pos) + 1


def left_child(pos):
    return 2 * pos


class MaxHeap:

    def __init__(self, maxsize: TNode):
        curr_node = maxsize
        self.maxsize = maxsize.value
        self.size = 0
        self.HeapVal = [0] * (self.maxsize + 1)
        self.HeapNode = [0] * (self.maxsize + 1)
        self.HeapVal[0] = sys.maxsize
        self.HeapNode = np.array(maxsize.value)
        print("WOW ", self.HeapNode)
        self.FRONT = 1

    # Function to return the position of parent for the node currently at pos

    # Function to return the position of the left child for the node currently at pos

    # Function to return the position of the right child for the node currently at pos

    # Function that returns true if the passed node is a leaf node
    def is_leaf(self, pos):

        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.HeapNode[fpos], self.HeapNode[spos] = (self.HeapNode[spos], self.HeapNode[fpos])
        self.HeapVal[fpos], self.HeapVal[spos] = (self.HeapVal[spos], self.HeapVal[fpos])

    # Function to heapify the node at pos
    def max_heapify(self, pos):

        # If the node is a non-leaf node and smaller than any of its child
        if not self.is_leaf(pos):
            if (self.HeapVal[pos] < self.HeapVal[left_child(pos)] or
                    self.HeapVal[pos] < self.HeapVal[right_child(pos)]):

                # Swap with the left child and heapify the left child
                if (self.HeapVal[left_child(pos)] >
                        self.HeapVal[right_child(pos)]):
                    self.swap(pos, left_child(pos))
                    self.max_heapify(left_child(pos))

                # Swap with the right child and heapify the right child
                else:
                    self.swap(pos, right_child(pos))
                    self.max_heapify(right_child(pos))

    # Function to insert a node into the heap
    def insert(self, element):

        if self.size >= self.maxsize:
            return
        self.size += 1
        self.HeapVal[self.size] = element

        current = self.size

        while self.HeapVal[current] > self.HeapVal[parent(current)]:
            self.swap(current, parent(current))
            current = parent(current)

    # Function to print the contents of the heap
    def print(self):

        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.HeapVal[i]) +
                  " LEFT CHILD : " + str(self.HeapVal[2 * i]) +
                  " RIGHT CHILD : " + str(self.HeapVal[2 * i + 1]))

    # Function to remove and return the maximum element from the heap
    def extract_max(self):

        popped = self.HeapVal[self.FRONT]
        self.HeapVal[self.FRONT] = self.HeapVal[self.size]
        self.max_heapify(self.FRONT)

        return popped


# Driver Code
# if __name__ == "__main__":
#     print('The maxHeap is ')
#
#     maxHeap = MaxHeap(15)
#     maxHeap.insert(5)
#     maxHeap.insert(3)
#     maxHeap.insert(17)
#     maxHeap.insert(10)
#     maxHeap.insert(84)
#     maxHeap.insert(19)
#     maxHeap.insert(6)
#     maxHeap.insert(22)
#     maxHeap.insert(9)
#
#     maxHeap.print()
#
#     print("The Max val is " + str(maxHeap.extract_max()))
