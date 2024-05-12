# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def print_LL(self):
#         if self.head is None:
#             print("Linked List is empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(n.data)
#                 n=n.ref

#     def add_begin(self,data):
#         newNode = Node(data)
#         newNode.ref = self.head
#         self.head = newNode
    
# LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.print_LL()

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,end=" ")
                n =n.ref


    def add_begin(self,data):
        new_Node = Node(data)
        new_Node.ref = self.head
        self.head = new_Node

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(5)
LL1.print_LL()