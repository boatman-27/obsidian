# **Tasks Feature Documentation**

## **Overview**
The tasks feature allows users to create, manage, and delete tasks. Each task is associated with specific metadata, such as difficulty, deadlines, and rewards in the form of coins. This system incentivizes users to complete tasks based on their difficulty level, with higher rewards for more challenging tasks.

---

## **Database Schema**

### **Tasks Table**
The `tasks` table stores all tasks created by users.

#### **Table Definition**
```sql
CREATE TABLE tasks (
	id SERIAL PRIMARY KEY, 
	taskName TEXT NOT NULL, 
	addedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	deadline TIMESTAMP NOT NULL,
	taskid VARCHAR(255) NOT NULL UNIQUE,
	userId VARCHAR(8) NOT NULL REFERENCES users(userId),
	difficulty TEXT NOT NULL CHECK (difficulty IN ('easy', 'medium', 'hard')) DEFAULT 'easy',
	coins INT NOT NULL,
	status TEXT NOT NULL CHECK (status IN ('Backlog', 'In Progress', 'In Review', 'Done')) DEFAULT 'Backlog',
	description TEXT, 
	category TEXT DEFAULT 'General', 
	priority INT CHECK (priority BETWEEN 1 AND 5) DEFAULT 3
);
```

### **Column Descriptions**

| **Column**    | **Type**       | **Description**                                                                                        |
| ------------- | -------------- | ------------------------------------------------------------------------------------------------------ |
| `id`          | `SERIAL`       | Unique identifier for each task.                                                                       |
| `taskName`    | `TEXT`         | Name of the task. Cannot be null.                                                                      |
| `addedOn`     | `TIMESTAMP`    | Timestamp of when the task was created. Defaults to the current timestamp.                             |
| `deadline`    | `TIMESTAMP`    | The deadline for the task.                                                                             |
| `userId`      | `VARCHAR(8)`   | References the `users` table to associate tasks with users.                                            |
| `taskid`      | `VARCHAR(255)` | Unique identifier for each task. tsk-(userid)-some_number                                              |
| `difficulty`  | `TEXT`         | Task difficulty. Allowed values: `easy`, `medium`, `hard`. Defaults to `easy`.                         |
| `coins`       | `INT`          | Coin rewards for completing the task, with ranges depending on difficulty.                             |
| `status`      | `TEXT`         | Current status of the task. Allowed values: `Backlog`, `In Progress`, `In Review`. Defaults to `Done`. |
| `description` | `TEXT`         | Optional field to provide additional details about the task.                                           |
| `category`    | `TEXT`         | Category of the task. Defaults to `General`.                                                           |
| `priority`    | `INT`          | Priority of the task, ranging from 1 (lowest) to 5 (highest). Defaults to 3.                           |
|               |                |                                                                                                        |
|               |                |                                                                                                        |

---

## **Coin Reward Limits**

Tasks have specific coin rewards based on their difficulty level:

| **Difficulty** | **Minimum Coins** | **Maximum Coins** |
| -------------- | ----------------- | ----------------- |
| Easy           | 5                 | 25                |
| Medium         | 26                | 50                |
| Hard           | 51                | 100               |

---

## **Feature Capabilities**

### **1. Adding Tasks**

Users can add tasks to the system. Each task must include:

- A name
- Deadline
- Difficulty level
- Coin reward
- Associated user ID

#### **Example SQL Query**
```sql
INSERT INTO tasks (taskName, taskid, deadline, userId, difficulty, coins, status, description, category, priority) 
VALUES 
('Write Chapter 4: Interpolation notes in Obsidian', 'tsk-Boatman-0001', '2025-02-12 12:00:00', 'Boatman', 'hard', 100, 'In Review', 'Optimize API endpoints for better performance', 'Maths', 4);
```


---

### **2. Deleting Tasks**

Tasks can be deleted from the system using their unique ID.

#### **Example SQL Query**


```sql DELETE FROM tasks WHERE id = 1;```

---

### **3. Updating Tasks**

Users can update task details, such as:

- Status (`pending`, `completed`, `expired`)
- Deadline
- Priority

#### **Example SQL Query**
`UPDATE tasks SET status = 'completed', priority = 2 WHERE id = 1;`

---

### **4. Querying Tasks**

Users can filter tasks based on priority, deadlines, or categories.

#### **Example SQL Query**
`SELECT * FROM tasks WHERE userId = 'USR12345' AND status = 'pending' ORDER BY priority DESC;`

---

## **Constraints**

### **Database Constraints**

1. **Difficulty:**
    - Values must be `easy`, `medium`, or `hard`.
2. **Coins:**
    - Coin rewards must align with the task's difficulty level.
3. **Status:**
    - Allowed values are `pending`, `completed`, or `expired`.
4. **Priority:**
    - Priority must be a number between 1 and 5.
5. **Foreign Key:**
    - Tasks must reference a valid user in the `users` table.

### **Business Logic**

- Users cannot assign tasks with past deadlines.
- Rewards must incentivize tasks based on difficulty.
- Categories and descriptions are optional but recommended for better organization.

---

## **Future Enhancements**

1. **Recurring Tasks:**
    - Add support for tasks that repeat at specified intervals.
2. **Task Dependencies:**
    - Enable linking tasks to represent dependencies (e.g., Task A must be completed before Task B).
3. **Progress Tracking:**
    - Add a `progress` column to represent partially completed tasks.
4. **Notifications:**
    - Notify users of approaching deadlines.
5. **Task Sharing:**
    - Allow tasks to be shared or assigned to multiple users.

---

## **Usage Scenarios**

1. **Personal Productivity:**
    - Users can prioritize tasks by difficulty, category, or deadline.
2. **Gamification:**
    - The coin reward system motivates users to complete more challenging tasks.
3. **Data Analytics:**
    - Admins can analyze user task trends to improve platform engagement.

---

## **Sample Data**

### **Example Task Entry**

|**ID**|**Name**|**Difficulty**|**Deadline**|**Coins**|**Status**|**Category**|**Priority**|
|---|---|---|---|---|---|---|---|
|1|Complete React Project|Hard|2025-02-01 18:00:00|50|Pending|Work|4|
|2|Write Blog Post|Medium|2025-01-30 12:00:00|25|Completed|General|3|