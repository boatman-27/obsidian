# **Progress System Documentation**

## **Overview**
The progress system is designed to track and reward user activity through two main features:  
1. **XP (Experience Points)**: Measures user progress and contributes to leveling up.  
2. **Streaks**: Tracks consecutive days of activity, encouraging consistency.  

Both XP and streaks contribute to unlocking rewards and maintaining user engagement.  

---

## **1. Experience Points (XP)**

### **How XP Works**
- Users earn XP by completing tasks based on their difficulty:  
  - **Easy Tasks**: 10 XP  
  - **Medium Tasks**: 25 XP  
  - **Hard Tasks**: 50 XP  
- Additional XP can be earned through bonus activities, such as maintaining streaks or completing milestone tasks.

### **XP Ranks**
As users gain XP, they rank up. Each rank unlocks specific rewards in the **Generic Shop**.  

| **Rank**        | **XP Required** | **Unlocks**                                   |
|------------------|-----------------|----------------------------------------------|
| Beginner         | 0–99            | Basic rewards (e.g., 1-hour break)           |
| Intermediate     | 100–499         | Mid-tier rewards (e.g., App subscriptions)   |
| Advanced         | 500–999         | Exclusive rewards (e.g., Premium vouchers)   |
| Expert           | 1000+           | Rare rewards (e.g., Custom items)            |

#### **XP Logging**
A new table tracks user XP over time.

```sql
CREATE TABLE xp_log (
    logId SERIAL PRIMARY KEY,
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    earnedXP INT NOT NULL CHECK (earnedXP > 0),
    reason TEXT NOT NULL,
    earnedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---
## **2. Streaks**

### **How Streaks Work**

- A streak tracks the number of consecutive days a user completes at least one task.
- Streak resets if the user misses a day.

#### **Streak Rewards**

- Users receive bonus XP for maintaining streaks:
    - **3-Day Streak**: +15 XP
    - **7-Day Streak**: +50 XP
    - **30-Day Streak**: +200 XP

### **Streak Table**

```sql
CREATE TABLE streaks (
    userId VARCHAR(8) PRIMARY KEY REFERENCES users(userId),
    currentStreak INT DEFAULT 0,
    longestStreak INT DEFAULT 0,
    lastActivity DATE
);
```

#### **Streak Logic**

1. **Daily Update**:
    
    - Check if the last activity is today or yesterday.
    - If yes, increment `currentStreak`.
    - If no, reset `currentStreak` to 0.
2. **Longest Streak**:
    
    - Update `longestStreak` if `currentStreak` exceeds it.

---

## **3. Unlocking Rewards**

### **Generic Shop Unlocks**

- Higher ranks unlock exclusive rewards in the **Generic Shop**.
- Example unlocks:
    - Intermediate Rank: Access to "3-Hour Break" reward.
    - Advanced Rank: Access to "Special Discounts".
    - Expert Rank: Custom reward creation privileges.

### **Streak Milestones**

- Users can earn exclusive rewards for achieving streak milestones:
    - **30-Day Streak**: "Golden Reward" worth 100 coins.
    - **90-Day Streak**: Rare collectible reward.

---
## **4. Progress Dashboard**

### **Dashboard Features**

The dashboard provides an overview of user progress:

- **XP Progress**: Displays current XP, rank, and XP required for the next rank.
- **Streak Tracker**: Shows the current and longest streak.
- **Achievements**: Highlights milestones, rewards, and completed tasks

---

## **5. Achievements System (Optional Feature)**

### **Overview**

An achievements system can provide additional motivation.

- **Examples**:
    - "First Task Completed" (10 XP)
    - "10-Day Streak" (50 XP)
    - "100 Tasks Completed" (100 XP)

### **Database Schema**

``` sql
CREATE TABLE achievements (
    achievementId SERIAL PRIMARY KEY,
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    achievementName TEXT NOT NULL,
    earnedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---
## **6. Sample Queries**

### **Log XP for Completing a Task**

```sql
INSERT INTO xp_log (userId, earnedXP, reason)
VALUES ('USR12345', 50, 'Completed a hard task');
```

### **Update Streak**

```sql
-- Check last activity
UPDATE streaks
SET currentStreak = currentStreak + 1,
    longestStreak = GREATEST(longestStreak, currentStreak),
    lastActivity = CURRENT_DATE
WHERE userId = 'USR12345' AND lastActivity = CURRENT_DATE - 1;
```

### **Unlock Rewards**

```sql
SELECT rewardName
FROM rewards
WHERE price <= (SELECT coins FROM users WHERE userId = 'USR12345')
  AND (SELECT SUM(earnedXP) FROM xp_log WHERE userId = 'USR12345') >= 500;
```

---
## **Usage Scenarios**

1. **Daily Motivation**:
    - Users earn XP and maintain streaks to unlock rewards.
2. **Gamification**:
    - Progress tracking and rank-based rewards encourage consistent engagement.
3. **Flexibility**:
    - Both XP and streaks provide diverse ways for users to earn and track progress.