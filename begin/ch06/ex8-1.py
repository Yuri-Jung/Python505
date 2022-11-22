
# 좀더 쉽게 하기~~~
while True:
    a = input("계산할 첫 번째 수를 입력하세요 : ")
    b = input("계산할 두 번째 수를 입력하세요 : ")
    ch = input("계산할 연산자를 선택해주세요  +  -  *  /  %  //  **  :  ")

    mathE = eval(a+ch+b)
    print(mathE)