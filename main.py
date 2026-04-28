from roll import roll_dice
from display import show_result  
print("==== Dice roll simulator =====")

while True:
    user = input("\n press Enter to roll dice or type 'exit' to quit:")

    if user.lower()== "exit":
        print("Thanks for playing !")
        break
    print("Rolling intzaar karo ...")
    dice = roll_dice()
    show_result(dice)

