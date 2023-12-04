board = ['#', '#', '#', '#', '#', '#', '#', '#', '#']

def showBoard() :
  pos = 0
  for i in range(3):
    for j in range(3):
      print(board[pos], end = " ")
      pos = pos + 1
    print()

def Draw():
  cnt = 0
  for i in range(len(board)):
    if board[i] != '#':
      cnt = cnt  + 1

  return cnt == 9


def valid(pos):
  if pos < 1 or pos > 9:
    return False
  if(board[pos-1] == '#'):
     return True
  else:
    return False
def checkWin(player):
  chk = ''
  if player+1 == 1:
    chk = 'X'
  else :
    chk = 'O'

  # check row
  if board[0] == chk and board[1] == chk  and board[2] == chk:
    return True
  if board[3] == chk and board[4] == chk  and board[5] == chk:
    return True
  if board[6] == chk and board[7] == chk  and board[8] == chk:
    return True
  #check col
  if board[0] == chk and board[3] == chk  and board[6] == chk:
    return True
  if board[1] == chk and board[4] == chk  and board[7] == chk:
    return True
  if board[2] == chk and board[5] == chk  and board[8] == chk:
    return True
  #check diagonal
  if board[0] == chk and board[4] == chk  and board[8] == chk:
    return True
  if board[2] == chk and board[4] == chk  and board[6] == chk:
    return True

  return False



#Driver code
Player = 0
while(True) :
  showBoard()
  print(f"Player {Player + 1}  Turn")

  ch = int(input())
  if(valid(ch)):
    if(Player==0):
      board[ch - 1] = 'X'
    else :
      board[ch - 1] = 'O'


    if(checkWin(Player)):
      print(f"Player {Player+1} Win!")
      break
  else:
    print("Invalid Move!")
    continue

  #check for draw
  if(Draw()) :
    print("Match Draw!")
    break

  Player = Player^1



