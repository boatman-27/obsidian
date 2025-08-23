An API (Application Programming Interface) is a set of defined rules and protocols that allow different software applications to communicate and interact with each other. It provides a standardized way for developers to access and manipulate the functionalities or data of a service, application, or platform without needing to understand its internal workings.

APIs can be public or private and are commonly used to integrate disparate systems, facilitate third-party development, and enable interoperability between applications. They typically include endpoints, request methods (like GET, POST, PUT), and data formats (like JSON or XML) to interact with.

API architecture is usually explained in terms of client and server. The application sending the request is called the client, and the application sending the response is called the server.

## Types of APIs
### 1. **SOAP APIs (Simple Object Access Protocol)**
- **Format:** XML
- **How it works:**  
    SOAP APIs rely on a strict messaging protocol using XML for request and response between the client and server.
- **Use case:**  
    Often used in enterprise applications where security, ACID-compliance, and formal contracts are essential (e.g., banking, telecommunications).
- **Characteristics:**
    - Strict standards and structure
    - Uses HTTP, SMTP, or other protocols
    - Includes built-in error handling
    - Slower and less flexible than newer APIs
### 2. **RPC APIs (Remote Procedure Call)**
- **Format:** Can use XML (XML-RPC) or JSON (JSON-RPC)
- **How it works:**  
    The client invokes a function or method on the server (like `getUserInfo()`), and the server executes it and returns the result.
- **Use case:**  
    Useful in microservices and internal systems where functions need to be triggered remotely.
- **Characteristics:**
    - Simple and lightweight
    - Tight coupling between client and server functions
    - Less flexible than REST
### 3. **WebSocket APIs**
- **Format:** JSON (typically)
- **How it works:**  
    Establishes a **persistent, full-duplex** communication channel between client and server. After the initial handshake over HTTP, it upgrades the connection to a WebSocket.
- **Use case:**  
    Ideal for real-time applications like chat apps, online gaming, live sports feeds, etc.
- **Characteristics:**
    - Supports **two-way communication**
    - More efficient than polling REST APIs
    - Server can **push data** to the client at any time
### 4. **REST APIs ([[Representational State Transfer]])**
- **Format:** Usually JSON (sometimes XML)
- **How it works:**  
    The client sends HTTP requests (GET, POST, PUT, DELETE) to endpoints. The server processes the request and returns a response.
- **Use case:**  
    The most widely-used API type for web and mobile apps.
- **Characteristics:**
    - Stateless (each call is independent) (No memory of past interactions. Every request must contain all necessary information.)
    - Uses standard HTTP methods
    - Flexible and easy to use
    - scalable

## Authentication
API [[authentication]] is the process of verifying the identity of clients attempting to access an API, ensuring that only authorized users or applications can interact with the API's resources.

