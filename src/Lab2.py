#Victor Medina 
#Introduction to Python Programming:Lab 2 
#October 3rd 2016
numGuessed=int(input('Guess a number from 1-10, Enter "0" to end this simulation.:'))
correctNum=6
while(numGuessed!=correctNum):
	if numGuessed > 10 or numGuessed < 0:
		print('That is not a number from 1 to 10!')
	elif numGuessed==0:
		print('End Simulation') 
		exit()
	elif numGuessed > correctNum:
		print('That is too high!')
	else:
		print('That is too low!')
	numGuessed=int(input('Guess again! (Number from 1-10,0 to end.):'))
print('That is Correct')
print('End Simulation')
