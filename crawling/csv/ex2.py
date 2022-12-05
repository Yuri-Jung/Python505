#ex2.py

import os, re
import usecsv as uc

os.chdir(r'.\data')
apt = uc.switch(uc.opencsv('apt_202210.csv'))
#
# for i in apt[:6]:
#     print(i[-7])

# print('거래갯수 : ' , len(apt))

new_list = []
for i in apt:
    try :
        # 강원도 크기는 120 넘고 거래금액 3억 이상인 조건
        if i[5]>=120 and i[-7]>=50000 and re.match('강원', i[0]):
            # print(i[0],i[4],i[-4])
            new_list.append([i[0], i[4],i[-4]])
    #     i[-4] i의 뒤에서 4번째 값
    #  i[0]:도로명 , i[4]:단지명, i[-4]:도로명
    except :
        pass
print(len(new_list))
uc.writecsv('over120_lower30000.csv', new_list)



# 문제 부산에 크기는 150넘거나 5억 이상 리스트 저장

