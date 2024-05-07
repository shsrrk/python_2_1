#일반 매개 변수와 함께 사용하는 가변 매개 변수

def print_args(argc, *argy):  #*를 사용하는 이유는 다 담을 수 있다.
    for i in range(argc):
        print(argv[i])
        
print_args('argv1', 'argv2', 'argv3',argc=3)
#print_args('argv1', 'argv2', 'argv3',3) 오류 예
