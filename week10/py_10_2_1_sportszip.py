#구기 종목 리스트
#종목에 대응하는 팀원 수를 항목으로 구성
sports = ['축구','야구','농구','배구']
num = [11,9,5,6]

print(sports)
print(num)
print()

print('함수 zip():')
for s, i in zip(sports, num):
    print('%s: %d명' %(s, i), end = ' ')

print()
s = dict(zip(sports, num))
print(s)


print('여기부터는 딕셔너리에서 했던 키값 찍어내기 3개')
for key in s.keys():
    print('%s: %s명' %(key, s[key]), end = ' ')

print()
for item in s.items():
    print('{} {}명' .format(item[0], item[1]), end = ' ')
print()

print()
for item in s.items():
    print('{} {}명' .format(*item), end = ' ')
print()
