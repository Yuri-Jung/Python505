import os, re
import usecsv as uc

os.chdir(r'.\data')
apt = uc.switch(uc.opencsv('apt_202210.csv'))


new_list = []
for i in apt:
    try :
        # 부산 크기 150넘거나 5억이상 리스트
        if (i[5] >= 150 or i[-7] >= 70000) and re.match('부산광역시', i[0]):
            new_list.append([i[0], i[4],i[-4] , i[-7],i[5]])

    except :
        pass

print(new_list)
print(len(new_list))
uc.writecsv('over150+high50000.csv', new_list)
#  파일 새로 생성
