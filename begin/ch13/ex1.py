# db연동
# ch13 ex1

import pymysql 
# pip install pymysql
# pip : python install package
# 리눅스 환경

con, cur = None, None
data1, data2, data3, data4 = '','','',''
sql = ''

con = pymysql.connect(host='localhost', user = 'root', password = '1234', db='mydb', charset='utf8')
cur = con.cursor()

while True:
    data1 = input('사용자 id ==> ')
    if data1 == '':
        break
    data2 = input('사용자 이름 ==>')
    data3 = input('사용자 이메일 ==>')
    data4 = input('사용자 출생년도 ==>')
    sql = "INSERT INTO tblMember2 VALUES ('"+data1 + "','" + data2 + "','" + data3 + "','" + data4 + "')"
    cur.execute(sql)

    con.commit()
    con.close()


