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


# 소수 구하기
def get_prime_cnt_sum(number):
    li = []
    for n in range(2, number+1):
        for x in range(2, n):
            if n % x == 0:
                break
        else:
            li.append(n)
    return f'찌찌 개수:{len(li)}, 찌찌 합:{sum(li)}'

print(get_prime_cnt_sum(number=6))