#!/bin/python3

#ToDo list
#2 minute mode for +
#High Score
#Configurable highest number
#Subtraction & Division modes
#Colors

import random
import datetime
import time

name = ''
age = ''
factor1 = 0
factor2 = 0
correctanswer = 0
useranswer = 0
numberright = 0
numberwrong = 0
foundationfacts = [ 0, 1, 2, 5, 10 ]

print('Welcome to SuperLightning Math!')
print('this is a multiplication and addition program. use it to get FAST quicker!')
print('what is your name?')
name = input()
print('hello, {} how old are you?'.format(name))
age = int(input())

#Multiplication mode
if (age > 7):
	print('enter F for foundation facts,or R for regular:')
	foundation = input()
	print('enter T for timed mode or Q for 10 question mode:')
	mode = input()
	
	if (mode == 'Q'):
		start = datetime.datetime.now()
		for i in range(1,11):

			if (foundation == 'F'):
				factor1 = foundationfacts[random.randint(0,len(foundationfacts)) - 1]
			else:
				factor1 = random.randint(0,12)

			factor2 = random.randint(0,12)
			correctanswer = factor1 * factor2
			print('question {}: what is {} x {}?'.format(i,factor1,factor2))
			useranswer = int(input())
 
			if (useranswer == correctanswer):
				print('good job!!!!\n\n')

				numberright = numberright + 1
			else:
				print('good try, but the answer was {}\n\n'.format(correctanswer))
				numberwrong = numberwrong + 1
		end = datetime.datetime.now()
		yourtime = end - start
	else:
		i = 1
		print('get ready, your game will start in 5 secconds!!!!!!')
		time.sleep(5)
		start = datetime.datetime.now()
		now = start
		end = now + datetime.timedelta(minutes = 2)
		while (now < end):
			if (foundation == 'F'):
				factor1 = foundationfacts[random.randint(0,len(foundationfacts)) - 1]
			else:
				factor1 = random.randint(0,12)

			factor2 = random.randint(0,12)
			correctanswer = factor1 * factor2
			print('question {}: what is {} x {}?'.format(i,factor1,factor2))
			useranswer = int(input())
 
			if (useranswer == correctanswer):
				print('good job!!!!\n\n')
				numberright = numberright + 1
			else:
				print('good try, but the answer was {}\n\n'.format(correctanswer))
				numberwrong = numberwrong + 1
			i += 1
			now = datetime.datetime.now()

		yourtime = end - start
			
#Addition mode
else:
	start = datetime.datetime.now()
	for i in range(1,11):

		factor1 = random.randint(0,20)
		factor2 = random.randint(0,20)
		correctanswer = factor1 + factor2
		print('question {}: what is {} + {}?'.format(i,factor1,factor2))
		useranswer = int(input())
 
		if (useranswer == correctanswer):
			print('good job!!!!')
			numberright = numberright + 1
		else:
			print('good try, but the answer was {}'.format(correctanswer))
			numberwrong = numberwrong + 1

	end = datetime.datetime.now()
	yourtime = end - start

print('good job {}, you got {} correct and {} incorrect.'.format(name,numberright,numberwrong))
print('your time was {}.'.format(yourtime))


