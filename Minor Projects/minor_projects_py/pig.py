import random

#generating random roll

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


# asking players to be in m=between 2-4 if they are they will move if not invalid
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

print(players)

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

        # ✅ Stop the game if a player reaches max_score
        if player_scores[player_idx] >= max_score:
            winning_idx = player_idx
            print("\n🎉 Player", winning_idx + 1, "wins with a score of:", player_scores[winning_idx])
            exit()  # This stops the program immediately


max_score = max(player_scores)
winning_idx = player_scores.index(max(player_scores))
print("Player number", winning_idx + 1, "is the winner with a score of:", player_scores[winning_idx])
