"""
CDT Brett Yelverton
x97226
8SEP16
"""
def pi_to(decimal):
	"""
	>>> pi_to(0)
	3.0
	>>> pi_to(1)
	3.1
	>>> pi_to(2)
	3.14
	>>> pi_to(3)
	3.142
	>>> pi_to(4)
	3.1416
	>>> pi_to(5)
	3.14159
	>>> pi_to(6)
	3.141593
	>>> pi_to(7)
	3.1415927
	>>> pi_to(8)
	3.14159265
	>>> pi_to(9)
	3.141592654
	>>> pi_to(10)
	3.1415926536
	>>> pi_to(11)
	3.14159265359
	>>> pi_to(12)
	3.14159265359
	>>> pi_to(13)
	3.1415926535898
	>>> pi_to(14)
	3.14159265358979
	>>> pi_to(15)
	3.141592653589793
	"""
    num=0
    if decimal == 0:
        part = (1 / 16 ** decimal) * ((4 /( 8 * decimal + 1)) - (2 / (8 * decimal + 4)) - (1 /( 8 * decimal + 5)) - (1 / (8 * decimal + 6)))
        printnum = round(part,decimal)
    else:
        for number in range(0, decimal, 1):
            part = (1 / 16 ** number) * ((4 /( 8 * number + 1)) - (2 / (8 * number + 4)) - (1 /( 8 * number + 5)) - (1 / (8 * number + 6)))
            num = num + part
            printnum = round(num,decimal)
    print (printnum)

def    grant_meals(money,day,dayType):
	"""Breakfast is sandwich ($2.70 or 270 pennies) and a coffee ($2.35 or 235 pennies). Only eat breakfast on 2-day weekdays.
	Never pay for lunch at grant.
	Dinner at grant every night of the week except Thursday. Monday - Saturday is a large pizza ($11.25 or 1125 pennies), a pint of Ben and Jerry's ice cream ($5.95 or 595 pennies), and two 20 		oz. Cokes (diet $1.85 or 185 pennies, each).
	On Sunday night you have a garden salad ($5.50 or 550 pennies) and a water ($2.25 or 225 pennies).
	Convert money to pennies to have the values as integers.
	0==Mon
	1==Tue
	2==Wed
	3==Thu
	4==Fri
	5==Sat
	6==Sun
	Breakfast == 505 pennies
	Dinner Mon-Sat == 2090 pennies
	Dinner Sun == 775 pennies
	
	>>> grant_meals(5.00, 0, True)
	0
	>>> grant_meals(5.05, 0, False)
	1
	>>> grant_meals(7.75, 6, False)
	1
	>>> grant_meals(20.90, 0, True)
	4
	>>> grant_meals(20.90, 1, False)
	1
	>>> grant_meals(20.90, 1, True)
	3
	>>> grant_meals(20.90, 3, False)
	3
	>>> grant_meals(20.90, 3, True)
	3
	>>> grant_meals(20.90, 5, True)
	1
	>>> grant_meals(20.90, 6, True)
	3
	>>> grant_meals(200.00, 0, True)
	13
	>>> grant_meals(200.00, 0, False)
	13
	>>> grant_meals(200.00, 3, False)
	16
	"""
	week = 1
	pMoney = money * 100
	startPoint = day
	meals = 0
	breakfast = 505
	normDinner = 2090 
	sunDinner = 775
	while week <= 4:
		if week == 1 or 3:			
			if startPoint == 0:
				for days in range(0,7,1):				
					if days == 0 or 2 or 4 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 1 or 3:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
							if pMoney >= normDinner:
								pMoney = pMoney - normDinner
								meal = meal + 1
							else:
								break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 1:
				for days in range(1,7,1):
					if days == 0 or 2 or 4 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 1 or 3:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
							if pMoney >= normDinner:
								pMoney = pMoney - normDinner
								meal = meal + 1
							else:
								break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 2:
				for days in range(2,7,1):
					if days == 0 or 2 or 4 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 1 or 3:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
							if pMoney >= normDinner:
								pMoney = pMoney - normDinner
								meal = meal + 1
							else:
								break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 3:
				for days in range(3,7,1):
					if days == 0 or 2 or 4 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 1 or 3:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
							if pMoney >= normDinner:
								pMoney = pMoney - normDinner
								meal = meal + 1
							else:
								break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 4:
				for days in range(4,7,1):
					if days == 0 or 2 or 4 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 1 or 3:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
							if pMoney >= normDinner:
								pMoney = pMoney - normDinner
								meal = meal + 1
							else:
								break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 5:
				for days in range(5,7,1):
					if days == 0 or 2 or 4 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 1 or 3:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
							if pMoney >= normDinner:
								pMoney = pMoney - normDinner
								meal = meal + 1
							else:
								break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 6:
				for days in range(6,7,1):
					if days == 0 or 2 or 4 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 1 or 3:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
							if pMoney >= normDinner:
								pMoney = pMoney - normDinner
								meal = meal + 1
							else:
								break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
		elif week == 2 or 4:
			if startPoint == 0:
				for days in range(0,7,1):				
					if days == 1 or 3 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 0 or 2 or 4:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 1:
				for days in range(1,7,1):
					if days == 1 or 3 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 0 or 2 or 4:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 2:
				for days in range(2,7,1):
					if days == 1 or 3 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 0 or 2 or 4:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 3:
				for days in range(3,7,1):
					if days == 1 or 3 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 0 or 2 or 4:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 4:
				for days in range(4,7,1):
					if days == 1 or 3 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 0 or 2 or 4:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 5:
				for days in range(5,7,1):
					if days == 1 or 3 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 0 or 2 or 4:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
			elif startPoint == 6:
				for days in range(6,7,1):
					if days == 1 or 3 or 5:
						if pMoney >= normDinner:
							pMoney = pMoney - normDinner
							meal = meal + 1
						else:
							break
					elif days == 0 or 2 or 4:
						if pMoney >= breakfast:
							pMoney = pMoney - breakfast
							meal = meal + 1
						else:
							break
					elif days == 6:
						if pMoney >= sunDinner:							
							pMoney = pMoney - sunDinner
							meal = meal + 1
						else:
							break
				week = week + 1
print(meal)			



