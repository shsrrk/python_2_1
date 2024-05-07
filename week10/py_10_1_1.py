#<함수 zip()>
#몇개의 리스트나 튜플의 항목으로 조합된 튜플을 생성
#동일한 수로 이뤄진 여러개의 튜플 항목 시퀀스를 각각의 리스트로 묶어주는 역할을 하는 함수
#자료형 zip 은 간단히 리스트나 튜플로 변


a=['ftp','telnet','dns'] #list
b=(20,23,25,23) #tuple
print(zip(a,b)) #리스트나 튜플의 항목으로 조합
z=list(zip(a,b))    #zip해서 list로 변환
print(type(z))
print(z)

z2=tuple(zip(a,b))  #zip해서 tuple로 변환
print(type(z2))
print(z2)

print(dict(zip(a,b)))   #zip으로 해서 dictionary



print(list(zip('abcd','xy')))
print(tuple(zip('abcd','xy')))
print(dict(zip('abcd','xy')))
