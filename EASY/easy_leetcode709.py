# covert string to lower

# print(ord('Z'),ord('z'))
# print(ord('A'),ord('a'))


data='DAyA'
for i in data:
    if i.isupper():
        print(chr(ord(i)+32),end='')
    else:
        print(i,end='')
