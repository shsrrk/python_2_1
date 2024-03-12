# 345672원이 만 원이 몇장, 만 원이 계산된 후 오천 원이 몇장,,,,,
# 오천 원이 계산된 후 천 원이 몇장, 오백 원이 몇 개, 백 원이 몇개

'''
345672
만 원: 34
오천 원: 1
천 원: 0
오백 원: 1
백 원: 1
72원
'''
mon=345672
mod=mon//10000
print('만 원 : ', mod)

mon=mon%10000
mod=mon//5000
print('오천 원 : ', mod)

mon=mon%5000
mod=mon//1000
print('천 원 : ', mod)

mon=mon%1000
mod=mon//500
print('오백 원 : ', mod)

mon=mon%500
mod=mon//100
print('백 원 : ', mod)

