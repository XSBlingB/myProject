# -*- coding: utf-8
import requests
test_url = "http://www.163.com"
response = requests.get(test_url)   #requests.method(url,headers,data,...)
print (response.status_code)
print (response.headers)
print (response.text)


#模拟手机端请求
print ("展示的是163手机端的响应信息+++++++++++++++++++")
h = {"User-Agent":"Android/H60-L101/4.4.2/"}
response = requests.get(test_url,headers=h)
print (response.status_code)
print (response.headers)
print (response.text)

#练习Cookies参数
print ("练习cookies参数++++++++++++++++++++++++++++")
import requests
c = {"JSESSIONID":"1944D2279258F6E89832ECD8CF4B7B47"}
test_url = "https://mail.163.com/js6/main.jsp?sid=mCriJDWpbyMgzzQUtAppnOFYcbrBtOEn&df=mail163_letter#module=mbox.ListModule%7C%7B%22filter%22%3A%7B%22flags%22%3A%7B%22read%22%3Afalse%7D%7D%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%2C%22fids%22%3A%5B1%2C3%2C18%2C257%5D%7D"
response = requests.get( test_url,cookies = c)
#response = requests.get( test_url,headers ={"cookie":c})
#cookie也可以通过headers参数传递，不同之处在于cookie是以字典的形式发送的，
#而在headers里面cookie只是其中一个键，所以需要用key：value形式
print (response.status_code)
print (response.headers)
print (response.text)

#params参数可以存放请求的表单，并会以key1=value1&key2=value2的形式跟在
#URL之后发送，为了区分URL和参数，最好不要把表单放在URL里面，可以通过params参数进行发送
#URL部分把参数进行分离

import requests
print ("params参数练习+++++++++++++++++++++++++++++")
#c = "JSESSIONID":"1944D2279258F6E89832ECD8CF4B7B47"
#test_url ="https://mail.163.com/js6/main.jsp"
#p = {
 #   "sid":"mCriJDWpbyMgzzQUtAppnOFYcbrBtOEn",
 #   "df":"mail163_letter#module=mbox.ListModule%7C%7B%22filter%22%3A%7B%22flags%22%3A%7B%22read%22%3Afalse%7D%7D%2C%22order%22%3A%22date%22%2C%22desc%22%3Atrue%2C%22fids%22%3A%5B1%2C3%2C18%2C257%5D%7D"
#}
#response = requests.get(test_url,headers={"cookie":c},params=p)
#print (response.status_code)
#print (response.headers)
#print (response.text)

#data参数也是用于存放请求的表单，是requests模块的中重要的参数之一
#post可以提交四种类型的数据，post的数据类型必须和服务器接收的一致，若不一致会报错。至于需要post什么，可以抓包查看
#request header content-type

import requests
print ("data参数练习++++++++++++++++++++++++++++++")
test_url = "https://music.163.com/#/song?id=26608741"
form = {"params":"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",
        "encSecKey":"b7dfc4754af51bb30624fab98a30bd61584d1135181ce5c564b9968f2b1191b2e0756bdfee15c8d026d95818a587d80223b429ec37a5d3de86ae77298882ff2f8516ad96e744c5eef174dfe54d3afdc177ff1afce097b52c79ec7cb3867d37178d2d135684b32a41d386e268eaa16bc606b6e2418774bfb37f8fbc8ced13cc3d"}
response = requests.post(test_url,data=form)
print (response.status_code)
print (response.headers)
print (response.text)

#zhihu.com 练习 https请求模拟
print ("zhihu.com 练习 https +++++++++++++++++++++++++++++++++++++++++")
test_url = "https://www.zhihu.com/signup?next=%2F"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
r = requests.get(test_url,headers = headers)
print (r.status_code)
print (r.headers)
print (r.text)
