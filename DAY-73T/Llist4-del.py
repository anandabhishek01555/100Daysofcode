class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class Llist:
    def __init__(self):
        self.head=None
        
    def create(self,list1):
        for i in range(len(list1)):
            tmp=node(list1[i])
            tmp.next=self.head
            self.head=tmp
    
    def delb(self):
        if self.head==None:
            print("Empty List")
        else:
            tmp=self.head
            self.head=self.head.next
            del(tmp)
            print("List after deletion from begining: ")
            
    def dele(self):
        if self.head.next==None:
            del(self.head)
            self.head=None
            print("List after deletion from end: ")
        else:
            curr=self.head
            prev=self.head
            while curr.next!=None:
                prev=curr
                curr=curr.next
            prev.next=None
            del(curr)
            print("List after deletion from end: ")
            
            
    def delkey(self,key):
        if self.head.data==key:
            tmp=self.head
            self.head=self.head.next
            del(tmp)
            print("List after deletion of node:",key)
        else:
            curr=self.head
            prev=self.head
            while(curr.data!=key and curr.next!=None):
                prev=curr
                curr=curr.next
            if curr.data==key:
                prev.next=curr.next
                del(curr)
                print("List after deletion of node",key)
            
    def display(self):
        tmp=self.head
        while(tmp!=None):
            print(tmp.data,end="->")
            tmp=tmp.next
            
l=Llist()
list1=list(map(int,input("Enter the elements of the list :").split()))
l.create(list1)
l.display()
print()
l.delb()
l.display()
print()
l.dele()
l.display()
print()
l.delkey(int(input("Enter the node you want to delete :")))
l.display()