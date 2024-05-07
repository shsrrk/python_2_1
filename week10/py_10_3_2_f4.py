#가변 매개변수(Arbitrary argumentList)
#입력개수가 달라질 수 있는 매개변수
# * 를 이용하여 정의된 가변 매개변수는 튜플

def merge_string(*text_list):
    result=''
    for s in text_list:
        result += s
        return result

#main
print(merge_string('red','green'))
print(merge_string('aaa','bbb','ccc'))
print(merge_string('dd','ee','ff','gg'))
