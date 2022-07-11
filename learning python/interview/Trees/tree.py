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


node = Node(20)
child_node = node.add(0)
child_node.add(12)
child_node.add(-2)
child_node.add(1)
node.add(40)
child_node2 = node.add(-15)
child_node2.add(-2)

tree = Tree()
tree.root = node

def call_back(node):
    print(node.data, end=' -> ')

tree.traverse_bf(call_back)
print('')
tree.traverse_df(call_back)


