# Quiz 2. 2부터 입력받은 숫자 n 사이에 있는 소수들의 합과 그 개수를 구하시오 (1은 소수로 x)
# ex ) 
# n = 6
# 소수 : 2, 3, 5 -> 개수 : 3, 합 : 10
# n = 10
# 소수 : 2, 3, 5, 7 -> 개수 : 4, 합 : 17

# n = 2,3,4,5
a = []
for i in range(2,10):
    flag = True
    for j in range(2,i):
        if i%j == 0:
            flag = False
            break
    if flag:
        a.append(i)
    else:
        continue
print(a)
print(f'소수 : {len(a)}개')
print(f'소수의 합 : {sum(a)}')