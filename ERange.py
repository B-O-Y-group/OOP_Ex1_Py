from TNode import TNode
from TRange import TRange
from BTraffic import *
from Esort import *
from mybts import MaxHeap


class ERange:
    def __init__(self, traffic_list: BTraffic, el_list: ESort):
        '''new idea ----->'''

        """ Data structures : """

        self.t_list = traffic_list
        self.elevator_list = el_list.sort_elev
        self.range_tree = TRange(self.t_list, self.elevator_list)

        '''------> init the tree '''
        self.pointer = 0
        self.range_tree.root.set_elev(el_list.sort_elev.__getitem__(self.pointer).id)
        print("curr node el_id -------> ", self.range_tree.root.elev_id)

        '''------> split the first NODE'''
        self.target = 1001 / 1.6
        # self.target = traffic_list.get_traffic(traffic_list.getMinFloor(), traffic_list.getMaxFloor()) / (
        #     len(traffic_list.get_el_list()))
        next_n = self.split(self.range_tree.root.range, self.target)
        self.range_tree.root.allocate_to_node(next_n["i"], next_n["j"])
        print("root split ", self.range_tree.root.split)
        # print(next_n["val"])
        self.range_tree.addAfterSplit(self.range_tree.root, traffic_list)
        self.range_tree.max_list.append(self.range_tree.root)
        self.range_tree.max_list.sort()
        print(self.range_tree.max_list)
        self.pointer += 1
        print("the fking pointer ", self.pointer)

        ''' -----> allocate all elevators'''

        for i in range(len(self.elevator_list) - 1):
            curr = self.range_tree.max_list.__getitem__(0)

            self.target /= 1.6
            # self.target = traffic_list.get_traffic(curr.range["i"], curr.range["j"]) / (
            #         len(traffic_list.get_el_list()) - self.pointer)  # need to fix target
            curr.set_elev(el_list.sort_elev.__getitem__(self.pointer).id)
            print("KOKO", curr.range, "the ELEV ", el_list.sort_elev.__getitem__(self.pointer).id)
            print("CURR ALO ", curr.elev_id)
            print(self.range_tree.max_list)
            self.pointer += 1
            next_n = self.split(curr.range, self.target)
            curr.allocate_to_node(int(next_n["i"]), int(next_n["j"]))
            self.range_tree.addAfterSplit(curr, traffic_list)
            self.range_tree.max_list.sort()
            print(self.range_tree.max_list)
        print("Traffic problem ", traffic_list.get_traffic(traffic_list.getMinFloor(), traffic_list.getMaxFloor()))
        print("HOW MANY ELEVATORS ", len(self.t_list.get_el_list()))
        print("MIN_F ", traffic_list.getMinFloor(), "MAX_F ", traffic_list.getMaxFloor(), "HOW MANY FLOORS ",
              self.t_list.get_num_floor())

        print2DUtil(self.range_tree.root, 1)

    '''SPLIT function here --------> '''

    def split(self, n_range: TNode, target):
        # sub_range = {"x": n_range["i"], "y": n_range["i"] + target}





        i = int(n_range["i"])
        val = self.t_list.get_traffic(i, i + 1) / 2
        ranges = {"left": i, "right": i + 1}

        # print("check range: ", n_range["j"])
        while i < int(n_range["j"]) - 1:
            j = i + 1
            while j < int(n_range["j"]):
                if self.t_list.get_traffic(i, j) / (j - i) > val and self.t_list.get_traffic(i, j) <= target:
                    val = self.t_list.get_traffic(i, j)
                    ranges["left"] = i
                    ranges["right"] = j
                j += 1
            i += 1

        return {"i": ranges["left"], "j": ranges["right"], "val": val}


COUNT = [10]


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
