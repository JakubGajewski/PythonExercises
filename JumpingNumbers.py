# https://www.codewars.com/kata/jumping-number-special-numbers-series-number-4/train/python

#Definition
#Jumping number is the number that All adjacent digits in it differ by 1.

#Task
#Given a number, Find if it is Jumping or not .

#Warm-up (Highly recommended)
#Playing With Numbers Series
#Notes
 #   Number passed is always Positive .
  #  Return the result as String .
   # The difference between ‘9’ and ‘0’ is not considered as 1 .
    #All single digit numbers are considered as Jumping numbers.

	def jumping_number(number):
    first = int(str(number)[0])
    for i in range  (1, len(str(number))):
        if (int(str(number)[i])-first != 1) and (int(str(number)[i])-first != -1):
            return 'Not!!'
        first = int(str(number)[i])
    return 'Jumping!!'