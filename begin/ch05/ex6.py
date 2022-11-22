select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

## 메인 코드 부분 ##
# eval 함수 사용 => 문자를 숫자형으로 변환해줌
# 1. 입력한 수식 계산  2. 두 수 사이의 합계 : 1
#  *** 수식을 입력하세요 : 3+4
#  3+4 결과는   7.0입니다.
#
# 힌트 :  eval 함수 사용
#
# 1. 입력한 수식 계산  2. 두 수 사이의 합계 : 2
#  *** 첫 번째 숫자를 입력하세요 : 10
#  *** 두 번째 숫자를 입력하세요 : 20
# 10+...+20는 165입니다.

# select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))
#
# if select == 1:
#     numStr = eval(input("수식을 입력해주세요 : "))
#     print("%d 입니다" % (numStr))
#
# elif select == 2:
#     num1 = int(input("*** 첫 번째 숫자를 입력해주세요 : "))
#     num2 = int(input("*** 두 번째 숫자를 입력해주세요 : "))
#     answer = 0
#     for i in range(num1, num2+1):
#         answer += i
#     print("%d +...+%d는 %d 입니다" % (num1, num2, answer))

select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 :"))

if select == 1:
    numStr = input("***수식을 입력해주세요")
    answer = eval(numStr)
    print("%s 결과는 %5.1f입니다" %(numStr,answer))
elif select == 2:
    num1 = int(input("*** 첫 번째 숫자를 입력해주세요 : "))
    num2 = int(input("*** 두 번째 숫자를 입력해주세요 : "))
    for i in range(num1,num2+1):
        answer = answer + i
    print("%d +...+ %d는 %d 입니다" % (num1, num2, answer))
else:
    print("1또는 2만 입력해야 합니다")






