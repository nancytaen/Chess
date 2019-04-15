def GetPlayerPositions(board, player):
    occup = []
    if player == 10:
        for i in range (0,63,1):
            if board[i]<20 and board[i]>=10:
                occup += [i]
    if player == 20:
        for i in range (0,63,1):
            if board[i]>=20:
                occup += [i]
    return occup

def checkPlayer(board,position):
    pos = board[position]
    if pos <10 or pos >26:
        return 0
    if pos >=10 and pos <20:
        return 10
    if pos >=20:
        return 20
def isOpponent(board,position,player):
    if checkPlayer(board,position)==player:
        return False
    if checkPlayer(board,position)==0:
        return False
    else:
        return True

def checkCol(position):
    col = 0
    while True:
        position -= 8
        if position <0:
            break
        col += 1
    return col

def checkKFront(board, position, accum, player):
    if position+17<64:
        if board[position+17]==0 or isOpponent(board,position+17,player)==True:
            if checkCol(position+17) == checkCol(position)+2:
                accum += [position+17]
    if position+15<64:
        if board[position+15]==0 or isOpponent(board,position+15,player)==True:
            if checkCol(position+15) == checkCol(position)+2:
                accum +=[position+15]
    return accum

def checkKBack(board,position,accum, player):
    if position-17 >=0:
        if board[position-17]==0 or isOpponent(board,position-17,player)==True:
            if checkCol(position-17)== checkCol(position)-2:
                accum += [position-17]
    if position-15 >=0:
        if board[position-15]==0 or isOpponent(board,position-15,player)==True:
            if checkCol(position-15) == checkCol(position)-2:
                accum +=[position-15]
    return accum

def checkBishop(board,pos,accum,player):
    nr = pos % 8
    nl = 7 - (pos % 8)
    ul = pos
    ul = pos
    ll = pos
    ur = pos
    lr = pos
    for i in range(0,nr,1):
       ur += 7
       lr -= 9
       if lr>=0 and lr<64:
          if board[lr] == 0:
             accum+=[lr]
          else:
             if isOpponent(board,lr,player)==True:
                accum += [lr]
             break
       if ur>=0 and ur<64:
          if board[ur]==0:
             accum +=[ur]
          else:
             if isOpponent(board,ur,player)==True:
                accum += [ur]
             break

    for i in range(0,nl,1):
       ul += 9
       ll -= 7
       if ul>=0 and ul<64:
          if board[ul]==0:
             accum +=[ul]
          else:
             if isOpponent(board,ul,player)==True:
                accum +=[ul]
             break

       if ll>=0 and ll<64:
          if board[ll]==0:
             accum +=[ll]
          else:
             if isOpponent(board,ll,player)==True:
                accum += [ll]
             break

    return accum

def checkSides(board,position,accum,player):
    i=1
    while position+8*i < 64:
     if board[position+8*i]!=0:
         if isOpponent(board,position+8*i, player)==True:
             accum += [position+8*i]
         break
     accum += [position+8*i]
     i = i+1
    i =1
    while True:
     if position-8*i<=0:
         break
     if board[position-8*i]!=0:
         if isOpponent(board,position-8*i, player)==True:
             accum += [position-8*i]
         break
     accum += [position-8*i]
     i = i+1
    i=1

    while checkCol(position+i)==checkCol(position):
       if position+i > 63:
           break
       if board[position+i]!=0:
           if isOpponent(board,position+i, player)==True:
               accum += [position+i]
           break
       accum += [position+i]
       i=i+1
    i=1
    while checkCol(position-i)==checkCol(position):
       if position-i <0:
           break
       if board[position-i]!=0:
           if isOpponent(board,position-i, player)==True:
               accum += [position-i]
           break
       accum+=[position-i]
       i=i+1
    return accum

def GetPieceLegalMoves(board,position):
   pos = board[position]
   player = checkPlayer(board,position)
   piece = pos - player
   accum = []
   if piece == 0:
       if player == 10:
           if board[(position+8)]==0:
               accum += [position+8]
           if isOpponent(board, position+9,10)==True:
               if checkCol(position+9) == checkCol(position)+1:
                   accum += [position+9]
           if isOpponent(board,position+7,10)==True:
               if checkCol(position+7) == checkCol(position)+1:
                   accum += [position+7]
           return accum
       elif player == 20:
           if board[(position-8)]==0:
               accum += [position-8]
           if isOpponent(board, position-9,20)==True:
               if checkCol(position-9) == checkCol(position)-1:
                   accum += [position-9]
           if isOpponent(board,position-7,20)==True:
               if checkCol(position-7) == checkCol(position)-1:
                   accum += [position-7]
           return accum
   elif piece == 1:
       if position < 48:
           accum = checkKFront(board,position,accum,player)
       if position >= 16:
           accum = checkKBack(board,position,accum,player)
       return accum
   elif piece == 2:
       accum = checkBishop(board,position,accum,player)
       return accum
   elif piece == 3:
       return checkSides(board,position,accum,player)
   elif piece == 4:
       accum = checkBishop(board,position,accum,player)
       accum =checkSides(board,position,accum,player)
       return accum
   elif piece == 5:
       for i in range (-1,2,1):
           if position+8+i<64:
               if board[(position+8+i)] == 0 or isOpponent(board, position+8+i,player)==True:
                   accum += [position+8+i]
           if position-8+i>=0:
               if board[(position-8+i)] == 0 or isOpponent(board, position-8+i,player)==True:
                   accum += [position-8+i]
       return accum

def IsPositionUnderThreat(board, position, player):
   if player == 10:
       opponent  = 20
   else:
       opponent = 10
   accum = GetPlayerPositions(board,opponent)
   for i in accum:
       moves = GetPieceLegalMoves(board,i)
       if position in moves:
           return True
   return False

def getPiece(name):
  if name=="pawn":
     return 0
  elif name=="knight":
     return 1
  elif name=="bishop":
     return 2
  elif name=="rook":
     return 3
  elif name=="queen":
     return 4
  elif name=="king":
     return 5
  else:
     return -1

def genBoard():
  r=[0]*64
  White=10
  Black=20
  for i in [ White, Black ]:
    if i==White:
        factor=+1
        shift=0
    else:
        factor=-1
        shift=63

    r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
    r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
    r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
    if i==White:
        r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
        r[shift+factor*3] = i+getPiece("king")
    else:
        r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
        r[shift+factor*4] = i+getPiece("king")

    for j in range(0,8):
        r[shift+factor*(j+8)] = i+getPiece("pawn")
        for j in range(0,8):
            r[shift+factor*(j+8)] = i+getPiece("pawn")
    return r

def printBoard(board):
      accum="---- BLACK SIDE ----\n"
      max=63
      for j in range(0,8,1):
         for i in range(max-j*8,max-j*8-8,-1):
            accum=accum+'{0: <5}'.format(board[i])
         accum=accum+"\n"
      accum=accum+"---- WHITE SIDE ----"
      return accum
