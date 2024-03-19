#문자열[start:end:step]
#step 간격 생략되면 1
#음수일 경우 역순 문자열 반환
str='python'
print(str[0:4:2]); #0부터 4까지 두개씩 건너뛰면
print(str[::3]);
print(str[::-2]);
