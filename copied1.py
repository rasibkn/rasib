Roll_dice():
    return random.randint(1,6)

def Move(Player, value, P1N, P2N, P3N, P4N):
    snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
    ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
    Throw = Roll_dice()
    if Player == 1:
        num = value + Throw
        print(P1N, "Rolled a", Throw, "And is now on", num)
    if Player == 2:
        num = value + Throw
        print(P2N, "Rolled a", Throw, "And is now on", num)
    if Player == 3:
        num = value + Throw
    print(P3N, "Rolled a", Throw, "And is now on", num)
