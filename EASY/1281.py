# find difference between product and sum of numbers

n = 234

def ss(n):
    prod = 1

    sum = 0
    for i in str(n):
        prod*=int(i)
        sum+=int(i)
    return int(prod)-int(sum)
print(ss(n))



