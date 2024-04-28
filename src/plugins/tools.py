"""
    会用到的预处理工具存放在此文件中。
    目前已拥有：
    1.
    待添加：
    1. 数据库连接
    2. 频道用户存入数据库（缓存）
    3. 频道发言-数据库用户匹配
    4. 以json或其他形式完成
"""
import time
import mysql.connector
# from nonebot import

# 连接到MySQL数据库
conn = mysql.connector.connect(
    host="114.132.85.27",
    user="BOT_Testing",
    password="HPDwPWiRDknsTFhA",
    database="bot_testing"
)

# 创建一个游标对象
cursor = conn.cursor()

# 执行SQL语句
cursor.execute("SELECT * FROM users")

# 获取结果
result = cursor.fetchall()

# 关闭连接
conn.close()