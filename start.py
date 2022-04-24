#test 
#print("Hellow World")

from dataclasses import replace


x=3 #integer
f=3.14 #float
name = "Python"

z=round(x+f,2)

print(f) 
print (z)
print(x+f)

dict ={"name":["Jon","Maria"],"age":[36,32]}

print(dict["name"][0])

z = input("podaj liczbę: ")

z=z.replace(",",".")
z2=z.replace(".","")
z2=z2.replace("-","")

if z2.isdecimal():
    print("podana liczba jest ok")
else:
    print("podana liczka jest zła")
print(float(z))

a=3
b=4
print("%s jest >/</== od %s" %(a,b))


