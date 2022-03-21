from time import sleep
import requests

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

logout_url = 'http://10.10.42.3/F.htm'

session = requests.Session()
r = session.get(logout_url)

if r.status_code == 200:
    print('注销成功')

sleep(0.3)


