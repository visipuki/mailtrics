#!/usr/bin/env python3

from email import message_from_string
from smtpd import PureProxy
from attachments2file import attachments2file
from datetime import date
from os import path
import asyncore


class fork(PureProxy):
    def process_message(self, peer, mailfrom, rcpttos, data):
        super().process_message(peer, mailfrom, rcpttos, data)
        rcpts_str = ''.join(rcpttos)
        base_dir = 'attachments'
        date_subdir = str(date.today())
        save_to = path.join(base_dir, rcpts_str, date_subdir)
        mail = message_from_string(data)
        attachments2file(mail, save_to)


s = fork(('127.0.0.1', 1025), ('127.0.0.1', 25))
asyncore.loop()
