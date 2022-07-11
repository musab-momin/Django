class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



# node_one = Node('Hi')
# print(node_one.data)
# print(node_one.next)

# node_two = Node('There', node_one)
# print(node_two.data)
# next_node = node_two.next
# print(next_node.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        self.head = Node(data, self.head)
    

    def insert_last(self, data):
        new_node = Node(data)
        if self.head != None:
            node = self.get_last()
            node.next = new_node
        else:
            self.head = new_node


    def size(self):
        counter = 0
        node = self.head
        while(node):
            counter+=1
            node = node.next
        return counter
    
    def get_first(self):
        return self.head

    
    def get_last(self):
        node = self.head
        while(node.next):
            if node.next != None:
                node = node.next
        return node

    
    def remove_first(self):
        node = self.head
        self.head = node.next


    def remove_last(self):
        if(self.head != None):
            previouse = self.head
            if previouse.next != None:
                node = previouse.next
                while node.next != None:
                    previouse = node
                    node = previouse.next
                previouse.next = None
            else:
                self.head = None
        else:
            return 'Linked List in empty'


    def get_at(self, index):
        if self.head:
            node = self.head
            counter = 0
            length = self.size() - 1
            if index <= length and index >= 0:
                while(counter != index):
                    node = node.next
                    counter += 1
                return node
            else:
                raise Exception('Index out of boud')
        else:
            return self.head


    def remove_at(self, index):
        if self.head:
            if index == 0 and index >= 0:
                self.head = self.head.next
            elif index <= self.size() and index >= 0:
                previouse = self.get_at(index-1)
                node = self.get_at(index)
                previouse.next = node.next
            else:
                raise Exception('Index out of bound')
        else:
            raise Exception('Linked list is empty')


    def insert_at(self, data, index):
        if self.head !=None or index < 0:
            length = self.size()-1
            if index <= length:
                previous = self.get_at(index-1)
                previous.next = Node(data, self.get_at(index))
            else:
                node = self.get_last()
                node.next = Node(data)
        else:
            print('-*-*-*-*-*-*-*')
            self.head = self.insert_first(data)


    def for_each(self, cb):
        if self.head:
            node = self.head
            while(node):
                cb(node)
                node = node.next
        else:
            raise Exception('Linked list is empty')

    def clear(self):
        self.head = None


# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# print(link_list.size())   #output: 3

# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# print(link_list.get_first().data) #output: hows it gogin
# print(link_list.get_last().data)  #output: Hi

# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# link_list.clear()
# print(link_list.size()) #0

# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# link_list.remove_first()
# print(link_list.get_first().data) #Their

# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# link_list.remove_last() #removes hows it going
# print(link_list.get_last().data) #Their


# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# link_list.insert_last('Good! What about you ?')
# print(link_list.get_last().data)


# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# node_four = link_list.insert_first('Good! What about you ?')

# print(link_list.get_at(2).data) #output: their


# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# node_four = link_list.insert_first('Good! What about you ?')

# link_list.remove_at(2) #removing Their
# print(link_list.get_at(2).data) #now Hi is at 2 index 



# link_list = LinkedList()
# node_first = link_list.insert_first('Hi')
# node_two = link_list.insert_first('Their')
# node_three = link_list.insert_first('Hows it going')
# node_four = link_list.insert_first('Good! What about you ?')

# link_list.insert_at('Greate!', 2)
# print(link_list.get_at(2).data, link_list.get_at(2).next.data)


# def call_back(node):
#     node.data += 10
#     print(node.data)


# link_list = LinkedList()
# node_first = link_list.insert_first(1)
# node_two = link_list.insert_first(2)
# node_three = link_list.insert_first(3)
# node_four = link_list.insert_first(4)
# link_list.for_each(call_back)



##################################################
#write a function that takes likeedlist as argument and return the midpoint of the linkedlist
#do not use size  and iteration is allowed. If the linkedlist have even numbers of node returns the last node of first falh


#explanation: 
#we take two variable slow and fast, We start iterating the linked list but in each iteration we increment fast by two node 
#and slow by one node if fast don't have two more nodes in to travel in list than we stop and return the node which is 
#at slow

# def find_midpoint(link_list):
#     if link_list.head.next:
#         node = link_list.head
#         slow = node
#         fast = node
          #check if fast and two more nodes to travel or not
#         while(fast.next and fast.next.next):
#             slow = slow.next
#             fast = fast.next.next
#         print(slow.data)


#     else:
#         print( link_list.head.data )


# link_list = LinkedList()
# node_first = link_list.insert_first('green')
# node_two = link_list.insert_first('blue')
# node_three = link_list.insert_first('red')
# node_four = link_list.insert_first('orange')
# node_five = link_list.insert_first('grey')
# node_six = link_list.insert_first('white')
# find_midpoint(link_list) 


######################################################
#Given a linked list and integer n, return the element n
#spaces from the last node in the list. Do not call the 
#size method of the linked list. Assume that n will always
#be less than the length of the list.

# def from_last(list, n):
#     node = list.head
#     if node != None:
#         slow = node
#         fast = node

#         #for first interation increment fast by n numbers of nodes
#         for pointer in range(n):
#             fast = fast.next

#         #incremen fast and slow by one in each iteration
#         while(fast.next):
#             fast = fast.next
#             slow = slow.next
        
#         return slow

#     else:
#         return 'List is empty'
    



# link_list = LinkedList()
# node_first = link_list.insert_first('grey')
# node_two = link_list.insert_first('purple')
# node_three = link_list.insert_first('orange')
# node_four = link_list.insert_first('red')
# node_five = link_list.insert_first('blue')
# node_six = link_list.insert_first('green')
# ans = from_last(link_list, 0).data
# print(ans)

