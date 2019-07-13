#Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
#Какое число является 10001-ым простым числом?
#-----------------------------------------------------------
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001'st prime number?

n = 2
k = 0
flag = 0
while True:
	for i in range(1,n+1):
		if n%i==0:
			flag+=1
		if flag>2:
			break
	if flag<=2:
		k+=1
		print("Value = {} - {}#".format(n,k))
		flag = 0
	else:
		flag = 0
	if k>=10001:
		break
	n+=1

#Value = 104743 - 10001#