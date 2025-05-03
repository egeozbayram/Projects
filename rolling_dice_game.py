import random

choice = input("Do you want to roll the dice? (yes/no): ").lower()
while True:
    if choice == "yes":
      dice1 = random.randint(1, 6)
      dice2 = random.randint(1, 6)

      print (f"Dice 1: {dice1}")
      print (f"Dice 2: {dice2}")
      break

    elif choice == "no":
      print("Goodbye!")
      break

    else:
      print("Invalid input. Please enter 'yes' or 'no'.")

if dice1 == dice2:
   print("Nobody wins")

elif dice1 > dice2:
    print("Player 1 wins")

else:
    print("Player 2 wins")