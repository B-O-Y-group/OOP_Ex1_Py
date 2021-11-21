from TNode import TNode
from TRange import TRange
from Esort import *


class ERange:
    def __init__(self, traffic_list: BTraffic, el_list: ESort):

        """ Data structures : """

        self.t_list = traffic_list
        self.elevator_list = el_list.sort_elev
        self.range_tree = TRange(self.t_list, self.elevator_list)

        '''------> init the tree '''
        self.pointer = 0
        self.range_tree.root.set_elev(el_list.sort_elev.__getitem__(self.pointer).id)

        '''------> split the first NODE'''
        self.target = self.t_list.val_range_list.__getitem__(self.pointer) * int(
            self.t_list.final_range_list.__getitem__(self.pointer))
        next_n = self.split(self.range_tree.root.range, self.target)
        self.range_tree.root.allocate_to_node(next_n["i"], next_n["j"])
        self.range_tree.addAfterSplit(self.range_tree.root, traffic_list)
        self.range_tree.max_list.append(self.range_tree.root)
        self.range_tree.max_list.sort()
        self.pointer += 1

        ''' -----> allocate all elevators'''

        for i in range(len(self.elevator_list) - 1):
            curr = self.range_tree.max_list.__getitem__(0)

            self.target = self.t_list.val_range_list.__getitem__(self.pointer) * int(
                self.t_list.final_range_list.__getitem__(self.pointer))
            curr.set_elev(el_list.sort_elev.__getitem__(self.pointer).id)
            self.pointer += 1
            next_n = self.split(curr.range, self.target)
            curr.allocate_to_node(int(next_n["i"]), int(next_n["j"]))
            self.range_tree.addAfterSplit(curr, traffic_list)
            self.range_tree.max_list.sort()

        print2DUtil(self.range_tree.root, 1)

    '''SPLIT function here --------> '''

    def split(self, n_range: TNode, target):

        i = int(n_range["i"])
        val = self.t_list.get_traffic(i, i + 1) / 2
        ranges = {"left": i, "right": i + 1}

        # print("check range: ", n_range["j"])
        while i < int(n_range["j"]) - 1:
            j = i + 1
            while j < int(n_range["j"]):
                if self.t_list.get_traffic(i, j) / (j - i) > val and self.t_list.get_traffic(i, j) <= int(target):
                    val = self.t_list.get_traffic(i, j)
                    ranges["left"] = i
                    ranges["right"] = j
                j += 1
            i += 1

        return {"i": ranges["left"], "j": ranges["right"], "val": val}


COUNT = [10]

'''function to print tree (not a great one) --> taken from web'''


def print2DUtil(root, space):
    # Base case
    if (root == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root)

    # Process left child
    print2DUtil(root.mid, space)
    print2DUtil(root.left, space)
