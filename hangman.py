word_deff =["codecool","dog"]
word =word_deff[0]
print(word)

y=""
for x in word:
    y=y+"_"


print(y)
lista=list(y)
print(lista)
print("teraz")
y2=""
for i in range(len(lista)):
    y2+=lista[i]

print(y2)
while y2!=word:
    a=input("podaj litere: ")
    for i in range(len(lista)):
        if a==word[i]:
            lista[i]=a


    y2=""
    for i in range(len(lista)):
        y2+=lista[i]
    print(y2)
    if y2==word:
        break


if y2==word:
    print("wygrałeś")
else:
    print("nie udało się")
