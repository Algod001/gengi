def minimax(position,depth,alpha,beta, minimizingPlayer):
    if depth == 0 or game over in positon:
        return evaluation process of position
    if minimizingPlayer:
        maxEval= -infinity
        for each child of position:
            eval = minimax(child, depth-1,alpha,beta,false)
            maxEval = max (maxEval.eval)
            alpha = max(alpha,eval)
            if beta<=alpha:
                break
        return maxEval
    
    else:
        miniEval = +infinity
        for each child of position:
            eval = minimax(child,depth-1,alpha,beta,time)
            miniEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval