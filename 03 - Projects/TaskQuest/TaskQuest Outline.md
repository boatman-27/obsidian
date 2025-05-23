#project 

This document outlines the TaskQuest project, the project will be build in React and Typescript. The main idea behind the app is to boost productivity by allowing users to earn their leisure time completing tasks for a reward that is either set by them or rewards set automatically by the system. 

The Project can be divided into 5 main features:
- [[Tasks]]
- [[Rewards]]
- [[Progress]]
- [[Socials]]
- [[Customization]]

```sql
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

## **Refresh Tokens**

```sql
CREATE TABLE refresh_tokens (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL,
    token TEXT NOT NULL UNIQUE,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    revoked BOOLEAN DEFAULT FALSE
);
```


## **Core Features**

### **1. Tasks System**

Users create and manage tasks, each with:

- **Difficulty levels (Easy, Medium, Hard)** affecting the **coin rewards**
- **Deadlines** to encourage timely completion
- **Status tracking** (**Pending, Completed, Expired**)
- **Categories & Priorities** to organize tasks
- **Coin limits** to prevent abuse

### **2. Rewards System**

Users spend earned coins in **two shops**:

1. **Developer Shop**: Pre-set rewards designed by you (e.g., themes, power-ups)
2. **User-Created Shop**: Custom rewards users can add for personal motivation

### **3. Progress Tracking**

Users gain **XP** from tasks and challenges:

- XP contributes to **level-ups**, unlocking new shop items
- **Streaks** encourage daily engagement
- Leaderboard rankings are influenced by XP and streaks

### **4. Customization**

Users can personalize their experience with:

- **Themes** (light/dark/custom colors)
- **Avatars** (default or unlockable via XP/shop)

### **5. Social Features**

Encourages community interaction with:

- **Friends System** (add/remove, track activity)
- **Leaderboard** (global & friends ranking)
- **Custom Challenges** (task- or XP-based competitions with rewards)

---

## **Tech & Logistics**

- **Frontend**: **React + TypeScript**, with **Tailwind CSS**
- **Backend**: Likely **PostgreSQL** (with structured tables for tasks, users, leaderboards, etc.)
- **Authentication**: User accounts linked to tasks and rewards
- **Data Flow**:
    - Tasks generate XP and coins →
    - Coins buy rewards →
    - XP leads to ranking up & unlocking new features →
    - Social engagement enhances motivation

---

## **Possible Enhancements**

- **Group Challenges**: Users team up to complete goals together
- **Daily/Weekly Missions**: Time-sensitive bonus objectives
- **Item Power-Ups**: One-time boosts (e.g., streak protection, double XP)
- **AI Task Suggestions**: Smart recommendations based on past tasks