
print("--------PRINT-------")
print("Hello,Adhvik!!!!")

print("--------INPUT-------")
name=input()
print(f"Hello,{name}")

print("--------VARIABLES-------")
i=28;
print(F"{i}")
f=2.8
print(f"{f}")
b=True
print(f"{b}")
n=None
print(f"{n}")


print("--------CONDITIONS-------")
X=28
if X>0:
    print ("X is positive")
elif x<0:
    print("X is negative")
else:
    print("X is zero")


print("--------SEQUENCES-------")
fname="Alica"
coordinates =(10.0,20.0)
names=["Alice","Senthil","Adhvik","Priya"]
print(fname[1])
print(coordinates[0])
print(names[2])


print("--------LOOPS-------")
for i in range(5):
    print(i)

namelist=["Alice","Senthil","Adhvik","Priya"]
for (namel) in namelist:
    print(namel)

print("--------SETS-------")

s=set()
s.add(1)
s.add(2)
s.add(2)
s.add(2)
s.add(5)
s.add(5)
print(s)

print("--------DICTIONARY-------")
ages={"Senthil":35,"Priya":25,"Adhvik":5}
ages["Takshiv"]=3
ages["Takshiv"]+=2
print(ages)
