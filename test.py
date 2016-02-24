#!/usr/bin/env python
# coding: utf-8

import time
import sys
if sys.version_info.major > 2:
    from wxbot3 import *
else:
    from wxbot import *

class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 5:
            self.send_msg(msg['user_name'], 'hi')
'''
    def schedule(self):
        self.send_msg('tb', 'schedule')
        time.sleep(1)
'''

def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()

if __name__ == '__main__':
    main()
