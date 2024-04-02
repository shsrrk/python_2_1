#입력 단어가 지금까지 배운 파이썬의 키워드인지를 in문으로 검사해 결과를 출력

inkey = input('배운 파이썬 키워드를 입력하세요 >>')
keywords = "'False', 'True', 'and', 'in, 'is', 'not', 'or'"
print('입력단어 {}, 키워드인가? {}' .format(inkey, inkey in keywords))
