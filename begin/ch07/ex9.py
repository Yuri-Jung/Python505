import operator

trainDic, trainList = {}, []
# 딕셔너리, 리스트

trainDic = {'Thomas':'토마스', 'Edward':'에드워드', 'Henry':'헨리', 'Gothen':'고든', 'James':'제임스'}
print(trainDic)
# {'Thomas': '토마스', 'Edward': '에드워드', 'Henry': '헨리', 'Gothen': '고든', 'James': '제임스'}

trainList = sorted(trainDic.items(), key=operator.itemgetter(0))
print(trainList)
# [('Edward', '에드워드'), ('Gothen', '고든'), ('Henry', '헨리'), ('James', '제임스'), ('Thomas', '토마스')]

trainList = sorted(trainDic.items(), key=operator.itemgetter(1))
print(trainList)
# [('Gothen', '고든'), ('Edward', '에드워드'), ('James', '제임스'), ('Thomas', '토마스'), ('Henry', '헨리')]


# 음식을 치면 궁합 음식을 출력해준다
foods = {"떡볶이":"오뎅",
            "짜장면":"단무지",
            "라면":"김치",
            "피자":"피클",
            "맥주":"땅콩",
            "치킨":"치킨무",
            "삼겹살":"상추" };

# key값을 list로 변환해 출력
while True:
    myFood = input(str(list(foods.keys())) + "중 좋아하는 음식은?")
# ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']중 좋아하는 음식은?

    if myFood in foods:
        print("<%s> 궁합 음식은 <%s>입니다." %(myFood, foods.get(myFood)))
    elif myFood == "끝":
        break
    else:
        print("그런 음식이 없습니다. 확인해보세요")






