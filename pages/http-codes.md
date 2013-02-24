title: "httpcode: what the hell is code 418? What, a teapot???"
date: 2012-09-05
tags: [tool]
abstract: Httpcode is a simple tool to explain the meaning of HTTP status codes

This is a neat tool that comes handy when you get exotic HTTP statut codes like the 418 one (teapots are bad guys, beware!).

It's opensource (fork it on [GitHub](https://github.com/rspivak/httpcode)) and you can install it easily with pip:

<pre class="shell">$ pip install httpcode</pre>

And this is the list of codes known to the tool.

<pre>Status code 100
Message: Continue
Code explanation: Request received, please continue</pre>

<pre>Status code 101
Message: Switching Protocols
Code explanation: Switching to new protocol; obey Upgrade header</pre>

<pre>Status code 200
Message: OK
Code explanation: Request fulfilled, document follows</pre>

<pre>Status code 201
Message: Created
Code explanation: Document created, URL follows</pre>

<pre>Status code 202
Message: Accepted
Code explanation: Request accepted, processing continues off-line</pre>

<pre>Status code 203
Message: Non-Authoritative Information
Code explanation: Request fulfilled from cache</pre>

<pre>Status code 204
Message: No Content
Code explanation: Request fulfilled, nothing follows</pre>

<pre>Status code 205
Message: Reset Content
Code explanation: Clear input form for further input.</pre>

<pre>Status code 206
Message: Partial Content
Code explanation: Partial content follows.</pre>

<pre>Status code 300
Message: Multiple Choices
Code explanation: Object has several resources -- see URI list</pre>

<pre>Status code 301
Message: Moved Permanently
Code explanation: Object moved permanently -- see URI list</pre>

<pre>Status code 302
Message: Found
Code explanation: Object moved temporarily -- see URI list</pre>

<pre>Status code 303
Message: See Other
Code explanation: Object moved -- see Method and URL list</pre>

<pre>Status code 304
Message: Not Modified
Code explanation: Document has not changed since given time</pre>

<pre>Status code 305
Message: Use Proxy
Code explanation: You must use proxy specified in Location to access this resource.</pre>

<pre>Status code 307
Message: Temporary Redirect
Code explanation: Object moved temporarily -- see URI list</pre>

<pre>Status code 400
Message: Bad Request
Code explanation: Bad request syntax or unsupported method</pre>

<pre>Status code 401
Message: Unauthorized
Code explanation: No permission -- see authorization schemes</pre>

<pre>Status code 402
Message: Payment Required
Code explanation: No payment -- see charging schemes</pre>

<pre>Status code 403
Message: Forbidden
Code explanation: Request forbidden -- authorization will not help</pre>

<pre>Status code 404
Message: Not Found
Code explanation: Nothing matches the given URI</pre>

<pre>Status code 405
Message: Method Not Allowed
Code explanation: Specified method is invalid for this resource.</pre>

<pre>Status code 406
Message: Not Acceptable
Code explanation: URI not available in preferred format.</pre>

<pre>Status code 407
Message: Proxy Authentication Required
Code explanation: You must authenticate with this proxy before proceeding.</pre>

<pre>Status code 408
Message: Request Timeout
Code explanation: Request timed out; try again later.</pre>

<pre>Status code 409
Message: Conflict
Code explanation: Request conflict.</pre>

<pre>Status code 410
Message: Gone
Code explanation: URI no longer exists and has been permanently removed.</pre>

<pre>Status code 411
Message: Length Required
Code explanation: Client must specify Content-Length.</pre>

<pre>Status code 412
Message: Precondition Failed
Code explanation: Precondition in headers is false.</pre>

<pre>Status code 413
Message: Request Entity Too Large
Code explanation: Entity is too large.</pre>

<pre>Status code 414
Message: Request-URI Too Long
Code explanation: URI is too long.</pre>

<pre>Status code 415
Message: Unsupported Media Type
Code explanation: Entity body in unsupported format.</pre>

<pre>Status code 416
Message: Requested Range Not Satisfiable
Code explanation: Cannot satisfy request range.</pre>

<pre>Status code 417
Message: Expectation Failed
Code explanation: Expect condition could not be satisfied.</pre>

<pre>Status code 418
Message: I'm a teapot
Code explanation: The HTCPCP server is a teapot</pre>

<pre>Status code 500
Message: Internal Server Error
Code explanation: Server got itself in trouble</pre>

<pre>Status code 501
Message: Not Implemented
Code explanation: Server does not support this operation</pre>

<pre>Status code 502
Message: Bad Gateway
Code explanation: Invalid responses from another server/proxy.</pre>

<pre>Status code 503
Message: Service Unavailable
Code explanation: The server cannot process the request due to a high load</pre>

<pre>Status code 504
Message: Gateway Timeout
Code explanation: The gateway server did not receive a timely response</pre>

<pre>Status code 505
Message: HTTP Version Not Supported
Code explanation: Cannot fulfill request.</pre>

If you are curious about the 418 code, there is an explanation on [Quora](http://www.quora.com/What-is-the-story-behind-HTTP-status-code-418-Im-a-Teapot). Do not expect to find any sense in it though...