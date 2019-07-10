board = [
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]]
def is_targeted(board,N,x,y):
  for i in range(N):
    for j in range(N):
      if board[i][j]!=0:
        if x==i or y ==j:
          return True
        if (x-i)+(y-j)==0:
          return True
        if (x+j)-(y+i)==0:
          return True
  return False
#N=len(board)
def NQueens(board,N):
  if N==0:
    print(board)
    return True 
  for i in range(len(board)):
    for j in range(len(board)):
      if is_targeted(board,len(board),i,j)==False:
        board[i][j]=1
        if NQueens(board,N-1)==True:
          return True 
        board[i][j]=0
        #N-=1
  #print(board,N)
  return False

print(NQueens(board,N=len(board)))