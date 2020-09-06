a=777
b=777
print(a==b, a is b)
#Result : 777==777, 777 is 777

a=3.5
b=int(3.5)
print(a**((a//b)*2))
#Result : (3.5**(1*2))

print(((a-b)*a)//b)
#Result : ((0.5*3.5)//3)

b=(((a-b)*a)%b)
print(b)
#Result : ((0.5*3.5)%3)

print((a*4)%(b*4))
#Result : ((3.5*4)%(1.75*4))
