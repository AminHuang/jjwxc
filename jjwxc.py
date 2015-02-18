#!/usr/bin/python
#encoding=utf-8

# -*- coding: utf-8 -*-

import getpass
import urllib2
import socket

from login_jjwxc import *

is_login = False
is_quit = False

if __name__ == '__main__':
    print 'please login first'
    while not is_quit:
        while not is_login:
            try:
                # username = raw_input('username:')
                # password = getpass.getpass('password:')
                username = 'kom9ing@163.com'
                password = '3310571'
            except EOFError:
                print 'EOFError'
                is_quit = True
                break
            except KeyboardInterrupt:
                print 'KeyboardInterrupt'
                is_quit = True
                break
            else:
                try:
                    is_login = login(username, password)
                except urllib2.URLError:
                    print 'link error'
                except socket.timeout:
                    print 'timeout'
                else:
                    if is_login:
                        print 'login succeed!'
                    else:
                        print 'login flase!'
        if is_quit:
            break

        try:
            opera = raw_input('the time:')
        except EOFError:
            opera = '0'
            print 'EOFError'
        except KeyboardInterrupt:
            opera = '0'
            print 'KeyboardInterrupt'
        if opera != '0':
            ok = comment_check(int(opera))
            if ok:
                print 'comment check succeed!'

        if opera == '0':
            is_quit = True

    print 'Final!'


