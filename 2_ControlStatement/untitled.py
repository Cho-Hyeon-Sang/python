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


# quiz_3
from pprint import pprint

pog_csv = [ {'floor' : 0, 'cell' : 0},
  {'floor' : 0, 'cell' : 0},
  {'floor' : 0, 'cell' : 1},
  {'floor' : 0, 'cell' : 2},
  {'floor' : 0, 'cell' : 3},
  {'floor' : 1, 'cell' : 0},
  {'floor' : 1, 'cell' : 1},
  {'floor' : 1, 'cell' : 2},
  {'floor' : 1, 'cell' : 3},
  {'floor' : 1, 'cell' : 4},
  {'floor' : 2, 'cell' : 0},
  {'floor' : 2, 'cell' : 1},
  {'floor' : 2, 'cell' : 1},
  {'floor' : 2, 'cell' : 2},
  {'floor' : 2, 'cell' : 2},]

  # 결과 -> {
#           '0': {'0': 0, '1': 0, '2': 0, '3': 0}, 
#           '1': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}, 
#           '2': {'0': 0, '1': 0, '2': 0}
#        } 

dic ={}
for i in pog_csv:
    dic[str(i['floor'])] = {}
for i in range(len(pog_csv)):
    each = pog_csv[i]
    floor = str(each['floor'])
    cell = str(each['cell'])
    dic[floor][cell] = 0
pprint(dic)
# 이렇게 해도 될까요? 개현상 선생님?