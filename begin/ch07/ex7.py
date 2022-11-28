# 딕셔너리 : key와 value 쌍으로 구성
dic1 = {1:'a', 2:'b', 3:'c'}
print(dic1)
# {1: 'a', 2: 'b', 3: 'c'}

student1 = {'학번':1000, '이름':'홍길동','학과':'컴퓨터학과'}
print(student1)
# {'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
# 타입이 일치하지 않아도 잘 출력이 된다.

student1['연락처'] = '010-2222-3333'
print(student1)
# {'학번': 1000, '이름': '홍길동', '학과': '컴퓨터학과', '연락처': '010-2222-3333'}

# 수정
student1['학과'] = '파이썬학과'
print(student1)
# {'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '연락처': '010-2222-3333'} 수정

# 삭제
del(student1['학과'])
print(student1)
# {'학번': 1000, '이름': '홍길동', '연락처': '010-2222-3333'}

# 찾기
print(student1.get('학과'))
# none

print(student1.get('이름'))
# 홍길동

print(student1.get('홍길동'))
# key 값을 찾아야함 => none

# key값 리턴하기
print(student1.keys())