
example_input = [
    "A Y",
    "B X",
    "C Z",
]

# part one

# A X Rock 1
# B Y Paper 2
# C Z Scissors 3

# Win 6
# Draw 3
# Lose 0

score_map = {
    "A X": 4, # Rock Rock Draw
    "A Y": 8, # Rock Paper Win
    "A Z": 3, # Rock Scissors Lose
    "B X": 1, # Paper Rock Lose
    "B Y": 5, # Paper Paper Draw
    "B Z": 9, # Paper Scissors Win
    "C X": 7, # Scissors Rock Win
    "C Y": 2, # Scissors Paper Lose
    "C Z": 6  # Scissors Scissors Draw
}

from utils import load_input_as_list
input = load_input_as_list("inputs/two.txt")
scores_example = [score_map[i] for i in example_input]
scores = [score_map[i] for i in input]
print(f'Day 2 part 1 answer: {sum(scores)}')

# part two

# X lose
# Y draw
# Z win

response_map = {
    "A X": "A Z",   # Lose to Rock > Scissors
    "A Y": "A X",   # Draw to Rock > Rock
    "A Z": "A Y",   # Win against Rock > Paper
    "B X": "B X",   # Lose to Paper > Rock
    "B Y": "B Y",   # Draw to Paper > Paper
    "B Z": "B Z",   # Win against Paper > Scissors
    "C X": "C Y",   # Lose to Scissors > Paper
    "C Y": "C Z",   # Draw to Scissors > Scissors
    "C Z": "C X"    # Win against Scissors > Rock
}


part_two_scores = [score_map[response_map[i]] for i in input]
print(f'Day 2 part 2 answer: {sum(part_two_scores)}')



