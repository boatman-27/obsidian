This is a secure and simple RESTful API built with **Go**, using the **Gin** web framework and **PostgreSQL** for data storage.  
It supports managing user tasks — including creating, retrieving, updating, and deleting them — and incorporates a gamified coin reward system upon task completion.

> **Authentication and user management** (registration, login, JWT tokens, refresh, logout) are handled in a separate repository.  
> Kindly refer to [JWT_GO](https://github.com/boatman-27/JWT_GO) for full authentication implementation.

---
## Features
- PostgreSQL integration for users and tasks
- Task creation, editing, deletion
- Task status tracking: Backlog, In Progress, In Review, Done
- Coin-based reward system for completed tasks
- Task statistics (coins earned/pending, task counts by status)
---

## sQl tables

```sQL
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fname VARCHAR(255) NOT NULL,
    lname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    userId VARCHAR(10) NOT NULL UNIQUE,
    role VARCHAR(10) NOT NULL DEFAULT 'user' CHECK (role IN ('admin', 'user'))
    
    -- Gamification fields
    coins INT DEFAULT 0 CHECK (coins >= 0), -- Users earn/spend coins through tasks & shop
    xp INT DEFAULT 0 CHECK (xp >= 0), -- Experience points for leveling up
    level INT DEFAULT 1 CHECK (level >= 1), -- Users rank up based on XP
    streak INT DEFAULT 0 CHECK (streak >= 0), -- Daily task completion streak
    
    -- Social features
    friends_count INT DEFAULT 0 CHECK (friends_count >= 0), -- Number of friends added
    leaderboard_rank INT DEFAULT NULL, -- Rank in global leaderboard
    last_active TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP -- For activity tracking
);
```

```sQL
CREATE TABLE tasks (
	id SERIAL PRIMARY KEY, 
	taskName TEXT NOT NULL, 
	addedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	deadline TIMESTAMP NOT NULL,
	taskid VARCHAR(255) NOT NULL UNIQUE,
	userid VARCHAR(8) NOT NULL REFERENCES users(userId),
	difficulty TEXT NOT NULL CHECK (difficulty IN ('easy', 'medium', 'hard')) DEFAULT 'easy',
	coins INT NOT NULL,
	status TEXT NOT NULL CHECK (status IN ('Backlog', 'In Progress', 'In Review', 'Done')) DEFAULT 'Backlog',
	description TEXT, 
	category TEXT DEFAULT 'General', 
	priority INT CHECK (priority BETWEEN 1 AND 5) DEFAULT 3
);
```

### Example sQl commands for Tasks table

```sQL
INSERT INTO tasks (
	taskName, deadline, taskid, userid, difficulty, coins, status, description, category, priority
) VALUES
('Fix navbar bug', '2025-06-09 12:00:00', 'TASK001', 'u1234567', 'easy', 14, 'Backlog', 'Fix the responsive layout issue in the navbar.', 'UI', 2),
('Deploy backend to server', '2025-06-10 18:00:00', 'TASK002', 'u2345678', 'medium', 32, 'In Progress', 'Deploy the Express server to production using Docker.', 'DevOps', 4),
('Write documentation', '2025-06-11 17:00:00', 'TASK003', 'u3456789', 'easy', 14, 'In Review', 'Create markdown files for the new API endpoints.', 'Documentation', 3),
('Design landing page', '2025-06-12 20:00:00', 'TASK004', 'u4567890', 'hard', 100, 'Backlog', 'Mock up the new landing page using Figma.', 'Design', 5),
('Set up test coverage', '2025-06-13 09:00:00', 'TASK005', 'u5678901', 'medium', 23, 'Done', 'Integrate Jest and add coverage reporting.', 'Testing', 3),
('Implement login flow', '2025-06-14 14:00:00', 'TASK006', 'u6789012', 'hard', 80, 'In Progress', 'Implement full login/logout functionality with JWT.', 'Authentication', 4),
('Refactor utils module', '2025-06-15 10:00:00', 'TASK007', 'u7890123', 'medium', 35, 'Backlog', 'Refactor utility functions for better readability.', 'Code Cleanup', 2),
('Create user avatars', '2025-06-16 16:00:00', 'TASK008', 'u8901234', 'easy', 8, 'In Progress', 'Add avatar upload and display support in profile.', 'Feature', 3);
```

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/boatman-27/JWT_GO
cd JWT_GO
```

### 2. Setup environment variables

Create a `.env` file and add your secrets and DB config:
``` env
ACCESS_SECRET=your_access_secret
REFRESH_SECRET=your_refresh_secret
```


### 3. Install CompileDaemon (Optional)
Once installed, you can use `CompileDaemon` to watch your project files and recompile/run your Go application automatically on changes.

```Bash
go install github.com/githubnemo/CompileDaemon@latest
```

Add `export PATH="$HOME/go/bin:$PATH"` to your `shell` file (`.zshrc` or `.bashrc`)

### 4. Add an alias in your `shell` file (Optional)

```bash
alias gomon="CompileDaemon -build='go build -o myapp main.go' -command='./myapp'"
```

### 5. Run the application

If CompileDaemon is installed

```bash
gomon
```

OR if CompileDaemon is not installed

```
go run .
```

---
## API Endpoints
| Method | Endpoint         | Description                   | Auth Required      |
| ------ | ---------------- | ----------------------------- | ------------------ |
| GET    | `/adminGetTasks` | Get all tasks (admin only)    | Admin only         |
| GET    | `/getTasks`      | Get tasks by user ID          | Authenticated user |
| GET    | `/fetchTaskById` | Fetch task details by task ID | Authenticated user |
| GET    | `/stats`         | Get task status stats         | Authenticated user |
| POST   | `/AddTask`       | Add a new task                | Authenticated user |
| POST   | `/DeleteTask`    | Delete a task                 | Authenticated user |
| PUT    | `/EditTask`      | Edit a task                   | Authenticated user |
| PUT    | `/UpdateStatus`  | Change task status            | Authenticated user |

#### Example JSON for `task/stats`

```json
{
	"backlog": 0,
	"coins_earned": 74,
	"coins_pending": 0,
	"done": 2,
	"in_progress": 0,
	"in_review": 0,
	"total": 2
}
```

---
## Tech Stack
- Go (Golang)
- Gin Web Framework
- PostgreSQL
- JWT Authentication (see [JWT_GO](https://github.com/boatman-27/JWT_GO))
- CompileDaemon (for live reloading, optional)
---
## Future Enhancements
- Add pagination to `/getTasks`
- Email notifications for upcoming deadlines
- Shop to spend coins
- Admin panel UI
---

