Token-based authentication is a protocol which allows users to verify their identity, and in return receive a unique access token. During the life of the token, users then access the website or app that the token has been issued for, rather than having to re-enter credentials each time they go back to the same webpage, app, or any resource protected with that same token.

Auth tokens work like a stamped ticket. The user retains access as long as the token remains valid. Once the user logs out or quits an app, the token is invalidated. Token-based authentication is different from traditional password-based or server-based authentication techniques. Tokens offer a second layer of security, and administrators have detailed control over each action and transaction.

## Token Authentication in 4 Easy Steps
Use a token-based authentication system, and visitors will verify credentials just once. In return, they'll get a token that allows access for a time period you define.

The process works like this:

- **Request:** The person asks for access to a server or protected resource. That could involve a login with a password, or it could involve some other process you specify.
- **Verification:** The server determines that the person should have access. That could involve checking the password against the username, or it could involve another process you specify.
- **Tokens:** The server communicates with the authentication device, like a ring, key, phone, or similar device. After verification, the server issues a token and passes it to the user.
- **Storage:** The token sits within the user's browser while work continues.

If the user attempts to visit a different part of the server, the token communicates with the server again. Access is granted or denied based on the token.

Administrators set limits on tokens. You could allow a one-use token that is immediately destroyed when the person logs out. Or you could set the token to self-destruct at the end of a specified time period.

## Why Should You Try Authorization Tokens?
You've assessed your current strategy, and you think things are working just fine. Why should authorization tokens become part of your systems? Very real benefits come to developers who take the plunge.

Authorization tokens are good for administrators of systems that:

- **Often grant temporary access.** Your user base fluctuates based on the date, the time, or a special event. Granting and rescinding access repeatedly is too draining. Tokens could be helpful.
    Administrators of university library sites, for example, might appreciate a token approach.
    
- **Require granular access.** Your server grants access based on specific document properties, not user properties. Passwords don't allow that time of fine-tuned detail.
    For example, you run an online journal. You want everyone to read and comment on only one document, not on any others. Tokens could allow this.
    
- **Are prime hacking targets.** Your server contains sensitive documents that could do your company intense damage on release. A simple password doesn't offer enough protection. A piece of hardware helps quite a bit.

<img src="https://roadmap.sh/guides/token-authentication.png">
