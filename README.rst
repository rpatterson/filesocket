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

File sockets can also be given specific file objects to use.

    >>> from StringIO import StringIO
    >>> in_file = StringIO('bar')
    >>> out_file = StringIO()

    >>> fsocket = FileSocket(in_file, out_file)
    >>> fsocket.send('foo')
    >>> out_file.getvalue()
    'foo'
    >>> fsocket.recv(3)
    'bar'
    