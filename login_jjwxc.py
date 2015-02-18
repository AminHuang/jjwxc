#! /usr/bin/env python
#coding:utf-8
 
import sys
import re
import urllib2
import urllib
import cookielib
import time
import random
from openUrl import *
## 这段代码是用于解决中文报错的问题  
#reload(sys)  
#sys.setdefaultencoding("utf8")

def login(username, password):
    # 处理cookie
    cookie = cookielib.CookieJar()
    cj = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cj)
    urllib2.install_opener(opener)

    # POST数据到登录URL
    response = postData(url_login, {'loginname': username, 'loginpassword': password, })
    print response.read()
    return response.url == url_logininfo

def comment_check(times):
    for i in range(times):
        cont = getData(url_comment)
        aelems = extract_val(cont)
        print find_result(cont)
        for aelem in aelems:
            values = aelem.split(',')
            commentid = values[0]
            replyid = values[1]
            novelid = values[2]
            print commentid,' ',replyid,' ',novelid
            url_read = url_comment + '?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid
            response_check = getData(url_read)
            print response_check
        time.sleep(8.0)
    ok = 1
    return ok



def extract_val(content):
    vals = []
    aelems = re.findall('<input type="button".*onclick="pass.*?\)', content)
    # print aelems
    for aelem in aelems:
        # print aelem
        splits = aelem.split(' ')
        taelem = splits[5]
        # print taelem
        matches = re.match('onclick="pass\((.*)\)',taelem)
        val = matches.group(1)
        vals.append(val)
    return vals

def find_result(content):
    aelems = re.findall('历史总评审字数.*</font>',content)
    return aelems