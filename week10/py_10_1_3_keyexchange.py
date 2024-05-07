#튜플과 시퀀스 간의 변환 // 리스트의 집합 간의 변환
#딕셔너리를 다른 시퀀스로 변환하면 항목이 키로만 구성

game = dict(일='밤', 이='낮', 삼='해', 사='달')

print(game)

print(list(game))   #key로만 구성

print(tuple(gmae))   #key로만 구성됨
print(set(game)) #key로만 구성
