#!/usr/bin/env python3
'''
Usage as script:
attachments2file file1[ file2[...fileN]..]
'''
import email
import sys
import os


def attachments2file(msg, dir_out='.'):
    '''
    Takes message, extracts attachments and saves them to directory
    '''
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        filename = part.get_filename()
        if not filename:
            continue
        if not os.path.isdir(dir_out):
            try:
                os.makedirs(dir_out)
            except FileExistsError:
                print('Can\'t make dir to output attachments')
                return
        full_path = os.path.join(dir_out, filename)
        for count in range(1, 1000):
            if os.path.isfile(full_path):
                newname = '{:04d}_'.format(count)+filename
                full_path = os.path.join(dir_out, newname)
        with open(full_path, 'wb') as fp:
            fp.write(part.get_payload(decode=True))


def main():
    if len(sys.argv) == 1:
        sys.exit('Usage: attachments2file file1[ file2[...fileN]..]')
    for arg in sys.argv[1:]:
        with open(arg) as body_f:
            msg = email.message_from_file(body_f)
        attachments2file(msg, 'attachments')


if __name__ == '__main__':
    main()
