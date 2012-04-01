==========
filesocket
==========

The `filesocket` module implements socket behavior backed by two
file-like object to and from which the actual data is read and
written.

Create a filesocket wrapper using the FileSocket class.

    >>> from filesocket import FileSocket
    >>> fsocket = FileSocket()

By default, the socket uses `sys.stdin` for reading and `sys.stdout`
for writing.

    >>> fsocket.send('foo')
    foo
    >>> fsocket.recv(0)
    ''

