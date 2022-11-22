#ex8.py

ch = ''
a, b = 0, 0

# while True:
#     a = int(input("계산할 첫 번째 수를 입력하세요 : "))
#     b = int(input("계산할 두 번째 수를 입력하세요 : "))
#     ch = int(input("계산할 연산자를 선택해주세요 (1: + 2: - 3: * 4: / 5: % 6: // 7: ** 8: 나가기) : "))
#
#     if ch == 1:
#         print("%d + %d = %d" % (a, b, a + b))
#     elif ch == 2:
#         print("%d - %d = %d" % (a, b, a - b))
#     elif ch == 3:
#         print("%d * %d = %d" % (a, b, a * b))
#     elif ch == 4:
#         print("%d / %d = %d" % (a, b, a / b))
#     elif ch == 5:
#         print("%d % %d = %d" % (a, b, a % b))
#     elif ch == 6:
#         print("%d // %d = %d" % (a, b, a // b))
#     elif ch == 7:
#         print("%d ** %d = %d" % (a, b, a ** b))
#     elif ch == 8:
#         break
#     else:
#         print("다시 선택해주세요")

while True:
    a = int(input("계산할 첫 번째 수를 입력하세요 : "))
    b = int(input("계산할 두 번째 수를 입력하세요 : "))
    ch = input("계산할 연산자를 선택해주세요  +  -  *  /  %  //  **  :  ")

    if ch == '+':
        print("%d + %d = %d" % (a, b, a+b))
    elif ch =='-':
        print("%d - %d = %d" % (a, b, a - b))
    elif ch == '*':
        print("%d * %d = %d" % (a, b, a * b))
    elif ch == '/':
        print("%d / %d = 5.2%d" % (a, b, a / b))
    elif ch == '%':
        print("%d % %d = %d" % (a, b, a % b))
    elif ch == '//':
        print("%d // %d = %d" % (a, b, a // b))
    elif ch == '**':
        print("%d ** %d = %d" % (a, b, a ** b))
    else:
        print("연산자를 잘못 입력했습니다 다시 선택해주세요")








