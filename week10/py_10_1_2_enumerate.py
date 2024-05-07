#enumerate() 0부터 시작하는 첨자(n)와 항목값(s)의 튜플 리스트를 생성
#--(n, s)와 같이 생성된

lst = [10,20,30]
print(lst)
print(list(enumerate(lst)))

print(list(enumerate([22,33,44],start=1)))

lst2 = 'python'
print(list(enumerate(lst2)))
