from chessPlayer_chess import*
from queue import*
from chessPlayer_tree import*

def chessPlayer(board,player):
    pos = GetPlayerPositions(board,player)
    if pos==[]:
        status = False
    elif player+5 not in pos:
        status = False
    else:
        status = True
    eTree=(evalTree(board,player))[0]
    evalT = eTree.Get_LevelOrder()
    num = eTree.CountSuccessors()
    candidateMoves = (evalTree(board,player))[1]
    score = minimax(eTree, 2, -100000,100000,True)
    mins = candidateMoves[0][1]
    move = candidateMoves[0][0]
    for i in range (len(candidateMoves)):
        if candidateMoves[i][1]<mins:
            mins = candidateMoves[i][1]
            move = candidateMoves[i][0]

    print(move)
    return [status,move,candidateMoves, evalT]

def evalTree(board, player):
    evalTree = Tree(evaluateBoard(board))
    moves = GetPlayerPositions(board,player)
    cmoveslist = []
    for i in moves:
        accum = GetPieceLegalMoves(board,i)
        for j in accum:
            cmoves = []
            xboard=list(board)
            evals = 0
            cmoves = [i,j]
            xboard[j]=xboard[i]
            xboard[i]=0
            evals = evaluateBoard(xboard)
            subtree = Tree(evals)
            evalTree.AddSuccessor(subtree)
            xmoves = GetPlayerPositions(xboard, player)
            for k in xmoves:
                xaccum = GetPieceLegalMoves(xboard,k)
                for q in accum:
                    yboard=list(xboard)
                    xeval = 0
                    yboard[k]=yboard[q]
                    yboard[k]=0
                    xeval = evaluateBoard(yboard)
                    xtree = Tree(xeval)
                    subtree.AddSuccessor(xtree)
            cmoveslist+=[[cmoves,evals]]
    return evalTree, cmoveslist

def maxi(maxEval,evals):
    if maxEval<evals:
        return evals
    else:
        return maxEval
        def mini(minEval,evals):
            if minEval<evals:
                return minEval
            else:
                return evals

def minimax(root,depth,alpha,beta,player):
    if depth == 0:
        print("root is:", root.store[0])
        return root.store[0]
    if player:
        maxEval = -1000000
        children = root.GetSuccessors()
        for i in children:
            evals = minimax(i,depth-1,alpha,beta,False)
            maxEval = maxi(maxEval,evals)
            alpha = maxi(alpha,evals)
            if beta<=alpha:
                break
        print("maxeval is:", maxEval)
        return maxEval
    else:
        minEval = +1000000
        children = root.GetSuccessors()
        for i in children:
            evals = minimax(i,depth-1,alpha,beta,True)
            minEval = mini(minEval,evals)
            print("eval is", evals)
            print("mineval is", minEval)
            beta=mini(beta,evals)
            if beta<=alpha:
                break
        print("mineval is: ", minEval)
        return minEval

def evaluateBoard(board):
    evals = 0
    for i in board:
        if i == 10:
            evals +=10
        elif i == 11:
            evals +=30
        elif i == 12:
            evals +=30
        elif i == 13:
            evals += 50
        elif i == 14:
            evals += 90
        elif i == 15:
            evals += 900
        elif i == 20:
            evals -= 20
        elif i == 21:
            evals -=30
        elif i == 22:
            evals -=30
        elif i == 23:
            evals -= 50
        elif i == 24:
            evals -= 90
        elif i == 25:
            evals -= 900
    return float(evals)
