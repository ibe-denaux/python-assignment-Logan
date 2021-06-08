'''
The Zebra Puzzle
1. There are five houses.
2. The Englishman lives in the red house.
3. The Spaniard owns the dog.
4. Coffee is drunk in the green house.
5. The Ukrainian drinks tea.
6. The green house is immediately to the right of the ivory house.
7. The Old Gold smoker owns snails.
8. Kools are smoked in the yellow house.
9. Milk is drunk in the middle house.
10. The Norwegian lives in the first house.
11. The man who smokes Chesterfields lives in the house next to the man with the fox.
12. Kools are smoked in the house next to the house where the horse is kept.
13. The Lucky Strike smoker drinks orange juice.
14. The Japanese smokes Parliaments.
15. The Norwegian lives next to the blue house.

Each of the five houses is painted a different color, and their
inhabitants are of different national extractions, own different pets,
drink different beverages and smoke different brands of cigarettes.

Which of the residents drinks water?
Who owns the zebra?
'''

import itertools
# If x is to the right of y, it means the difference between x and y is 1
def right_to(x_right, y_left):
    return x_right-y_left == 1

# If x is next to y (either to the left or right of it), the difference should be 1 or -1
def next_to(x, y):
    return abs(x-y) == 1

def zebra_puzzle():
    # Returns the number of the houses where water is drunk and where the zebra is.
    # There are 5 house. We also define which houses are the "first" and "middle" ones.
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]

    # We create a list with all possible combinations of houses = 5! = 120
    orderings = list(itertools.permutations(houses))
    # It will return a tuple with the number of the houses where water is drunk and where the zebra is.
    answers = next((water, zebra)
                # 5 colors and their conditions
                for (yellow, blue, red, ivory, green) in orderings
                if right_to(green, ivory)
                # 5 nationalities and their conditions
                for (Norwegian, English, Japanese, Spanish, Ukrainian) in orderings
                if Norwegian == first
                if English == red
                if next_to(Norwegian, blue)
                # 5 drinks and their conditions
                for (tea, coffee, orangejuice, milk, water) in orderings
                if coffee == green
                if Ukrainian == tea
                if milk == middle
                # 5 brands of cigarettes and their conditions
                for (Kools, Chesterfield, Old_Gold, Luckystrike, Parliaments) in orderings
                if Kools == yellow
                if Luckystrike == orangejuice
                if Japanese == Parliaments
                # 5 animals and their conditions
                for (dog, fox, snails, horse, zebra) in orderings
                if Spanish == dog
                if Old_Gold == snails
                if next_to(Kools, horse)
                if next_to(Chesterfield, fox)
                )
    return answers
