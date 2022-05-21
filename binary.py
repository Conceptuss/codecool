def decimal_to_binary(decimal_number):
    n = decimal_number
    list = []
    n=int(n)
    while n >= 1:
        rest =n%2
        # print(rest)
        list.append(str(rest))
        n=n//2

    list.reverse()

    number = "".join(list)
    # for l in list:
    #     number+=str(l)

    return number




def binary_to_decimal(binary_number):
    binary_list=list(str(binary_number))
    binary_list.reverse()
    sum=0
    for i in range(0,len(binary_list)):
        
        sum+=int(binary_list[i]) * (2 ** i)
    return sum


print(decimal_to_binary(10))
print(binary_to_decimal(1010))
