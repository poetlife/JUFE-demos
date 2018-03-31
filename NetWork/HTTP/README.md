# HTTP
## HTTP概况
HTTP, HyperText Transfer Protocol, 超文本传输协议
A stateless protocol
Base on TCP with port 80
## 非持续连接和持续连接
connection: close
connection: keep-alive
## HTTP报文格式
Methods:
---------------------------
1. GET
2. POST
3. PUT
4. DELETE
5. HEAD

Request: 1. request line 2. header line 3. entity body
----------------------------
GET /basedir/index.html HTTP/1.1 \\r\\n
Host: www.jxufe.edu.com \\r\\n
Connection: close \\r\\n
User-agent: Mozilla/5.0 \\r\\n
Accept-language: zh \\n

Response: 1. status line 2. header line 3. entity body
---------------------------
HTTP/1.1 200 OK
Connection: close
Date: Tue, 09 Aug 2011 15:44:04 GMT
Server: Apache/2.2.3 (CentOS)
Last-Modified: Tue, 09 Aug 2011 15:11:04 GMT
Content-Length: 6821
Content-Type: text/html

(data data data data data ... )

status code
---------------------------
1. 200 OK
2. 301 Moved Permanently
3. 400 Bad Request
4. 404 Not Found
5. 505 HTTP Version Not Supported

## cookie
1. cookies header in HTTP response
2. cookies header in HTTP request
3. cookies in user-end
4. cookies in server-end

## web缓存
web cache
web proxy server

## 条件GET方法
send:
-----------------------
If-modified-since: Tue, 09 Aug 2011 15:11:04 GMT

recv:
-----------------------
HTTP 304 not modified
