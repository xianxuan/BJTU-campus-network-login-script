from getpass import getpass
from time import sleep
import requests

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

login_url = 'http://10.10.42.3/'

session = requests.Session()

r0 = session.get(login_url)
if '注销页' in r0.text:
    print('已登录，无需重复登录')
    exit()

user = input('学号：')
pswd = getpass()

data = {'DDDDD':user, 
        'upass':pswd,
        '0MKKey':''}

r = session.post(login_url, data)

if r.status_code == 200:
    r2 = session.get(login_url)
    if '注销页' in r2.text:
        print('登录成功')
    else:
        print('账号或密码错误，请重新登录')
else:
    print('登录失败，请检查网络链路是否畅通')

session.close()
sleep(0.3)


