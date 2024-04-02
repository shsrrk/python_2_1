#영회 조조 할인 판정
from time import localtime #import
hour = localtime().tm_hour
mnt = localtime().tm_min
if hour < 10:
    print('지금 시각: %d시 %d분, 조조할인 됩니다.' %(hour, mnt))
else:
    print('지금 시각: %d시 %d분, 조조할인 안됩니다.' %(hour, mnt))
