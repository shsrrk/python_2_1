#4개의 수를 입력받아 합, 평균값, 최댓값, 최솟값을 출력
m,n,x,y = input('4개의 수를 입력>>').split()
a, b, c, d= float(m), float(n), float(x), float(y)
print('입력값:', a, b, c, d)
sum = a + b + c + d
print('합: '.sum, '평균: ', sum / 4)
print('최대: ', max(a, b, c, d), '최th: ', min(a, b, c, d))
