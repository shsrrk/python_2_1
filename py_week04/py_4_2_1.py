#체질량 지수(BMI: Body Mass Index): 키가 1미터(m), 체중(w), 킬로그램(kg)일때
h, w = input('당신의 키(cm)와 몸무게(kg)은? >>').split()
height = float(h)
weight = float(w)
bmi = weight / (height/100)**2

print('키:%6.1f(cm), 몸무게: %5.1f(kg), BMI:%5.1f' %(height, weight, bmi))
print('{} {}' .format('고도비만', 40 <=bmi))
print('{} {}' .format('중등도비만', 35 <=bmi < 40))
print('{} {}' .format('비만', 30 <=bmi < 35))
print('{} {}' .format('과체중', 25 <=bmi < 30))
print('{} {}' .format('정상', 18.5 <=bmi < 25))
print('{} {}' .format('저체중', bmi < 18.5))
