def verify(N,pos):
    #Checking and converting input to row and col
    if len(pos)<2:
        return False
    x=ord(pos[0])-97
    y=int(pos[1])-1
    if x<0 or x>=N or y<0 or y>=N:
        return False
    return True

def printboard(board):
    for i in board:
        print([" ".join(i)])

def solve(N,r,board,col,pos_diagonal,neg_diagonal,input_row):
    #Base condition
    if r==N:
        return True
    #Passing already filled row by the user
    if r==input_row:
        return solve(N,r+1,board,col,pos_diagonal,neg_diagonal,input_row)
    for c in range(N):
        #checking the position is safe to place the Queen
        if c in col or (r+c) in pos_diagonal or (r-c) in neg_diagonal:
            continue
        #adding constants into hassets for keeping track of Queens position
        col.add(c)
        pos_diagonal.add(r+c)
        neg_diagonal.add(r-c)
        board[r][c]="Q"
        if solve(N,r+1,board,col,pos_diagonal,neg_diagonal,input_row):
            return True
        #Reverting the change made before and removing the constants 
        board[r][c]="."
        col.remove(c)
        pos_diagonal.remove(r+c)
        neg_diagonal.remove(r-c)
    return False
    
def main():
    try:
       N=int(input("Enter size of the board(3<N<27):"))
    except ValueError:
       return print('Please enter an Integer for board size.')
    else:
       if N<4 or N>26:
           return print('board size Out of range.')

    pos=input("Enter position of your choice(e.g., a1, b2, c3):")
    if verify(N,pos):
        #Creating board of required size
        board=[["." for i in range(N)] for j in range(N)]
        col=set()
        pos_diagonal=set()
        neg_diagonal=set()
        input_row=ord(pos[0])-97
        input_col=int(pos[1])-1
        #placing Queen based on user input
        board[input_row][input_col]="Q"
        col.add(input_col)
        pos_diagonal.add(input_row+input_col)
        neg_diagonal.add(input_row-input_col)
        if solve(N,0,board,col,pos_diagonal,neg_diagonal,input_row):
            return printboard(board)
        return print("Not solvable.")
    else:
        l=chr(96+N)+str(N)
        return print("Please enter a valid position between a1 to",l)

if __name__ == '__main__':
    print("Welcome to NQueen puzzle!")
    main()