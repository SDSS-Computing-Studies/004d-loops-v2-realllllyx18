#! python

name=input("Enter a name")
nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")
for x in nameList:
    if x==name:
        print("That name is on the list")
        break
if x!=name:
        print("That name is not in the list")
