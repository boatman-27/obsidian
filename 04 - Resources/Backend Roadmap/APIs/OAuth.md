OAuth is an open standard for authorization that allows third-party applications to access a user's resources without exposing their credentials.

It works by issuing access tokens after users grant permission, which applications then use to interact with resource servers on behalf of the user. This process involves a resource owner (the user), a resource server (which holds the data), and an authorization server (which issues tokens).

OAuth enables secure, token-based access management, commonly used for granting applications permissions to interact with services like social media accounts or cloud storage.

OAuth was created as a response to the direct authentication pattern. This pattern was made famous by HTTP Basic Authentication, where the user is prompted for a username and password. Basic Authentication is still used as a primitive form of API authentication for server-side applications: instead of sending a username and password to the server with each request, the user sends an API key ID and secret. 

Before OAuth, sites would prompt you to enter your username and password directly into a form and they would login to your data (e.g. your Gmail account) as you.

To create a better system for the web, federated identity was created for single sign-on (SSO). In this scenario, an end user talks to their identity provider, and the identity provider generates a cryptographically signed token which it hands off to the application to authenticate the user. The application trusts the identity provider. As long as that trust relationship works with the signed assertion, you’re good to go. The diagram below shows how this works.

<img src="https://developer.okta.com/assets-jekyll/browser_spa_implicit_flow-9116158c9299208718b42a75921acd10a60e4c829edee55a8f14a9ce8de40028.png">

## OAuth Central Components
OAuth is built on the following central components:
- Scopes and Consent
- Actors
- Clients
- Tokens
- Authorization Server
- Flows
### OAuth Scopes
Scopes are what you see on the authorization screens when an app requests permissions. They’re bundles of permissions asked for by the client when requesting a token. These are coded by the application developer when writing the application.

The consent can vary based on the application. It can be a time-sensitive range (day, weeks, months), but not all platforms allow you to choose the duration.

<img src="https://developer.okta.com/assets-jekyll/blog/oauth/oauth-scopes-7ea53a0efe6c05a8113671297f641baae7486dfb6ab8b8357c74cb6e6f8371ce.png">

### OAuth Actors
The actors in OAuth flows are as follows:
- **Resource Owner**: owns the data in the resource server. For example, I’m the Resource Owner of my Facebook profile.
- **Resource Server**: The API which stores data the application wants to access
- **Client**: the application that wants to access your data
- **Authorization Server**: The main engine of OAuth

When you use GitHub to sign into LeetCode

| Role                     | Who/What                                                                     |
| ------------------------ | ---------------------------------------------------------------------------- |
| **Resource Owner (RO)**  | You — the GitHub account holder                                              |
| **Client**               | **LeetCode** — the app trying to access your GitHub info                     |
| **Resource Server (RS)** | **GitHub's API** — where your data (like username, email, profile pic) lives |
| **Authorization Server** | **GitHub's OAuth server** — the server that handles login and token issuance |
### OAuth Tokens
Access tokens are the token the client uses to access the Resource Server (API). They’re meant to be short-lived. Think of them in hours and minutes, not days and month. You don’t need a confidential client to get an access token. You can get access tokens with public clients. They’re designed to optimize for internet scale problems. Because these tokens can be short lived and scale out, they can’t be revoked, you just have to wait for them to time out.

The other token is the refresh token. This is much longer-lived; days, months, years. This can be used to get new tokens. To get a refresh token, applications typically require confidential clients with authentication.

Refresh tokens can be revoked. When revoking an application’s access in a dashboard, you’re killing its refresh token. This gives you the ability to force the clients to rotate secrets. What you’re doing is you’re using your refresh token to get new access tokens and the access tokens are going over the wire to hit all the API resources. Each time you refresh your access token you get a new cryptographically signed token. Key rotation is built into the system.

The OAuth spec doesn’t define what a token is. It can be in whatever format you want. Usually though, you want these tokens to be JSON Web Tokens. In a nutshell, a JWT (pronounced “jot”) is a secure and trustworthy standard for token authentication. JWTs allow you to digitally sign information (referred to as claims) with a signature and can be verified at a later time with a secret signing key.

You can use the access token to get access to APIs. Once it expires, you’ll have to go back to the token endpoint with the refresh token to get a new access token.