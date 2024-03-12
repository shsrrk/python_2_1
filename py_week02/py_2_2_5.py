#input(): 키보드로부터 입력받는 명령어
#두 수를 입력받아 +, -, *, / 결과값 출력
#이때 실수는 소숫점 첫째자리까지 표시

a = int(input("첫 번째 수를 입력하세요 : "))
b = int(input("두 번째 수를 입력하세요 : "))

add = a + b
sub = a - b
mul = a * b
div = a / b

print(a, "+", b, "=", add)
print(a, "-", b, "=", sub)
print(a, "*", b, "=", mul)
print(a, "/", b, "=", div)
print(a, "/", b, "=","%7.1f" %div)


