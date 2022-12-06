# ex5.py
# 막대그래프

import matplotlib.pyplot as plt

y1 = [350,410,520,695]
y2 = [200,250,385,350]
x = range(len(y1))
print(x)
# range(0, 4)
# y1,y2값이 합쳐진 막대 그래프 약간 소다맛 아이스크림 같은

plt.bar(x,y1, width=0.7, color = 'blue')
plt.bar(x,y2, width=0.7, color = 'red', bottom=y1)
# y1이 아래에 있고 y2가 위에 있음

plt.title('Quarterly Sales')
plt.xlabel('Quarters')
plt.ylabel('Sales')
xLabel = ['first','second','third','fourth']
plt.xticks(x,xLabel, fontsize = 10)

plt.legend(['chairs','desks'])

plt.show()


