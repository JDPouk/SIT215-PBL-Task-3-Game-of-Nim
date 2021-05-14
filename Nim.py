import random

# Initial values of Aplha and Beta
MIN = 0


# Returns optimal value for current player
# (Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:

        best = MIN

        # Recur for left and right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = MAX

        # Recur for left and
        # right children
        for i in range(0, 2):

            val = minimax(depth + 1, nodeIndex, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best


def game_setup():
    n = random.randrange(2, 6)
    print(n)
    pieces = 2 * n + 1
    Pile = {}
    for x in range(1, n + 1):
        Pile[x] = 1

    while sum(Pile.values()) < pieces:
        for x in range(1, n + 1):
            if sum(Pile.values()) < pieces:
                Pile[x] += 1

    return Pile
    print(Pile)


human = int(0)  # Initialize the number of times humans win the game
computer = int(0)
play_str = input("Would you like to play? (0=no, 1=yes) ")

while int(play_str) != 0:  # use while to determine if the game starts
    Pile = game_setup()

    print("Start _--_")
    for x in Pile.keys():
        print("Pile ", x, ":", Pile[x])

    while (Pile[1] > 0) or (Pile[2] > 0):  # use while to determine if the pile is empty.
        pile = int(input("Choose a pile: "))

        while Pile[pile] == 0:
            # If one of the piles is empty. No more stones can be removed from this pile.

            print("Pile must be 1 or 2 and non-empty. Please try again.")
            pile = int(input("Choose a pile: "))

        else:

            while (pile < 0) or (pile > len(Pile)):
                # If the number of the pile is not legal. Can't continue.

                print("Pile must be 1 or 2 and non-empty. Please try again.")
                pile = int(input("Choose a pile: "))

            else:
                stones = int(input("Choose stones to remove from pile: "))

                while (stones > 3) or (stones < 1):
                    # If the number of the stones is not beween 1 and 3. Can't continue.

                    print("Invalid number of stones. Please try again.")
                    stones = int(input("Choose stones to remove from pile: "))

                else:

                    print("Player -> ", end='')
                    print("Remove", stones, "stones from pile", pile)

                    # Next, use the ”if“ to divide the two cases.

                    # The first is when humans choose to use the Pile[1.
                    # Then the computer judges the Pile[2 first.
                    # If the Pile[2 is empty.
                    # Judging the Pile[1.
                    # Once who is the last stone.
                    # Who wins.

                    # The second is when humans choose to use the Pile[2.
                    # Then the computer judges the Pile[1 first.
                    # If the Pile[1 is empty.
                    # Judging the Pile[2.
                    # Once who is the last stone.
                    # Who wins.

                    if pile > -1:
                        # If it is Pile[1 and there are enough stones in the Pile[1.

                        Pile[pile] = Pile[pile] - stones
                        for x in Pile.keys():
                            print("Pile ", x, ":", Pile[x])

                        if all(value == 0 for value in Pile.values()):
                            # If the piles are taken empty.

                            human = human + 1  # Humans win the game plus one.
                            print("\nPlayer wins!")
                            print("Score -> human:", human, "; computer:", computer)

                        else:
                            # The stones was not taken by humans.

                            if (Pile[2] > 0):
                                # If the Pile[2 is not taken empty.
                                MAX = sum(Pile.values())
                                values = list(Pile.values())
                                list(filter(lambda num: num != 0, values))
                                amount = minimax(0, 0, True, values, MIN, MAX)
                                for x in Pile:
                                    if Pile[x] == amount:
                                        break

                                Pile[x] = Pile[x] - amount
                                print("Computer -> ", end='')
                                print("Remove", amount, "stones from pile", x)

                            else:
                                # If the Pile[2 is taken empty.
                                MAX = sum(Pile.values())
                                values = list(Pile.values())
                                list(filter(lambda num: num != 0, values))
                                amount = minimax(0, 0, True, values, MIN, MAX)
                                for x in Pile:
                                    if Pile[x] == amount:
                                        break

                                Pile[x] = Pile[x] - amount
                                print("Computer -> ", end='')
                                print("Remove", amount, "stones from pile", x)

                            if all(value == 0 for value in Pile.values()):
                                # The stones was taken empty by computer.

                                computer = computer + 1  # Computer win the game plus one.
                                print("\nComputer wins!")
                                print("Score -> human:", human, "; computer:", computer)

                    if (pile == 2) and (Pile[2] >= stones):
                        # If it is Pile[2 and there are enough stones in the Pile[2.

                        Pile[2] = Pile[2] - stones
                        for x in Pile.keys():
                            print("Pile ", x, ":", Pile[x])

                        if all(value == 0 for value in Pile.values()):
                            # If the piles are taken empty.

                            human = human + 1  # Humans win the game plus one.
                            print("\nPlayer wins!")
                            print("Score -> human:", human, "; computer:", computer)

                        else:
                            # The stones was not taken by humans.

                            if (Pile[1] > 0):
                                # If the Pile[1 is not taken empty.
                                MAX = sum(Pile.values())
                                values = list(Pile.values())
                                list(filter(lambda num: num != 0, values))
                                amount = minimax(0, 0, True, values, MIN, MAX)
                                for x in Pile:
                                    if Pile[x] == amount:
                                        break

                                Pile[x] = Pile[x] - amount
                                print("Computer -> ", end='')
                                print("Remove", amount, "stones from pile", x)

                            else:
                                # If the Pile[1 is taken empty.
                                MAX = sum(Pile.values())
                                values = list(Pile.values())
                                list(filter(lambda num: num != 0, values))
                                amount = minimax(0, 0, True, values, MIN, MAX)
                                for x in Pile:
                                    if Pile[x] == amount:
                                        break

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

    else:
        play_str = input("\nWould you like to play again? (0=no, 1=yes) ")
        # Judge whether to come again
