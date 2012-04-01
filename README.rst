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

The socket can be shutdown.  The `how` argument controls whether the
`in_file`, `out_file` or both are closed.

    >>> in_file.closed
    False
    >>> out_file.closed
    False

    >>> import socket
    >>> fsocket.shutdown(socket.SHUT_RD)
    >>> in_file.closed
    True
    >>> out_file.closed
    False

    >>> fsocket.shutdown(socket.SHUT_WR)
    >>> in_file.closed
    True
    >>> out_file.closed
    True

    >>> in_file = StringIO('bar')
    >>> out_file = StringIO()
    >>> fsocket = FileSocket(in_file, out_file)
    >>> in_file.closed
    False
    >>> out_file.closed
    False
    >>> fsocket.shutdown(socket.SHUT_RDWR)
    >>> in_file.closed
    True
    >>> out_file.closed
    True

The `close()` method just deletes the references to the files but
doesn't necessarily close them.

    >>> in_file = StringIO('bar')
    >>> out_file = StringIO()
    >>> fsocket = FileSocket(in_file, out_file)
    >>> in_file.closed
    False
    >>> out_file.closed
    False
    >>> fsocket.close()
    >>> in_file.closed
    False
    >>> out_file.closed
    False

