
#! python

number=input("Enter a number")
x=int(number)
y=1

for i in range(1,x+1):
   y=y*i
print(number.strip()+"!"+" "+"is"+" "+str(y))
