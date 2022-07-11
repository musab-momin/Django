#Given the root node of a treen, return and arrayy where each element.
#is the width of the tree at each level.
#Example
#input:
#     0
#    / | \
#   1  2  3  
#   |     |
#   4     5

#output: [1, 3, 2]

class Node:
    def __init__(self, data):
        self.data = data
        self.childrens = []

    def add(self, data):
        node = Node(data) 
        self.childrens.append(node)
        return node

    def remove(self, data):
        for child in self.childrens:
            if child.data == data:
                self.childrens.remove(child)


class Tree:
    def __init__(self):
        self.root = None

    def traverse_bf(self, fn):
        nodes = [self.root]
        while(len(nodes)):
            node = nodes.pop(0)
            for child in node.childrens:
                nodes.append(child)
            fn(node)


    def traverse_df(self, fn):
        nodes = [self.root]
        while(len(nodes)):
            node = nodes.pop(0)
            for index in range(len(node.childrens)-1, -1, -1):
                nodes.insert(0, node.childrens[index])
            fn(node)
        
    def solution(self):
        nodes = [self.root, 's']
        levels = [1, 0]

        while(len(nodes)>1):
            node = nodes.pop(0)
            if node == 's':
                nodes.append('s')
                levels.append(0)
            else:
                for child in node.childrens:
                    nodes.append(child)
                    levels[-1] += 1
               
        return  levels


root_node = Node(0)
child_one = root_node.add(1)
child_one.add(4)

child_two = root_node.add(2)

child_three = root_node.add(3)
child_three.add(5)


tree = Tree()
tree.root = root_node

# def call_back(node):
#     print(node.data, end=' -> ')

# tree.traverse_bf(call_back)

ans = tree.solution()
# print(ans)