import random

ROCK = 0
PAPER = 1
SCISSORS = 2

seed = int(input())
random.seed(int(seed))

player1 = input()
player2 = input()

rounds = int(input())
while rounds < 1:
    print("Rounds must be > 0")
    rounds = int(input())

print(f"{player1} vs {player2} for {rounds} rounds")

# Initialize win counts
player1_wins = 0
player2_wins = 0
total_played_rounds = 0

while total_played_rounds < rounds:
    # Step 2: Generate random choices for both players
    p1_choice = random.randint(0, 2)
    p2_choice = random.randint(0, 2)

    # Check for tie
    if p1_choice == p2_choice:
        print("Tie")
        continue  # No need to check further, repeat this round without counting it

    if (p1_choice == ROCK and p2_choice == SCISSORS) or \
       (p1_choice == PAPER and p2_choice == ROCK) or \
       (p1_choice == SCISSORS and p2_choice == PAPER):
        player1_wins += 1
        winner = player1
        if p1_choice == ROCK:
            print(f"{winner} wins with rock")
        elif p1_choice == PAPER:
            print(f"{winner} wins with paper")
        else:
            print(f"{winner} wins with scissors")
    else:
        player2_wins += 1
        winner = player2
        if p2_choice == ROCK:
            print(f"{winner} wins with rock")
        elif p2_choice == PAPER:
            print(f"{winner} wins with paper")
        else:
            print(f"{winner} wins with scissors")

    # Count this round as a valid played round
    total_played_rounds += 1

print(f"{player1} wins {player1_wins} and {player2} wins {player2_wins}")
