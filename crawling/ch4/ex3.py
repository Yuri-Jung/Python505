# ch4 - ex3
import pandas as pd

data_dic={
    'year':[2018,2019,2020],
    'sales' : [350,480,1099]
}
# print(data_dic)
# {'year': [2018, 2019, 2020], 'sales': [350, 480, 1099]}

# 표 형태로 만들기
df1 = pd.DataFrame(data_dic)
# print(df1)
#    year  sales
# 0  2018    350
# 1  2019    480
# 2  2020   1099

data2 = ['1반','2반','3반','4반','5반']
df2 = pd.DataFrame([[85.2,78.6,81.3],[78.6,95.3,90.3]],
                   index=['중간고사','기말고사'],columns=data2[0:3])

# print(df2)
#         1반    2반    3반
# 중간고사  85.2  78.6  81.3
# 기말고사  78.6  95.3  90.3

data_df = [['20201101', 'Hong', '90', '95'], ['20201102',
'Kim', '93', '94'], ['20201103', 'Lee', '87', '97']]
df3 = pd.DataFrame(data_df)
# print(df3)
#           0     1   2   3
# 0  20201101  Hong  90  95
# 1  20201102   Kim  93  94
# 2  20201103   Lee  87  97

df3.columns = ['학번','이름','중간고사','기말고사']
# print(df3)
#          학번    이름 중간고사 기말고사
# 0  20201101  Hong   90   95
# 1  20201102   Kim   93   94
# 2  20201103   Lee   87   97

# print(df3.head(2))
#          학번    이름 중간고사 기말고사
# 0  20201101  Hong   90   95
# 1  20201102   Kim   93   94

# print(df3.tail(2))
#          학번   이름 중간고사 기말고사
# 1  20201102  Kim   93   94
# 2  20201103  Lee   87   97

# print(df3['이름'])
# 0    Hong
# 1     Kim
# 2     Lee
# Name: 이름, dtype: object

df3.to_csv('./data/score.csv', header=True, encoding='utf-8-sig')
df3.to_csv('./data/score1.csv', header=False, encoding='utf-8-sig')
# ,학번,이름,중간고사,기말고사 유무
# data 폴더안에 파일 생성되었다

df4 = pd.read_csv('./data/score.csv',encoding='utf-8', index_col=0)
df4 = pd.read_csv('./data/score.csv',encoding='utf-8', index_col='학번')
print(df4)
#          학번    이름  중간고사  기말고사
# 0  20201101  Hong    90    95
# 1  20201102   Kim    93    94
# 2  20201103   Lee    87    97

#           Unnamed: 0    이름  중간고사  기말고사
# 학번
# 20201101           0  Hong    90    95
# 20201102           1   Kim    93    94
# 20201103           2   Lee    87    97














