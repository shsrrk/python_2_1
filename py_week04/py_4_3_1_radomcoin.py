import turtle       #터틀 그래픽 모듈을 불러온다.
import random       #난수 모듈을 불러온다.

screen = turtle.Screen() #screen 저거 이름임 아무거나 해도 상관 
image1 = "front.gif"
image2 = "back.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
coin = random.randint(0,1)
if coin ==0:
    t1.shape(image1)
else:
    t1.shape(image2)
