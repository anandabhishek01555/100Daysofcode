class node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class Llist():
    def __init__(self):
        self.head=None

    def create(self,list1):
        self.head=node(list1[0])
        del(list1[0])
        while(len(list1)>0):
            tmp=node(list1[0])
            tmp.next=self.head
            self.head=tmp
            del(list1[0])

    def display(self):
        tmp=self.head
        while(tmp!=None):
            print(tmp.data,end="->")
            tmp=tmp.next

l=Llist()
l1=[i for i in input("Enter list of elements : ").split()]
l.create(l1)
l.display()