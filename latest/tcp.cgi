#!/usr/bin/python3
import cgi
import MySQLdb
from http import cookies
import random, string, os
import session
#----------------------------------------------------------------
# 処理
gotop = 0

form = cgi.FieldStorage()
credit = form.getfirst('credit')
security = form.getfirst('security_code')

connection = MySQLdb.connect(
	host='localhost',
	user='user1',
	passwd='passwordA1!',
	db='EC',
	charset='utf8'
)
cursor = connection.cursor()

if (credit != None) and (security != None):
    gotop = 1
    sql = "INSERT INTO `Credit` (`credit_num`, `security_code`) VALUES ('" + credit + "', '" + security + "')"
    cursor.execute(sql)
    connection.commit()
    connection.close()

connection = MySQLdb.connect(
	host='localhost',
	user='user1',
	passwd='passwordA1!',
	db='EC',
	charset='utf8'
)
cursor = connection.cursor()

#登録情報をDBに追加


#----------------------------------------------------------------
# HTML部
if gotop:
	print("Content-Type: text/html")
	htmlText = '''
	<!DOCTYPE html>
	<html lang="ja">
	    <head>
	    <link rel="stylesheet" href="./css/order_comp.css">
		<meta charset="utf-8">
		<title>sample file</title>
	    </head>

	    <body>
		<h1>Success!!</h1>
		<p>クレジットカードを登録しました</p>
		<input type="button" onclick="location.href='./top.cgi'" value="トップページへ戻る">
	    </body>
	</html>
	'''

else:
	print("Content-Type: text/html")
	htmlText = '''
	<!DOCTYPE html>
	<html lang="ja">
	    <head>
		<meta charset="utf-8">
		<title>sample file</title>
	    </head>

	    <body>
		<h1>Success!!</h1>
		<p>注文を確定しました</p>
		<p>クレジットカードを登録してください。</p>
		<form action="./tcp.cgi" method="post">
		    <input type="text" name="credit"><br>
		    <input type="text" name="security_code"><br>
		    <input type="submit" value="登録">
		</form>
	    </body>
	</html>
	'''

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
(END)
