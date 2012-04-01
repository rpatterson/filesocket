"""
The `filesocket` module implements socket behavior backed by two
file-like object to and from which the actual data is read and
written.
"""

import sys


class FileSocket(object):

    def __init__(self, in_file=sys.stdin, out_file=sys.stdout):
        self.in_file = in_file
        self.out_file = out_file

    def recv(self, bufsize, flags=0):
        return self.in_file.read(bufsize)

    def send(self, string):
        return self.out_file.write(string)    
