a=int(input())
b=int(input())
c=int(input())
print(type(a))

if((a>b)and (a>c)):
	print(a)
elif((c>b)and (c>a)):
	print(c)
else:
	print(b)
