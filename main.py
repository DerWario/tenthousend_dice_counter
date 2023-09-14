from Cup import Cup

THROWS = 100_000
DICE_COUNT = 6
DICE_SIDES = 6

cup = Cup(DICE_COUNT, DICE_SIDES)

multiples = [0, 0, 0, 0, 0, 0]
for i in range(THROWS):
    roll = cup.re_roll()
    this_trow_multiples = [0, 0, 0, 0, 0, 0]
    for n in range(DICE_SIDES - 1):
        if cup.has_multiple(n + 2):
            multiples[n] = multiples[n] + 1
            this_trow_multiples[n] = this_trow_multiples[n] + 1

print(f"Number of throws: {THROWS}")
print(f"Number of dice in cup: {DICE_COUNT}")
print(f"Number of sides on each dice: {DICE_SIDES}")
print("--------------------")
for i in range(DICE_SIDES - 1):
    print(f"Number of at least one pair of {i+2} multiples in a throw: {multiples[i]} chance: {multiples[i]/THROWS*100}%")
