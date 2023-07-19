#!/usr/bin/python3

import cgi
import MySQLdb
from http import cookies
import random, string, os
import session
import hashlib
#----------------------------------------------------------------

form = cgi.FieldStorage()
email = form.getfirst("email")
password = form.getfirst("password")

if password is not None:
#パスワードのハッシュ化
	hs_password = hashlib.sha256(password.encode()).hexdigest()

#使用するデータベースに接続
connection = MySQLdb.connect(
 host='localhost',
 user='user1',
 passwd='passwordA1!',
 db='EC',
 charset='utf8'
)
cursor = connection.cursor()

ch_login = 0
if (email != None):
    cursor.execute("select * from UserInfo where mail_address='" + email + "'")
    rows = cursor.fetchall()

    #MySQLに登録されているパスワードの先頭にある空白文字の削除
    for row in rows:
        if row != None:
            pas = row[1].lstrip()
            if (hs_password == pas):
                ch_login = 1
                break

#----------------------------------------------------------------
# HTML部

if ch_login:
	print("Content-Type: text/html")
	htmlText = '''
	<!DOCTYPE html>
	<html lang="ja">
	    <head>
		<meta charset="utf-8">
		<title>My Page</title>
		
	    </head>

	    <body>
	'''
	for row in rows:
	    htmlText+='''
	    <p>氏名： %s %s</p>
	    <p>郵便番号： %s</p>
	    <p>住所： %s</p>
	    <p>電話番号： %s</p>
	    <p>メールアドレス： %s</p>
	    '''%(row[2], row[3], row[4], row[5], row[6], row[7])
	
	''' 	
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
		<title>My Page</title>
		
	    </head>

	    <body>
	    <p>メールアドレスとパスワードを入力して下さい。</p>
	    <form action="./mypage.cgi" method="post">
	        <input type="text" name="email" placeholder="メールアドレス"><br>
	        <input type="password" name="password" placeholder="パスワード"><br>
	        <input type="submit" value="送信">
	    </form>
	    	
	    </body>
	</html>
	'''

print(htmlText.encode("utf-8", 'ignore').decode('utf-8'))
(END)
