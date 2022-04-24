def suma(a,b):
    suma=a+b
    return suma

print(suma(3,5))


for i in range(5):
    for j in range(5):
        #print("%s,%s"%(i,j))
        print("%s + %s = %s"% (i,j,suma(i,j)))
