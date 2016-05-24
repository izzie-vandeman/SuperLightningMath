#!/bin/python3

#ToDo list
#GitHub
#Configurable highest number
#Subtraction & Division modes
#Colors

import random
import datetime

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
			print('good job!!!!')
			numberright = numberright + 1
		else:
			print('good try, but the answer was {}'.format(correctanswer))
			numberwrong = numberwrong + 1
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



