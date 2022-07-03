# Quiz 3. cell_alert 데이터 만들기
# pog_csv file을 주었을떄, cell_alert 레디스 값을 만드는 로직 구현하기
# input data
# [ {'floor' : 0, 'cell' : 0},
#   {'floor' : 0, 'cell' : 0},
#   {'floor' : 0, 'cell' : 1},
#   {'floor' : 0, 'cell' : 2},
#   {'floor' : 0, 'cell' : 3},
#   {'floor' : 1, 'cell' : 0},
#   {'floor' : 1, 'cell' : 1},
#   {'floor' : 1, 'cell' : 2},
#   {'floor' : 1, 'cell' : 3},
#   {'floor' : 1, 'cell' : 4},
#   {'floor' : 2, 'cell' : 0},
#   {'floor' : 2, 'cell' : 1},
#   {'floor' : 2, 'cell' : 1},
#   {'floor' : 2, 'cell' : 2},
#   {'floor' : 2, 'cell' : 2},]
#
# 결과 -> {
#           '0': {'0': 0, '1': 0, '2': 0, '3': 0}, 
#           '1': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}, 
#           '2': {'0': 0, '1': 0, '2': 0}
#        } 
