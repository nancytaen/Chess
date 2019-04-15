from chessPlayer_chess import*
from chessPlayer import*

board=genBoard()

done=False
while not(done):
    print (printBoard(board))
    while True:
        wmovef = int(input("What's your move? "))
        if GetPieceLegalMoves(board,wmovef)!=[] and  wmovef in GetPlayerPositions(board, 10):
            while True:
                print(GetPieceLegalMoves(board,wmovef))
                wmovet = int(input("where do you want to move to? "))
                if wmovet in GetPieceLegalMoves(board,wmovef):
                    break
            break
    board[wmovet]=board[wmovef]
    board[wmovef] = 0
    print(printBoard(board))
    move = chessPlayer(board,20)[1]
    bmovef = move[0]
    bmovet = move[1]
    board[bmovet]=board[bmovef]
    board[bmovef] = 0
    print(printBoard(board))
