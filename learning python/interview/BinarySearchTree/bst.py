#Directions
#1) Implement the NOde calss to create a binary search tree.
#The constructor should initialize values 'data', 'left', and 'right.
#2)IMple the 'insert' metod for the Node cals..
#Insert should accept and argument 'data',
#then create an insert a new node at the appropriate location in the tree.
#3)Implement the 'contains' methdo for the Node class.
#Contains should accept a 'dta' argument and return the Node
#in the tree with the same value. If the value isn't in the tree return null.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        #checking the data is less and parent node and there is a left node present.
        if (data < self.data and self.left):
            self.left.insert(data)
        #cheing the data is less and parent node doesn't have have left node so we create the left node.
        elif (data < self.data):
            self.left = Node(data)
        #checking the data is greater and parent node and there is a right node present.
        if (data > self.data and self.right):
            self.right.insert(data)
        #cheing the data is greater and parent node doesn't have have right node so we create the left node.   
        elif (data> self.data):
            self.right = Node(data)
    
    #this is bfs I coded this by my self. :)
    def print(self):
        arr = [self]
        while(len(arr)>0):
            node = arr.pop(0)
            print(node.data, end=' -> ')
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)
    

    def contains(self, element):
        arr = []

        if element == self.data:
            return self
        
        if element > self.data and self.right:
            return self.right.contains(element)
           
        elif element < self.data and self.left:
           return self.left.contains(element)
        
        return None


root_nod = Node(10)
root_nod.insert(0)
root_nod.insert(12)
root_nod.insert(-1)
root_nod.insert(5)
root_nod.insert(11)
root_nod.insert(20)
root_nod.insert(17)
root_nod.insert(99)
root_nod.insert(-21)

#for visual output refere note.txt file
# root_nod.print()

ans = root_nod.contains(20)
print(ans.data if ans else ans)


       