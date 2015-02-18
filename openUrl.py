# -*- coding: utf-8
# 该函数打开url并且处理GET和POST

import urllib, urllib2


# 伪装成浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
}

# 晋江的URL
url_jjwxc = 'http://my.jjwxc.net/'

# 登录的URL
url_login = url_jjwxc + 'login.php?action=login&amp;referer=http%3A%2F%2Fmy.jjwxc.net%2Fbackend%2Flogininfo.php%3Fjsid%3D837021-0.6555891444440931'

# 登录后的URL
url_logininfo = url_jjwxc + 'backend/logininfo.php'

url_comment = url_jjwxc + 'backend/comment_check.php'

# 设置链接等待时间
time_out = 10#sec

def openUrl(url):
	response = urllib2.urlopen(url, timeout = time_out)
	results = response.read()
	return results

# 获取URL的内容返回字符串
def getData(url):
    # GET数据
        # 先形成一个request
    request = urllib2.Request(url = url, headers = headers)
        # 访问后获得一个response
    response = urllib2.urlopen(request, timeout = time_out)
    results = response.read()
    return results

#  将post_data POST到url，返回response
def postData(url, data):
    # POST数据
        # POST的数据转码
    post_data = urllib.urlencode(data)
        # 先形成一个request
    request = urllib2.Request(
        url = url,
        data = post_data,
        headers = headers,
    )
        # 获取response
    response = urllib2.urlopen(request, timeout = time_out)
    return response