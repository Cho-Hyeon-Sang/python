# 정사각형 별찍기
for i in range(3):
    for j in range(3):
        print('현상', end='')
    print()


# 역직각삼각형
for i in range(3):
    for j in range(3):
        if i>j:
            print('', end="")
        else:
            print('현상', end="")
    print()
