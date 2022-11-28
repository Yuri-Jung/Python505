#ex1.py
# 전역변수
# function제작
coffee = 0
def coffee_machine(button):
    print()
    print('#1.뜨거운 물을 준비한다')
    print('#2.종이컵을 준비한다')
    
    if coffee == 1:
        print('#3.보통커피를 탄다')
    elif coffee == 2:
        print('#3.설탕커피를 탄다')
    elif coffee == 3:
        print('#3.블랙커피를 탄다')
    else:
        print('#3.아무거나 탄다\n')
        
    print("#4. 물을 붓는다.");
    print("#5. 스푼으로 젓는다.");
    print()

# 여기까지 function

coffee = int(input("어떤 커피를 드릴까요?(1.보통 2.설탕 3.블랙)"))
coffee_machine(coffee)
print("A손님 여기 커피있습니다");

coffee = int(input("어떤 커피를 드릴까요?(1.보통 2.설탕 3.블랙)"))
coffee_machine(coffee)
print("B손님 여기 커피있습니다");
print();
coffee = int(input("어떤 커피를 드릴까요?(1.보통 2.설탕 3.블랙)"))
coffee_machine(coffee)
print("C손님 여기 커피있습니다");

# 함수와 메서드의 차이점
# 메서드는 반복되는 일을 사용할 때 많이 사용됨


