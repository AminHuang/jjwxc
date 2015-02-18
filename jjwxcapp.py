#!/usr/bin/python
#encoding=utf-8

import urllib,urllib2,httplib,cookielib
import time
import random
import re
import getpass

def extract_val(content):
    vals = []
    aelems = re.findall('<input type="button".*value="√通过"', content)
    # print aelems
    for aelem in aelems:
        # print aelem
        splits = aelem.split(' ')
        taelem = splits[5]
        # print taelem
        matches = re.match('onclick="pass\((.*)\)"',taelem)
        val = matches.group(1)
        vals.append(val)
    return vals

def find_result(content):
    aelems = re.findall('历史总评审字数.*</font>',content)
    return aelems

url='http://my.jjwxc.net/backend/comment_check.php'
url_login = "http://my.jjwxc.net/login.php?action=login&amp;referer=http%3A%2F%2Fmy.jjwxc.net%2Fbackend%2Flogininfo.php"


headers = { 
               'User-Agent'      : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'
             }

username='kom9ing@163.com'
password='3310571'

if __name__=='__main__':
    # username = raw_input('username:')
    # password = getpass.getpass('password:')
    user = { 
             'loginname'     : username,
             'loginpassword' : password,
           }
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    postdata = urllib.urlencode(user)
    request = urllib2.Request(url_login,postdata,headers=headers)
    response = urllib2.urlopen(request)
    thePage = response.read()
    # print thePage
    for i in range(30):
        op = opener.open(url)
        cont = op.read()
        aelems = extract_val(cont)
        print find_result(cont)
        for aelem in aelems:
            values = aelem.split(',')
            print values[0],' ',values[1],' ',values[2]
            commentid = values[0]
            replyid = values[1]
            novelid = values[2]
            url_read = url + '?act=pass&commentid='+commentid+'&replyid='+replyid+'&novelid='+novelid
            request2 = urllib2.Request(url_read, headers=headers)
            response_check = urllib2.urlopen(request2)
            print response_check.read()
        time.sleep(8.0)
    raw_input('end?')
