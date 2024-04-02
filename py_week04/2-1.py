#center() 폭을 지정하고 중앙에 문자열 배치하는 메소드
#strip() 문자열 앞뒤의 특정 문자들을 제거하는 메소드
#lsplit()
#rsplit()
st1='python'
print(st1.center(30,'*'))
print(st1.center(30))
print(st1.center(30,'='))
st3='***python---'
st4='   python   '
print(st4.lstrip())
print(st4.rstrip())
print(st4.strip())
print(st3.strip('*'))
print(st3.strip('-'))
print(st3.strip('*-'))
