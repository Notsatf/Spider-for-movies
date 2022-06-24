# -*-codingutf-8-*-
# @Time : 2022/6/23 19:09
# @Author :  TX
# @File : 数据库存储.py
# @Software : PyCharm
import json
import pymysql
#mysql的数据库连接信息
conn = pymysql.connect(
    #服务器地址
        host = '127.0.0.1',
    #端口号
        port = 3306,
    #用户名
        user = 'root',
    #密码
        passwd = 'XTW20020220',
    #数据库名称
        db = 'filedata',
    #字符编码格式
        charset = 'utf8',
    )
#设置游标，进行数据库操作
cur = conn.cursor()
#创建表语句
#sql = "CREATE TABLE view63_tbl12(centerlat decimal(10,7) DEFAULT NULL,c_uuid VARCHAR(36) DEFAULT NULL ,centerlong decimal(10,7) DEFAULT NULL,c_month_z  varchar(6) DEFAULT NULL,c_month_e varchar(15) DEFAULT NULL,c_province varchar(25) DEFAULT NULL, c_province_lat_float float(15,7) DEFAULT NULL,c_province_long_float float(20,10) DEFAULT NULL,c_province_lat_str varchar(15) DEFAULT NULL,c_province_long_str varchar(20) DEFAULT NULL,c_city_suffix VARCHAR(30)  DEFAULT NULL ,c_suffix VARCHAR(30)  DEFAULT NULL ,c_am_pm VARCHAR(10)  DEFAULT NULL,c_phone_prefix VARCHAR(15)  DEFAULT NULL,c_int int(11) DEFAULT NULL ,c_long bigint(40) DEFAULT NULL ,c_boolean tinyint(1) DEFAULT NULL, c_text text,c_date_time datetime(3),c_float float(10,7) DEFAULT NULL ,c_double double(20,18) DEFAULT NULL ,a_string varchar(1024) DEFAULT NULL ,a_int varchar(1024) DEFAULT NULL ,a_boolean varchar(1024) DEFAULT NULL  ,a_long varchar(1024) DEFAULT NULL ,a_float varchar(1024) DEFAULT NULL ,a_double varchar(1024) DEFAULT NULL  ,a_datetime varchar(1024) DEFAULT NULL ,a_string_x varchar(1024) DEFAULT NULL ,a_int_x varchar(1024) DEFAULT NULL ,a_boolean_x varchar(1024) DEFAULT NULL ,a_long_x varchar(1024) DEFAULT NULL ,a_float_x varchar(1024) DEFAULT NULL ,a_double_x varchar(1024) DEFAULT NULL ,a_datetime_x varchar(1024) DEFAULT NULL ,a_zero varchar(1024) DEFAULT NULL,c_nested varchar(1024) DEFAULT NULL )ENGINE=InnoDB DEFAULT CHARSET=utf8;"
#cur.execute(sql)
#json文件读取路径
path1 = r"K:\PythonClass\spider_films\json_data\test.json"
#打开文件
with open(path1, 'r', encoding='utf-8',errors='ignore') as f:
    ln=0
    #逐行读取
    for line in f.readlines():
        ln +=1
        #将数据转化为字典形式存储
        dic = json.loads(line,strict=False)
        #keys=dic.keys()
        #以，进行key的拼接，对应json中的字段
        keys = ', '.join(dic.keys())
       # value=dic.values()
        # 循环 dic.values() 如果类型是list或dict 转为str
        #print(type(dic.values()))
        print(keys)
        #将字典value信息存储成list
        valuesList = [dici for dici in dic.values()]
        #进行List列表的遍历
        for index1, value1 in enumerate(valuesList):
#             print(type(value1), value1)
        #如果是list,将其以str类型存储
            if isinstance(value1, list):
               # print(value1)
                valuesList[index1] = str(value1)
    #将str类型转化成元组形式存储
        valuesTuple = tuple(valuesList)
#         print((valuesTuple))
       # strdata=json.dumps(data)
    #将value值进行拼接
        values = ', '.join(['%s']*len(dic))
       # print(values)
    #设置表名称
        table="movies"
        #构造sql插入语句
        sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
#         print(sql)
        #执行sql语句
        cur.execute(sql,valuesTuple)
        conn.commit()
conn.close()
