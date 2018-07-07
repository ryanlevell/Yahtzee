from random import randint

"""Yahtzee Game"""

total_dice = [] 

one_dice = " ___\n|.  |\n|   |\n ---"
two_dice = " ___\n|.. |\n|   |\n ---"
three_dice = " ___\n|...|\n|   |\n ---"
four_dice = " ___\n|...|\n|.  |\n ---"
five_dice = " ___\n|...|\n|.. |\n ---"
six_dice = " ___\n|...|\n|...|\n ---"

for i in range(5):
	dice_face = randint(1,6)
	total_dice.append(dice_face)

print(total_dice)

one = 0
two = 0
three = 0
four = 0
five = 0

number_of_dice = 5	
for i in range(number_of_dice):
	if total_dice[i] == 1:
		print(one_dice)
		one = one + 1

for i in range(number_of_dice):
	if total_dice[i] == 2:
		print(two_dice)
		two = two + 1
		
for i in range(number_of_dice):
	if total_dice[i] == 3:
		print(three_dice)
		three = three + 1
		
for i in range(number_of_dice):
	if total_dice[i] == 4:
		print(four_dice)
		four = four + 1
		
for i in range(number_of_dice):
	if total_dice[i] == 5:
		print(five_dice)
		five = five + 1
		

print("\n  One | " + str(one))
print("  Two | " + str(two))
print("Three | " + str(three))
print(" Four | " + str(four))
print(" Five | " + str(five))


number_of_dice = input("How many dice do you want to re-roll? ")
for i in range(int(number_of_dice)):
	if total_dice[i] == 1:
		print(one_dice)
		one = one + 1
		
for i in range(int(number_of_dice)):
	if total_dice[i] == 2:
		print(two_dice)
		two = two + 1
		
for i in range(int(number_of_dice)):
	if total_dice[i] == 3:
		print(three_dice)
		three = three + 1
		
for i in range(int(number_of_dice)):
	if total_dice[i] == 4:
		print(four_dice)
		four = four + 1
		
for i in range(int(number_of_dice)):
	if total_dice[i] == 5:
		print(five_dice)
		five = five + 1
