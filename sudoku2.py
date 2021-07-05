M  = 9
def puzzle(a):
    for i in range(M):  
        for  j in range(M):            
                print(a[i][j],end=" | ")
        print()
def solve(borad,row,col,num):
    for i in range(9):
        if borad[row][i] == num:
            return False

    for i in range(9):
        if borad[i][col] == num:
            return False
    
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if borad[i+startRow][j+startCol] == num:
                return False
    return True

def sudoku(borad,row,col):
    if(row == M - 1 and col == M):
        return True
    
    if col == M:
        row += 1
        col = 0
    if  borad[row][col] > 0 :
            return sudoku(borad,row,col+1)
    for num in range(1,M+1,1):

        if solve(borad,row,col,num):
            borad[row][col] = num
            if sudoku(borad,row,col+1):
                return True
        borad[row][col] = 0
    return False
borad = [   
    [7,0,0,3,0,4,0,0,9],
    [1,0,0,8,0,6,0,0,0],
    [0,0,0,0,9,0,0,1,8],
    [8,3,0,0,0,0,0,4,0],
    [0,0,9,0,0,0,3,0,1],
    [5,1,0,0,0,0,0,8,2],
    [0,0,0,0,5,0,0,0,0],
    [0,0,5,1,0,3,0,0,0],
    [9,0,3,7,0,8,0,5,4]
]
if sudoku(borad,0,0):
    puzzle(borad)
else: 
    print(None)
