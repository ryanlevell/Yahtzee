from random import randint

"""Yahtzee Game"""

#Dice animation function
total_dice = [] 
def dice(num):
	
	if num == 1:
		print(" ___\n|.  |\n|   |\n ---")
		
	if num == 2:
		print(" ___\n|.. |\n|   |\n ---")
		
	if num == 3:
		print(" ___\n|...|\n|   |\n ---")
		
	if num == 4:
		print(" ___\n|...|\n|.  |\n ---")
		
	if num == 5:
		print(" ___\n|...|\n|.. |\n ---")
		
	if num == 6:
		print(" ___\n|...|\n|...|\n ---")


for i in range(5):
	dice_face = randint(1,6)
	total_dice.append(dice_face)
	dice(dice_face)
print(total_dice)



one = 0
two = 0
three = 0
four = 0
five = 0

	
for i in range(5):
	if total_dice[i] == 1:
		one = one + 1
for i in range(5):
	if total_dice[i] == 2:
		two = two + 1
for i in range(5):
	if total_dice[i] == 3:
		three = three + 1
for i in range(5):
	if total_dice[i] == 4:
		four = four + 1
for i in range(5):
	if total_dice[i] == 5:
		five = five + 1
	
print("\n  One | " + str(one))
print("  Two | " + str(two))
print("Three | " + str(three))
print(" Four | " + str(four))
print(" Five | " + str(five))

def length_counter(dice_number):
	if dice_number >= 3:
		print("Do you want to keep all the dice with the number " + str(dice_number) + "? ")
	
length_counter(one)
length_counter(two)
length_counter(three)
length_counter(four)
length_counter(five)

re_roll = input("How many dice do you want to re-roll? ")
new_roll = []
for i in range(int(re_roll)):
	dice_face = randint(1,6)
	new_roll.append(dice_face)
	dice(dice_face)
print(new_roll)


	
