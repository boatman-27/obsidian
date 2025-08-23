Cookie-based authentication is a method of maintaining user sessions in web applications. When a user logs in, the server creates a session and sends a unique identifier (session ID) to the client as a cookie.

This cookie is then sent with every subsequent request, allowing the server to identify and authenticate the user. The actual session data is typically stored on the server, with the cookie merely serving as a key to access this data. This approach is stateful on the server side and works well for traditional web applications.

It's relatively simple to implement and is natively supported by browsers. However, cookie-based authentication faces challenges with cross-origin requests, can be vulnerable to CSRF attacks if not properly secured, and may not be ideal for modern single-page applications or mobile apps.

## What is Session-Based Authentication?

Session-based authentication is a stateful authentication technique where we use sessions to keep track of the authenticated user. Here is how Session Based Authentication works:

- User submits the login request for authentication.
- Server validates the credentials. If the credentials are valid, the server initiates a session and stores some information about the client. This information can be stored in memory, file system, or database. The server also generates a unique identifier that it can later use to retrieve this session information from the storage. Server sends this unique session identifier to the client.
- Client saves the session id in a cookie and this cookie is sent to the server in each request made after the authentication.
- Server, upon receiving a request, checks if the session id is present in the request and uses this session id to get information about the client.

###### Example of session data stored in DB
``` json
Session-ID: "V-F6dZDSRRwc7sPD3A0A5asrO3GeBxC3"
Session-Data: {
	"cookie": {
	    "originalMaxAge": 3600000,
	    "expires": "2025-03-10T18:38:05.710Z",
	    "secure": false,
	    "httpOnly": true,
	    "path": "/",
	    "sameSite": true
	  },
	  "passport": {
	    "user": 1
  }
}
```
##### `cookie`
- `originalMaxAge: 3600000` → 1 hour (in milliseconds).
- `expires: ...` → When this session will expire.
- `secure: false` → Will work over HTTP, not just HTTPS.
- `httpOnly: true` → Cannot be accessed by JavaScript (good for security).
- `sameSite: true` → Limits cross-site requests (prevents CSRF).
##### `passport.user`
- This is the user ID that `passport` stored in the session via `req.login(user)` and `serializeUser`.
- When a request with this session ID comes in, `passport` automatically calls `deserializeUser(1)` to attach the full user to `req.user`.

CHECK MORE IN: [Boilerplate](https://github.com/boatman-27/BoilerPlate/tree/master)
Example of code `index.js`
```js
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import bodyParser from "body-parser";
import passport from "passport";
import session from "express-session";
import pgSession from "connect-pg-simple";

import "./config/passport.js";
import pool from "./config/db.js";
import accountRouter from "./routes/accountRoutes.js";

dotenv.config();

const app = express();
const port = 3000;

if (process.env.NODE_ENV === "production") {
  app.set("trust proxy", 1);
}

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: true }));
const pgSessionStore = pgSession(session);

const corsOptions = {
  origin: [
    "http://localhost:5173",
    "https://trial-auth-drab.vercel.app",
    "http://192.168.0.51:5173",
  ],
  credentials: true,
};

app.use(cors(corsOptions));

app.use(
  session({
    store: new pgSessionStore({
      pool: pool,
      tablename: "session",
    }),
    secret: process.env.SESSION_SECRET,
    resave: true,
    saveUninitialized: true,
    cookie: {
      secure: process.env.NODE_ENV === "development" ? false : true,
      httpOnly: process.env.NODE_ENV === "development" ? false : true,
      sameSite: process.env.NODE_ENV === "development" ? "" : "none",
      maxAge: 1000 * 60 * 30,
    },
  })
);

app.use(passport.initialize());
app.use(passport.session());
app.use(passport.authenticate("session"));

const checkAuth = async (req, res, next) => {
  if (req.isAuthenticated()) {
    next();
  } else {
    res.status(401).json({ message: "Please log in" });
  }
};

app.get("/auth", (req, res) => {
  if (req.isAuthenticated()) {
    res.status(200).json({ message: "User is authenticated", user: req.user });
  } else {
    res.status(401).json({ message: "User is not authenticated" });
  }
});

app.use("/account", accountRouter);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
```

`passport.js`
```js
import passport from "passport";
import { Strategy } from "passport-local";
import bcrypt from "bcrypt";
import pool from "./db.js";

passport.use(
  new Strategy(async function verify(username, password, done) {
    try {
      const { rows } = await pool.query(
        "SELECT * FROM users WHERE email = $1",
        [username]
      );
      if (rows.length === 0) {
        return done(null, false, { message: "Incorrect email." });
      } else {
        const user = rows[0];
        const isValidPassword = await bcrypt.compare(password, user.password);
        if (isValidPassword) {
          done(null, user);
        } else {
          done(null, false, { message: "Incorrect password." });
        }
      }
    } catch (error) {
      console.log(error);
      done(error);
    }
  })
);

passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser(async (id, done) => {
  try {
    const { rows } = await pool.query("SELECT * FROM users WHERE id = $1", [
      id,
    ]);
    if (rows.length > 0) {
      done(null, rows[0]);
    } else {
      done(new Error("User not found"), null);
    }
  } catch (error) {
    console.log(error);
    done(error, null);
  }
});
```