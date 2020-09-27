# Program to create a linked list.


# Node Structure

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

# Entering node values

n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)

# Creating links between the nodes

head=n1
n1.next=n2
n2.next=n3
n3.next=n4

# Displaying Linked List

tmp=head
while(tmp!=None):
    print(tmp.data,end="->")
    tmp=tmp.next