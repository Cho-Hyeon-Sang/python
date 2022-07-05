# Quiz 1 : a 리스트에서 "yusom"이라는 문자열을 출력하슈
a = [1, 2, [3, 4, ["hello", "yusom"]]]
print(a[2][2][1])

# Quiz 2 : a 리스트에서 인덱스의 번호가 홀수인 값을 슬라이싱으로 가져오고 출력하기
# 2 가지의 방법을 작성해보아요~
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1::2])
print(a[-1::-2])

# Quiz 3 : a 리스트를 오름차순으로 정렬하고 역순으로 정렬
a = [3, 6, 1, 10, 2, 7]
a.sort()
print(a)

a.reverse()
print(a)

# Quiz 4 : 3번 퀴즈에서 바뀐 a 리스트의 가운데 인덱스에 원소 100을 추가 해보슈(삽입 되는 인덱스의 위치는 인덱스 번호를 사용하지말고 함수를 사용 해보아요)
a.insert(len(a)//2, 100)
print(a)

# Quiz 5 : a 딕셔너리에 key : '1', value : 1 을 추가해 보아요
a = {1: 1, 2: 2}
a['1'] = 1
print(a)

# Quiz 6 : a 딕셔너리에서 "yusom" 문자열을 출력
a = {"a": {"b": ["hello", "yusom"]}}
print(a["a"]["b"][1])

# Quiz 7 : a 딕셔너리의 모든 key값, value값, (key, value)를 출력 해보거라~ 
print(a.keys(), a.values(), a.items())





# Quiz 8 : 각 연산의 결과를 구하고 설명
print(bool([])) 	# 답 : False  # 설명 : list가 비어있을 경우, boolean은 False를 의미하니까
print(bool(1))		# 답 : True   # 설명 : 0이 아니면 참이니까 , True
print(bool(2))		# 답 : True  # 설명 : 0이 아니면 참이니까 True 
print(bool(""))		# 답 : False  # 설명 : ""이 거짓이니까 False



# 유솜 화이팅 !!
# 이해 안가게 알려주면 욕하세요 ^-^
