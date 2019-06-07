#Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. 
#Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
#-----------------------------------------------------------
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

i = 0
j = 0
r_new = 0
while True:
	r = j * i
	if len(str(r))==6:
		n = str(r)[:3]
		m = str(r)[3:][::-1]
		if n == m and r>r_new:
			print("{} * {} = Result = {}".format(j,i,r))
			r_new = r
	i+=1
	if i == 1000:
		j+=1
		i = 0
	if j == 1000:
		break

#913 * 993 = Result = 906609