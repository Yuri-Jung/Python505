#ex4.py

myList = [30, 10, 20,222]
print("현재 리스트 : %s" % myList)

myList.append(40) #리스트 마지막에 40추가
print("append(40)사용 현재 리스트 : %s" % myList)

myList.sort() #오름차순 정렬
print("sort() 사용 현재 리스트 : %s" % myList)

myList.reverse() #내림차순 정렬
print("현재 리스트 : %s" % myList)

print("reverse() 사용 20값 위치 : %d" % myList.index(20))

myList.insert(2,222) # 두 번째 자리에 222추가 -> 1개만 지워지나보다, 더 앞쪽에 있는 값이 삭제되었다.
print("2에 222를 추가함.현재 리스트 : %s" % myList)

myList.remove(222) #222제거
print("remove(222) : 현재 리스트 : %s" % myList)

myList.extend([77,88,77]) #배열 더하기
print("현재 리스트 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))









