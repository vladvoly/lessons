#Простые делители числа 13195 - это 5, 7, 13 и 29.
#Каков самый большой делитель числа 600851475143, являющийся простым числом?
#-----------------------------------------------------------
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?

a = 600851475143
i = 2 
flag = True
out = 0
while (flag == True):
	if(a%i==0):
		out = int(a/i)
		print("i = {}. out = {}".format(i,out))
		a = out
		i = 2
	elif(out == 1):
		flag = False
	i+=1

#i = 6857 - largest prime