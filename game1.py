def fguesser(resp):
	if not hasattr(fguesser, "left"):
		fguesser.left = 2
		fguesser.right = 10
	else: 
		if resp == "l" or resp == "L":
			fguesser.right = fguesser.mid - 1
		else:
			fguesser.left = fguesser.mid + 1 
	
	fguesser.mid = (fguesser.left + fguesser.right) // 2
	return fguesser.mid



# Step 1   - printing for display
print("G U E S S I N G    G A M E")
print("--------------------------")
print("Please think of a number (between 1 and 10) ")

# Step 2  - interactivity, getting input from user
input("Press enter when you are ready!...")

# Step 3 - conditionals
guess = 1#_
count = 1#_
print ("Is it", guess, "?")
resp= input("Is it correct? (Higher/H, Lower/L or yes) ")
if resp in ['yes', 'Yes', 'Y', 'y']:
	print("Number in", count, "tries!")


# Step 4 and Step 5 - Loops and functions 
while resp not in ['yes', 'Yes', 'Y', 'y']:
	count=count+1
	# Function
	guess = fguesser(resp)
	print ("Is it", guess, "?")
	resp = input("Is it correct? (H, L or yes) ")
	if resp in ['yes', 'Yes', 'Y', 'y']:
		print("Number of tries:", count)
		break

print("Thank you for playing!")