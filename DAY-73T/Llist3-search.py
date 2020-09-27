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
            
    def search(self,key):
        if self.head==None:
            print("List is Empty")
        else:
            pos=1
            tmp=self.head
            while tmp.data!=key and tmp.next!=None :
                tmp=tmp.next
                pos+=1
            if tmp.data==key:
                print("Element Found at",pos)
            else:
                print("Element is not present in the list")
                
    def display(self):
        tmp=self.head
        while(tmp!=None):
            print(tmp.data,end="->")
            tmp=tmp.next
            
l=Llist()
l.create([1,2,3,4,5])
l.display()
print()
ele=int(input("Enter an element to search : "))
l.search(ele)
l.display()
    