#Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
#a^2 + b^2 = c^2
#Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc.
#-----------------------------------------------------------
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

a = 1
b = 1
c = 1
a1 = 0
b1 = 0
c1 = 0
stop = 1000

while True:
	a1 = a ** 2
	b1 = b ** 2
	c1 = c ** 2
	x = a+b+c

	if (a1+b1)==c1 and x == 1000:
		print('{}^2 + {}^2 = {}^2'.format(a,b,c))
		print('-----------------------------------')
		print(a*b*c)
		break		
	c+=1
	
	if c>1000:
		b+=1
		c = b+1
	if b>1000:
		a+=1
		b = a+1
		c = a+2

#Product abc = 31875000