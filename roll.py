import time
def roll_dice():
    dice = int(time.time()*1000) % 6 + 1
    return dice