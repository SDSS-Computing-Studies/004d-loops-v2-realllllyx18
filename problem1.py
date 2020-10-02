#! python

integer=(input("Enter an integer")).strip()

for i in range(1,13):
    z=int(integer)*i
    print(z,end=""+" ")
