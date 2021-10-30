def declareWinner(piles,chance): #checked after turn is incremented.
    if max(piles) == 0: #game over
        if chance % 2 == 0: 
            print("You Win!")
            return 1
        else:
            print("Computer Wins!")
            return 2
    else:
        return 0



def simulateWin(piles,chance):
    if max(piles) == 0: #game over
        if chance == "Computer":
            return -1
        elif chance == "Player":
            return 1
    else:
        return 0
            
  
def simulateComputer(piles): #maximise score
    score = simulateWin(piles,"Computer")
    if score != 0:
        return score
    bestScore = -9999
    n = piles[0]
    m = piles[1]
    for i in range(1,n+1): #pile1
        piles[0] -= i
        currentScore = simulatePlayer(piles) #simulating corresponding Player move
        piles[0] += i
        bestScore = max(bestScore,currentScore)
        
    for i in range(1,m+1): #pile2
        piles[1] -= i
        currentScore = simulatePlayer(piles) #simulating corresponding Player move
        piles[1] += i
        bestScore = max(bestScore,currentScore)
    
    return bestScore



def simulatePlayer(piles): #minimise score
    score = simulateWin(piles,"Player")
    if score != 0:
        return score
    bestScore = 9999
    n = piles[0]
    m = piles[1]
    for i in range(1,n+1): #pile1
        piles[0] -= i
        currentScore = simulateComputer(piles) #simulating corresponding computer move
        piles[0] += i
        bestScore = min(bestScore,currentScore)
        
    for i in range(1,m+1): #pile2
        piles[1] -= i
        currentScore = simulateComputer(piles) #simulating corresponding computer move
        piles[1] += i
        bestScore = min(bestScore,currentScore)
    
    return bestScore




def computerTurn(piles):
    bestScore = -9999
    computerMove = [0,0]
    n = piles[0]
    m = piles[1]
    for i in range(1,n+1): #pile1
        piles[0] -= i
        currentScore = simulatePlayer(piles) #simulating player moves
        piles[0] += i
        if currentScore > bestScore:
            bestScore = currentScore
            computerMove[0] = i 
    for i in range(1,m+1): #pile2
        piles[1] -= i
        currentScore = simulatePlayer(piles) #simulating player moves
        piles[1] += i
        if currentScore > bestScore:
            bestScore = currentScore
            computerMove[1] = i
            computerMove[0] = 0
    piles[0] -= computerMove[0]
    piles[1] -= computerMove[1]
    if(computerMove[0] != 0):
        move = "Removing " + str(computerMove[0]) + " stones from Pile 1"
        return move
    else:
        move = "Removing " + str(computerMove[1]) + " stones from Pile 2"
        return move
    
    
def main():
    piles=[]
    piles.append(int(input("Enter the no. of stones in Pile1: ")))
    piles.append(int(input("Enter the no. of stones in Pile2: ")))
    computerMoves = []
    playerMoves = []
    chance = 1
    print("Initial Status of Piles ==> Pile1 : " + str(piles[0]) + "; Pile2 : " + str(piles[1]))
    while True:
        winner = declareWinner(piles,chance)
        if winner != 0:
            if winner == 1:
                print(playerMoves)
                break
            elif winner == 2:
                print(computerMoves)
                break
        if chance % 2 == 0:
            print("Computer Playing...")
            computerMoves.append(computerTurn(piles))
            chance += 1
        else:
            print("Your Turn...")
            pile = int(input("Seclect the pile: 1 or 2: "))
            stones = int(input("Number of Stones: "))
            piles[pile-1] -= stones
            chance += 1
            playerMoves.append("Removing " + str(stones) + " stones from Pile " + str(pile))
        print("Current Status of Piles ==> Pile1: " + str(piles[0]) + "; Pile2 : " + str(piles[1]))
                
                
                
main()
                
            
        