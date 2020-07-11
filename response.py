import io
import socket
import typing

from collections import defaultdict
from headers import Headers


class Response():
    """An HTTP response.

      Parameters:
        status: The resposne status line (eg. "200 OK").
        headers: The response headers.
        body: A file containing the response body.
        content: A string representing the response body.  If this is
          provided, then body is ignored.
        encoding: An encoding for the content, if provided.
      """

    def __init__(
            self,
            status: str,
            Headers: typing.Optional[Headers] = None,
            body: typing.Optional[typing.IO] = None,
            content: typing.Optional[str] = None,
            encoding: str = "utf-8"
    ) -> None:

        self.status = status.encode()
        self.headers = headers or Headers()

        if content is not None:
            self.body = io.BytesIO(content.encode(encoding))
        elif body is None:
            self.body = io.BytesIO()
        else:
            self.body = body

    def send(self, sock: socket.socket) -> None:
        """Write this response to a socket.
        """
        raise NotImplementedError
