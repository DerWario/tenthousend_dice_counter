import random


class Cup:

    def __init__(self, dice_count, sides):
        self.dice_count = dice_count
        self.sides = sides
        self.roll = []

    def re_roll(self):
        self.roll = []
        for i in range(self.dice_count):
            self.roll.append(random.randint(1, self.sides))
        self.roll.sort()
        return self.roll

    def has_multiple(self, same_count, strict=True):
        cnt = 0
        for i in range(1, self.sides + 1):
            if strict:
                if self.roll.count(i) == same_count:
                    cnt += 1
            else:
                if self.roll.count(i) >= same_count:
                    cnt += 1
        return cnt
