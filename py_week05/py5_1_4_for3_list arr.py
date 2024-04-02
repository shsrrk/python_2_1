# str() : 문자열 반환

aa = []
for i in range(0,4):
    aa.append(0) #리스트 값 초기화, 전부 0으로 만듦
hap = 0

for i in range(0, 4):
    aa[i] = int(input( str(i+1) + "번째 숫자:"))

hap = aa[0] + aa[1] + aa[2] + aa[3]

print("합계 ==> %d" %hap)
