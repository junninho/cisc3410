def printBoard(board):
  for i in range(8):
    for j in range(8):
      print(board[i][j], end = " ")
    print()

def isSafe(board, row, col):
  for i in range(col):
    if board[row][i] == 1:
      return False

  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  for i, j in zip(range(row, 8, 1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  return True

def findSafe(board, col):
  if col >= 8:
    return True

  for i in range(8):
    if isSafe(board, i, col):
      board[i][col] = 1

      if findSafe(board, col + 1) == True:
        return True

      board[i][col] = 0

  return False

def solve():
  board = [[0 for i in range(8)] for j in range(8)]

  if findSafe(board, 0) == False:
    print("No solution")
    return False

  printBoard(board)
  return True

def main():
  solve()

main()
