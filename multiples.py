getmultiplier = raw_input("Pick a number between 2 and 9:")
multiplier = int(getmultiplier)

def multiples(num_times = multiplier):
	for num in range(1,51): #Define the range
		if num%num_times == 0:
			print "Can't touch this."
		else:
			print num
			
multiples(multiplier)