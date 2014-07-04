#!/usr/bin/env python3
import smtpd
# import sys
import email
import asyncore
from attachments2file import attachments2file


class SMTP2file(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        mail = email.message_from_string(data)
        attachments2file(mail, 'attachments')

s = SMTP2file(('127.0.0.1', 25), ())
asyncore.loop()
