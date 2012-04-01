"""
The `filesocket` module implements socket behavior backed by two
file-like object to and from which the actual data is read and
written.
"""

import sys
import socket


class FileSocket(object):

    def __init__(self, in_file=sys.stdin, out_file=sys.stdout,
                 use_out_fileno=False):
        self.in_file = in_file
        self.out_file = out_file

        fileno_file = in_file
        if use_out_fileno:
            fileno_file = out_file
        if hasattr(fileno_file, 'fileno'):
            self.fileno = fileno_file.fileno

    def recv(self, bufsize, flags=0):
        return self.in_file.read(bufsize)

    def send(self, string):
        return self.out_file.write(string)    

    def shutdown(self, how):
        if how in (socket.SHUT_RD, socket.SHUT_RDWR):
            self.in_file.close()
        if how in (socket.SHUT_WR, socket.SHUT_RDWR):
            self.out_file.close()

    def close(self):
        del self.in_file
        del self.out_file
