import time

a = 5
s = time.time()
for i in range(a):
    for j in range(a):
        if j<=i:
            print("*", end='')
    print()
print(time.time()-s)

print('----------------------------')

for i in range(5):
    for j in range(5):
        if i<=j:
            print("*",end='')
        else:
            print(" ",end ='')
    print()

print('----------------------------')

for i in range(5):
    for j in range(5):
        if j == i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print('----------------------------')

for i in range(5):
    for j in range(5):
        if i>=j:
            print(" ",end='')
        else:
            print("*",end='')
    print()