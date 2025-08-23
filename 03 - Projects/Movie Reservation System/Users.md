
## SQL table
```sQL
CREATE TABLE users (
	userid VARCHAR(36) PRIMARY KEY,
	name TEXT NOT NULL,
	email VARCHAR(50) NOT NULL UNIQUE,
	password TEXT NOT NULL,
	role VARCHAR(5) NOT NULL DEFAULT 'user' CHECK (role IN ('admin', 'user')),
	createdat TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	updatedat TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
)
```


INSERT INTO users (userid, name, email, password, role)
VALUES (
  'c6ae32ca-059d-4230-abe2-58af6fd22fea',
  'Adham Osman',
  'adham4603@gmail.com',
  '$2a$10$0dV0UQvvhFdK8EYSc5V2ZefFbOUuYqkzQpHX0zS2Ije5L6..sSkt.',
  'admin'
);