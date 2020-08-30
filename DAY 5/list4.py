#Program to count the frequency of each elements in list

a=[1,2,3,4,5,6,1,2,3,4,5,6,1,2]
l=[]
m=[]
for i in range(len(a)):
    if a[i] not in m:
        m.append(a[i])
for i in range(len(m)):
    print(a.count(m[i]),end=" ")   



# l=[1,2,3,4,5,1,2,3,1]
# k=[None]*len(l)
# visited=-1
# for i in range(0,len(l)):
#     c=1
#     for j in range(i+1,len(l)):
#         if(l[i]==l[j]):
#             c+=1
#             k[j]=visited
#     if(k[i]!=visited):
#         k[i]=c

  
# for i in range(0, len(k)):    
#     if(k[i] != visited):    
#         print(str(k[i]),end=" ");
       
    
  

