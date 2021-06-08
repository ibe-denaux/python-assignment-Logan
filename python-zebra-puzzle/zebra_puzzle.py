import itertools

# If x is right to y, the difference is 1
def right_to(x_right, y_left):
    return x_right-y_left == 1

# If x is next to y (either to the left or right of it), the difference should be 1 or -1
def next_to(x, y):
    return abs(x-y) == 1

def solution():
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))

    answers = next([{English: "English", Spanish: "Spanish", Ukranian: "Ukranian", Japanese: "Japanese", Norwegian: "Norwegian"}[x] for x in (water, zebra)]
                  for (red, green, ivory, yellow, blue) in orderings
                  if right_to(green, ivory)

                  for (English, Spanish, Ukranian, Japanese, Norwegian) in orderings
                  if English == red
                  if Norwegian == first
                  if next_to(Norwegian, blue)

                  for (coffee, tea, milk, orangejuice, water) in orderings
                  if coffee == green
                  if Ukranian == tea
                  if milk == middle

                  for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                  if Kools == yellow
                  if LuckyStrike == orangejuice
                  if Japanese == Parliaments

                  for (dog, snails, fox, horse, zebra) in orderings
                  if Spanish == dog
                  if OldGold == snails
                  if next_to(Chesterfields, fox)
                  if next_to(Kools, horse)
                  )

    return ("It is the {} who drinks the water.\n"
                "The {} keeps the zebra.").format(*answers)

print(solution())
