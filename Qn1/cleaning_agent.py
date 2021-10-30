import random


def suck(environment, position):
    if environment[position] == 0: #dirty
        environment[position] = 1  #cleaned the position
    return environment


def move(position):
    next = random.randint(0,1) #selecting random direction to move
    if next == 0:
        print("Action: Left")
    else:
        print("Action: Right")
    if position == next:
        print("Bot is already here!")
    return next
    
    
def encode(environment, position): #encoding current state
    agent = ""
    if position == 0:
        agent = "A"
    else:
        agent = "B"
    state = "A=" + str(environment[0]) + ";B=" + str(environment[1]) + ";Agent@" + agent
    return state
    
    
def main():
    print("CELL Value: 0 ==> DIRTY")
    print("CELL Value: 1 ==> CLEAN")
    print("Agent Position 0 ==> Agent at CELL A")
    print("Agent Position 1 ==> Agent at CELL B")
    print("A=0;B=1;Agent@A ==> Agent is at postion A, with cell A DIRTY and cell B CLEAN\n")
    #implementing all possible scenarios
    environment = [0,0]
    for startposition in range(2):
        for A in range(2):
            for B in range(2):
                steps = 0
                environment[0] = A
                environment[1] = B
                score = 0
                position = startposition
                print("----------Initial State of Environment --> " + str(environment) + " ; Initial Position of agent --> " + str(position)+ "----------")
                history = [] 
                current_state = encode(environment,position)
                history.append(current_state)
                while steps < 1000: #1000 lifetime steps
                    if environment[position] == 0: #dirty
                        environment = suck(environment,position)
                        score += 1
                        print("Action: Suck")
                        print("Current State of Environment: " + str(environment) + " ; Current Position of agent --> " + str(position) + " ; Performance score: " + str(score))
                        
                    else: #clean
                        position = move(position)
                        print("Current State of Environment: " + str(environment) + " ; Current Position of agent --> " + str(position) + " ; Performance score: " + str(score))
                    steps += 1
                    current_state = encode(environment,position)
                    history.append(current_state)
                print("\n---STATE SPACE GRAPH-----")
                for node in history:
                    print(" ===> " + str(node), end="")
                print("\n")
        
main()