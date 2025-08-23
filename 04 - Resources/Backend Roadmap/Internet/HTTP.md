## What is HTTP?

**HTTP** stands for **HyperText Transfer Protocol**. It is the foundation of data communication on the World Wide Web. It is a protocol used for transferring hypertext requests and information between servers and browsers.

### Key Features of HTTP
- **Stateless**: Each HTTP request is independent; the server does not retain user data between requests.
- **Client-Server Model**: The client (usually a web browser) sends requests to the server, and the server responds with the requested content.
    
- **Methods**: Common HTTP methods include:
    - `GET`: Retrieve data
    - `POST`: Submit data
    - `PUT`: Update data
    - `DELETE`: Remove data
### Structure of an HTTP Request
```
GET /index.html HTTP/1.1
Host: www.example.com
```
### Structure of an HTTP Response
```
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

---
## What is HTML?
**HTML** stands for **HyperText Markup Language**. It is the standard language used to create and design web pages. HTML structures the content on the web.
### Key Features of HTML
- **Markup Language**: Uses tags to define elements (e.g., headings, paragraphs, links).   
- **Hierarchical Structure**: Elements can be nested inside other elements.
- **Static Content**: HTML itself is static; dynamic behavior is added using CSS and JavaScript.
### Basic HTML Document Structure
```
<!DOCTYPE html>
<html>
  <head>
    <title>My First Page</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
    <p>This is a paragraph.</p>
  </body>
</html>
```
### Common HTML Tags
- `<h1>` to `<h6>`: Headings
- `<p>`: Paragraph
- `<a href="">`: Anchor (link)
- `<img src="" alt="">`: Image
- `<div>`: Division or container
- `<span>`: Inline container

---
## Relationship Between HTTP and HTML
When you enter a URL in your browser:
1. The browser sends an **HTTP GET request** to the server.
2. The server responds with an **HTML document**.
3. The browser parses and displays the HTML content to the user.

In essence, **HTTP is the transport mechanism**, and **HTML is the content** that gets delivered.
