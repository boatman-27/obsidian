## What is a JWT?

JWT (short for JSON Web Token and pronounced “jot”) is an [open standard](https://www.descope.com/learn/post/authentication-protocols) used to create compact, self-contained tokens used for securely transmitting information between different applications or services.

These tokens are typically used for authentication and authorization, as they can contain information that [verifies the identity of a user](https://www.descope.com/learn/post/id-token), and their [permissions](https://www.descope.com/learn/post/access-token).

In terms of authentication, the information stored in the JWT is used to help servers establish trust between an unknown client and themselves.

## Structure of a JWT

The three main components of a JWT are the:

1. Header
2. Payload
3. Signature

### Header 

**The header** is a JSON object that typically contains two properties: The type of token (JWT) and the encryption algorithm used (e.g., HMAC SHA256, RSA, etc).

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```


### Payload

**The payload** is another JSON object where all of the transmitted data lives. Also called a _claim_, this data typically contains user information (username, email address), session data (IP address, time or last login), or authorization permissions (roles or groups the user belongs to).

There are four types of claims:
- **Commonly used:** Registered and public
- **Not commonly used:** Private and custom

```
{
  "drn": "DS",
  "exp": 1680902696,
  "rexp": "2023-05-05T21:14:56Z"
}
```

### Signature

**The signature** is created by signing the Base64Url encoded header and payload with a secret key and an algorithm specified by the developers. It is used to verify that the sender of the JWT is who they claim to be and ensure the token's integrity.


## How does a JWT work?

JWTs work by encoding a set of claims into a compact, URL-safe string. This string can be easily transmitted over the network and verified by the receiver.

Here is a general overview of how JWTs work:

1. The issuer of the JWT creates a new JWT object and sets the claims that it wants to include in the token.
2. The issuer signs the JWT object using a secret key or a public/private key pair.
3. The resulting JWT is a compact, URL-safe string that can be transmitted over the network.
4. The receiver of the JWT verifies the signature of the JWT using the secret key or the public key.
5. If the signature is valid, the receiver can trust the claims in the JWT.

### JWT authentication example

Here is how JWT can be used in an authentication flow:

1. A user provides their credentials (e.g., username and password) and sends them to the server.
2. The server validates the credentials. If they are correct, the server generates a JWT containing the user's information (in a claim) and signs it with a secret key.
3. The server sends the JWT back to the user.
4. The user stores the JWT (usually in the browser's local storage or as a cookie) and includes it in the Authorization header in subsequent requests to the server
5. When the user sends a new request with the JWT, the server decodes the JWT, and verifies its signature. If the token is valid, the server processes the request and returns the appropriate response.

## Advantages of using JWTs

Along with their stateless design and scalability, there are other reasons why you should consider using JWTs in your projects:

- **Cross-domain support:** Unlike cookies, JWTs can be used across different domains and subdomains, making them ideal for [Single Sign-On](https://www.descope.com/learn/post/sso) (SSO) implementations.
- **Self-containment and extensibility:** Since JWTs already contain necessary information about the user, they reduce the need for extra queries to a database for user data. Moreover, JWTs can be extended with custom claims to include additional information as needed, allowing for greater flexibility.
- **Mobile-friendly:** JWT tokens are an excellent choice for mobile app authentication due to their compact size and stateless nature. They allow for seamless integration with APIs and can greatly reduce server overhead.
- **Enhanced security:** JWTs can be encrypted to protect sensitive data, ensuring that only intended recipients can read the token's content. Moreover, the use of digital signatures ensures that the token has not been tampered with during transmission.
## Limitations and considerations of JWTs

It is important to choose the right token format for your application. While JWTs are a good choice for applications that need a compact and easy-to-use token format, it’s best to avoid using them:

- **When the payload contains sensitive information.** JWTs are not encrypted, and the payload can be read by anyone who gains access to it.
- **When the application has strict size limits on network requests.** JWTs can become large if they contain a lot of claims.
- **When the application is vulnerable to replay attacks.** JWTs can be vulnerable to replay attacks if they do not have a way to prevent them.
- **When the application is vulnerable to** [**man-in-the-middle attacks**](https://www.descope.com/learn/post/mitm-attack)**.** JWTs can be vulnerable to MITM attacks if they are not signed using a strong algorithm.
## Best practices for using JWTs

To ensure the security and effectiveness of JWTs in your application, follow these best practices:

- **Secure the secret key:** Make sure that you keep the secret key used to sign the JWT confidential to prevent unauthorized access. For added security, it’s best to use a key management system or store the key in a secure environment variable.
- **Use HTTPS:** To protect JWTs from being intercepted during transmission, always use HTTPS for communication between the client and server.
- **Use appropriate algorithms:** To protect your web application, make sure that you choose a suitable signing algorithm for your JWTs. [Asymmetric algorithms](https://cryptography.io/en/latest/hazmat/primitives/asymmetric/) (like RSA or ECDSA) are generally considered the best, as they use a public/private key pair, making it difficult for an attacker to forge tokens.
- **Handle token revocation:** You should always assign a short expiration time for JWTs to minimize the risk of token theft or misuse. Many libraries will implement a mechanism for token revocation to address situations where a user's access must be immediately revoked, such as account deletion or security breaches.