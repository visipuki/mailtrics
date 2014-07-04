#!/usr/bin/env python3

import imaplib
import email
import attachments2file

M = imaplib.IMAP4_SSL("gmail-imap.l.google.com")
criterion = '(ON "04-May-2014")'
M.login('lexa.konoplev', '(IJN9ijn!')
M.select()
typ, data = M.search(None, criterion)
print(typ, data)
for num in data[0].split():
    typ, msg_data = M.fetch(num, '(RFC822)')
    print('typ  of fetch {}'.format(typ))
#   print('data {}'.format(msg_data))
    mail_str = msg_data[0][1]
    msg = email.message_from_bytes(mail_str)
    attachments2file.attachments2file(msg, 'attachment')
M.logout()
