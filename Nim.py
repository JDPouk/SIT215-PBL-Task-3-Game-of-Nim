import random

# Initial values of Beta, Alpha is set the the number of stones in all the piles
MIN = 0


# Returns optimal value for current player
# (Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]
    # checks to see if its the max player's turn
    if maximizingPlayer:

        best = MIN

        # Recur for left and right children
        for i in range(0, 2):
            # uses recursion to traverse to depth 3
            val = minimax(depth + 1, nodeIndex, False, values, alpha, beta)
            # updates the best value by comparing to to the aplha
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        # the function ends and returns the chosen value
        return best
    # if
    else:
        # begins finding the value for the min player
        best = MAX

        # Recur for left and
        # right children
        for i in range(0, 2):
            # uses recursion to traverse to depth 3
            val = minimax(depth + 1, nodeIndex, True, values, alpha, beta)
            # updates the best value by comparing to to the beta
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break
        # the function ends and returns the chosen value
        return best

# sets up the game by creating the piles
def game_setup():
    # piles are between 2-5
    n = random.randrange(2, 6)
    # pieces are calculated by n which is the number of piles
    pieces = 2 * n + 1
    Pile = {}
    for x in range(1, n + 1):
        Pile[x] = 1

    # distributes the pieces as evenly as possible
    while sum(Pile.values()) < pieces:
        for x in range(1, n + 1):
            if sum(Pile.values()) < pieces:
                Pile[x] += 1
    # returns a dictionary of piles filled with pieces
    return Pile



human = int(0)  # Initialize the number of times humans win the game
computer = int(0) # Initialize the number of times computer/AI win the game
play_str = input("Would you like to play? (0=no, 1=yes) ")

while int(play_str) != 0:  # use while to determine if the game starts

    Pile = game_setup()
    # determines whether the game loop continues
    game = True
    # displays a list of the keys and value which are the piles and pieces
    print("Start _--_")
    for x in Pile.keys():
        print("Pile ", x, ":", Pile[x])

    while game:  # use while to determine if the pile is empty.

        pile = int(input("Choose a pile: "))
        while pile < 1 or pile > len(Pile):
            print("Sorry, the pile must exist.")
            pile = int(input("Choose a pile: "))

        stones = int(input("Choose stones to remove from pile: "))
        while stones < 1 or stones > max(Pile.values()):
            print("Sorry, you can only remove stones that are in a pile.")
            stones = int(input("Choose stones to remove from pile: "))
        # player removes stone from a pile
        Pile[pile] = Pile[pile] - stones
        print("Player -> ", end='')
        print("Remove", stones, "stones from pile", pile)
        for x in Pile.keys():
            print("Pile ", x, ":", Pile[x])


        if all(value == 0 for value in Pile.values()):
            human = human + 1  # Humans win the game plus one.
            print("\nPlayer wins!")
            print("Score -> human:", human, "; computer:", computer)
            # determines whether1 the game loop continues
            game = False
            break

        # Alpha-Beta pruning algorithm begins
        # The MAX is the total number of stones remaining
        MAX = sum(Pile.values())
        values = list(Pile.values())
        # removes 0 from the list of values, you must take aleast 1 stone
        values[:] = (x for x in values if x != 0)
        # algorithm returns the best number of stones to remove
        amount = minimax(0, 0, True, values, MIN, MAX)
        for x in Pile:
            if Pile[x] == amount:
                break

        # AI removes stone from a pile
        Pile[x] = Pile[x] - amount
        print("Computer -> ", end='')
        print("Remove", amount, "stones from pile", x)
        for x in Pile.keys():
            print("Pile ", x, ":", Pile[x])

        if all(value == 0 for value in Pile.values()):
            # The stones was taken empty by computer.

            computer = computer + 1  # Computer win the game plus one.
            print("\nComputer wins!")
            print("Score -> human:", human, "; computer:", computer)
            # determines whether the game loop continues
            game = False

    play_str = input("\nWould you like to play again? (0=no, 1=yes) ")
        # Judge whether to come again
