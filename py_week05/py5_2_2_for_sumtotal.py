#1+2+3+4+.........>=100

hap, i = 0, 0

for i in range(1, 101):
    hap += i
    if hap >= 100:
        break


print("1~100의 합에서 최초로 100이 넘는 위치: %d의 합 %d" % (i, hap))
