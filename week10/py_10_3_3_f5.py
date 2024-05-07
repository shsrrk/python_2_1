#일반 매개 변수와 함께 사용하는 가변 매개 변수

def print_args(argc, *argy):  #*를 사용하는 이유는 다 담을 수 있다.
    for i in range(argc):
        print(argv[i])

print_args(3, 'red1', 'red2', 'red3')
#print_args(argc=3, 'argv1', 'argv2', 'argv3') 오류
