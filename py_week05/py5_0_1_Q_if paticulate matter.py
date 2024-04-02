#미세먼지 예보
PM = float(input('미세먼지(10마이크로램)의 농도는?(예: 23.3)'))
#PM = 90 #paticulate matter: 미세먼지
if 151 <= PM:
    print('미세먼지 농도: {:.2f}, 등급:{}'.format(PM, '매우나쁨'))
elif 81 <= PM:
    print('미세먼지 농도: {:.2f}, 등급:{}'.format(PM, '나쁨'))
elif 31 <= PM:
    print('미세먼지 농도: {:.2f}, 등급:{}'.format(PM, '보통'))
else:
    print('미세먼지 농도: {:.2f}, 등급:{}'.format(PM, '좋음'))
