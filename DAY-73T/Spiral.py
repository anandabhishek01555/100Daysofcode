#Spiral Traversal

def Print(row, col, myArr): 
    count = 0
    c1 = 0
    while count < row and c1 < col: 
        for i in range(c1, col): 
            print(myArr[count][i], end=" ")             
        count += 1
        for i in range(count, row): 
            print(myArr[i][col - 1],end=" ")               
        col -= 1

        if count < col:          
            for i in range(col - 1, (c1 - 1), -1): 
                print(myArr[row - 1][i],end=" ")              
            row -= 1

        if (c1 < col) : 
            for i in range(row - 1, count - 1, -1) : 
                print(myArr[i][c1],end=" ") 
              
            c1 += 1

myArr = [ [1, 2, 3], 
      [7, 8, 9], 
      [13, 14, 15] ] 
        
row = 3; col = 6
Print(row, col, myArr) 