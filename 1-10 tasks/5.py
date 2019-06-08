#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
#Какое самое маленькое число делится нацело на все числа от 1 до 20?
#-----------------------------------------------------------
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

j = 1
j_old = 1
flag = 1
c_num = 20

while True:
	for i in range(1,(c_num+1)):
		r = j % i
		if r != 0:
			continue

		if j == j_old:
			flag+=1
		else:
			flag = 1
		j_old = j
	
	if flag == c_num:
		print(j)
		break
		
	j+=1

# j = 232792560
# 44 minutes was spent on the calculation of the result.