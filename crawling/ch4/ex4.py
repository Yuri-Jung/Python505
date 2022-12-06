#ex4.py

import matplotlib.pyplot as plt

x = [2016,2017,2018,2019,2020]
y = [350,410,520,695,543]

plt.plot(x,y)
plt.title('Annual Sales')
plt.xlabel('year')
plt.ylabel('sales')
plt.show()

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.show()