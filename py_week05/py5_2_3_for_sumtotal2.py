#1부터 100사이에 3의 배수만 출력하지 않고 다른 수치 합 출력하기
#continue 제어권을 for 문으로

hap, i = 0, 0

for i in range(1, 101):
    if i%3 == 0:
        continue

    hap += i


print("1~100의 합계 (3의 배수 제외): %d" % hap)
