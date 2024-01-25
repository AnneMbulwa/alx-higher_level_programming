0x10. Python - Network #0
General
What a URL is
    -URL (Uniform Resource Locator) is a web address that specifies the location of a resource on the internet.

What HTTP is
    -Hyper Text Transfer Protocol is an asymmetric request-response client-server
    protocol.
    - HTTP is a protocol used for transmitting data over the web

How to read a URL
    -The first part of the URL is the scheme, which tells you what protocol to use (e.g., "http" or "https"). The next part is the domain name, which identifies the server that hosts the resource. After the domain name, there may be a path, which specifies the location of the resource on the server. If there is a query string, it comes after the path and is used to pass additional information to the server. Finally, there may be a fragment identifier, which specifies a particular section of the resource.

The scheme for a HTTP URL
    -is http or https

What a domain name is
    -A domain name is a human-readable name that identifies a server or group of servers on the internet. It is mapped to an IP address, which is a numerical label assigned to each device connected to the internet.
    example
        google.com which the ip adress 128.192.1.2

What a sub-domain is
    -subdivision of the domain. comes before root domain and is separated by a dot
        example
            www.google.com - www is a subdomain

How to define a port number in a URL
    -To define a port number in a URL, append it to the hostname using a colon
    example
        http://example.com:8080

What a query string is
    -part of the URL that follows a question mark and contains parameters for the
    resource.
        example
            https://www.google.com/apply?batch=89&location=SF
        -the above url has 2 string query i.e batch with value of 89 and location
        with value of SF

What an HTTP request is
    -HTTP request is a message sent from a client to a server, requesting some
    action or resource. It consists of the following parts:

    1.Request line: This includes the HTTP method (GET, POST, etc.),
    the request URI, and the HTTP version.
        example: GET /index.html HTTP/1.1.

    2.Headers: Key-value pairs providing additional information about the request.
        Examples include Host, User-Agent, Accept-Language, and Accept-Encoding,
        Except, From.

    3.Body (optional):Contains data sent to the server as part of the request,
    usually in the case of POST or PUT requests.

What an HTTP response is
    -An HTTP response is a message sent from a server to a client, containing the result of the requested action or resource. It consists of the following parts:

    1. Status line: This includes the HTTP version, a status code, and a status
    message.
        example: HTTP/1.1 200 OK.
    2. Headers: Key-value pairs providing additional information about the response
        Examples include Content-Type, Content-Length, and Set-Cookie.
    3. Body: Contains the actual data (resource) being sent back to the client.

What HTTP headers are
    -are key-value pairs in the header section of an HTTP request or response.
    they allow client or server to pass additional information about request or
    a response

What the HTTP message body is
    -part of either HTTP Request or Response that carries the actual information
    being sent or received

What an HTTP request method is
    -specifies the desired action to be performed on a resource
    -In HTTP Requests we have methods such as POST, GET, HEAD,PUT

What an HTTP response status code is
    -is a 3-digit integer that indicates the results of the HTTP Request
    example
        404 Not found
        400 bad reqquest

What an HTTP Cookie is
    - a small piece of data that a server sends to a user's web browser.
                OR
    - is a small piece of data stored on the client's computer by a web server,
    containing information about the client's interaction with the server.

How to make a request with cURL
    - use the syntax:
            curl [options] [URL]

What happens when you type google.com in your browser (Application level)
    -The browser resolves the domain name google.com to an IP address using DNS.
    The browser initiates a TCP connection to the IP address on port 80 (HTTP) or
    443 (HTTPS).
    The browser sends an HTTP request (usually a GET request) to the server,
    asking for the resource at the root URL (/).
    The server processes the request and sends an HTTP response, containing the
    requested resource (usually an HTML page).
    The browser receives the response, parses the HTML, and renders the page.
    If the page contains additional resources (images, scripts, stylesheets, etc.),
    the browser initiates additional requests for those resources.
    The browser downloads and processes the additional resources, rendering the 
    final page.
