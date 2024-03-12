#input(): 키보드로부터 입력받는 명령어
#두 수를 입력받아 +, -, *, / 결과값 출력
#이때 실수는 소숫점 첫째자리까지 표시

num1 = int(input("입력1 : "))
num2 = int(input("입력2 : "))

print("합", num1+num2)
print("차", num1-num2)


ee=input("연산식 입력(예:3.2+4.1+2)");
print("연산식 : " , eval(ee));
