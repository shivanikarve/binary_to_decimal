num=int(input("enter a binary number:"))
i=0
sum=0
while num!=0:
	rem=num%10
	sum=sum+rem*pow(2, i)
	num=int(num/10)
	i=i+1
print("dacimal number",sum)


# num = list(input("Input a binary number: "))
# value = 0
# for i in range(len(num)):
# 	digit = num.pop()
# 	if digit == '1':
# 		value = value + pow(2, i)
# print("The decimal value of the number is", value)
