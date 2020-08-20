import json

import openpyxl as openpyxl
import pymssql
import pymysql
import pandas
import xlrd


class importData:
    # 连接数据库
    def connsql(self, dateList):
        # 本地数据库
        connect = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='study',
            port=3306)
        if connect:
            print('连接成功')
        # 创建一个游标对象，python里的sql都要通过cursor来执行
        cursor = connect.cursor()
        # 执行sql语句
        sql = "insert into student(Sno, Sname) values (%s, %s)"
        try:
            cursor.executemany(sql, dateList)   # sql执行
            connect.commit()  # 提交到数据库
        except Exception as e:  # 获取报错信息
            print(e)
        cursor.close()  # 关闭游标
        connect.close()  # 关闭连接

    def readExcel(self, path):
        book = xlrd.open_workbook(path)
        sheet1 = book.sheets()[0]
        report_name = sheet1.row_values(0)  # 获取报表名称行数据
        row_num = sheet1.nrows  # 获取总行数
        report_name = sheet1.ncols  # 获取总列数

        list = []
        # 循环每一行数据
        for i in range(1, row_num):
            row = sheet1.row_values(i)  # 获取行数据
            number = "".join(row[0].split())  #序号
            # print("".join(row[0].split()))
            name = "".join(row[1])  #姓名
            # print("".join(row[1].split()))
            myTuple = (number, name)
            list.append(myTuple)
        print(list)
        self.connsql(list)

if __name__ == '__main__':
    path = "D:/SVN/未来招投标平台/test/T_OpenBidInfo.xlsx"
    importData = importData()
    conn = importData.readExcel(path)
    #  假数据测试
    # importData.connsql()


