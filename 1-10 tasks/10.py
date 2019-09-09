#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#Найдите сумму всех простых чисел меньше двух миллионов.
#-----------------------------------------------------------
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

n = 2000000
summa = 0
a = []
for i in range(0,(n+1)):
	a.append(i)
i = 2
while i <= n:
    if a[i] != 0:
        #print(i)
        summa+=i
        for j in range(i, n+1, i):
            a[j] = 0
    i+=1
print('-------------------------')
print(summa)

#sum = 142913828922