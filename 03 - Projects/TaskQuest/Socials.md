# **Socials Documentation**

## **Overview**
The Socials feature allows users to interact with others, compete for rankings, and collaborate through challenges. It includes:  
1. **Friends**: Build a network of friends to share progress and achievements.  
2. **Leaderboard**: Compete with others globally or within your friends' circle.  
3. **Custom Challenges**: Create and participate in challenges with unique rewards.

---

## **1. Friends**

### **Features**
- **Add Friends**: Send friend requests to connect with others.  
- **Friend List**: View and manage your list of friends.  
- **Activity Feed**: Track friends’ activities, such as completed tasks or milestones reached.  

### **Database Schema**
```sql
CREATE TABLE friends (
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    friendId VARCHAR(8) NOT NULL REFERENCES users(userId),
    status TEXT NOT NULL CHECK (status IN ('pending', 'accepted', 'rejected')),
    requestedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId, friendId)
);
```

### **User Interaction**
- **Send Request**: Add a friend by entering their username or user ID.
- **Accept/Reject Requests**: Manage incoming friend requests.
- **Remove Friend**: Remove connections if needed.

---
## **2. Leaderboard**

### **Features**

- **Global Leaderboard**: Displays top users based on XP or tasks completed.
- **Friends Leaderboard**: Shows rankings within the user’s friends' circle.
- **Category-Specific Rankings**: Users can view rankings for:
    - Total XP
    - Streak Count
    - Coins Earned

### **Database Schema**
```sql
CREATE TABLE leaderboard (
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    xp INT NOT NULL,
    streak INT NOT NULL,
    coinsEarned INT NOT NULL,
    lastUpdated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (userId)
);
```

### **User Interaction**
- **View Rankings**: Access leaderboards through the dashboard.
- **Filters**: Sort by XP, streak, or coins earned.
- **Rank Rewards**: Periodic rewards for top-ranked users (e.g., bonus coins or exclusive items).

---

## **3. Custom Challenges**

### **Features**
- **Create Challenges**: Users can define challenges with specific tasks and deadlines.
- **Join Challenges**: Friends or public users can join open challenges.
- **Challenge Types**:
    - Task-Based: Complete a set number of tasks.
    - XP-Based: Earn a target amount of XP within a timeframe.
    - Time-Limited: Achieve milestones before the deadline.

### **Database Schema**
```sql
CREATE TABLE challenges (
    challengeId SERIAL PRIMARY KEY,
    challengeName TEXT NOT NULL,
    createdBy VARCHAR(8) NOT NULL REFERENCES users(userId),
    challengeType TEXT NOT NULL CHECK (challengeType IN ('task', 'xp', 'time-limited')),
    target INT NOT NULL,
    deadline TIMESTAMP NOT NULL,
    reward INT NOT NULL,
    createdOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE challenge_participants (
    challengeId INT NOT NULL REFERENCES challenges(challengeId),
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    progress INT DEFAULT 0,
    isCompleted BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (challengeId, userId)
);
```

### **User Interaction**

- **Challenge Creation**:
    - Define the challenge type, target, deadline, and reward.
    - Invite friends or open the challenge to the public.
- **Joining Challenges**:
    - Users can browse and join available challenges.
    - Track progress in the challenge dashboard.
- **Rewards**:
    - Coins, XP, or exclusive items are distributed upon challenge completion.

---
## **4. Progress Integration**

The Socials feature integrates seamlessly with the Progress system:
- **Friends XP Boost**: Completing tasks with friends may grant a small XP bonus.
- **Leaderboard Ranks**: Updated dynamically as users progress in tasks and streaks.
- **Challenge Completion**: Contributes to XP and coin totals, influencing leaderboard rankings.

---
## **5. Future Enhancements**

1. **Real-Time Leaderboards**: Live updates for rankings during competitive events.
2. **Social Badges**: Earn badges for activities like hosting the most challenges or having the longest streak.
3. **Group Challenges**: Allow teams to compete against each other.
4. **Activity Analytics**: Provide users with insights into their performance compared to friends.
5. **Cross-Platform Sharing**: Enable users to share their progress and achievements on social media platforms.

---
## **Sample Queries**

### **Add a Friend**
```sql
INSERT INTO friends (userId, friendId, status) VALUES ('USR12345', 'USR67890', 'pending');
```

### **Update Leaderboard**

```sql
INSERT INTO leaderboard (userId, xp, streak, coinsEarned) 
VALUES ('USR12345', 500, 10, 250) 
ON CONFLICT (userId) 
DO UPDATE SET xp = EXCLUDED.xp, streak = EXCLUDED.streak, coinsEarned = EXCLUDED.coinsEarned;
```


### **Create a Challenge**

```sql
INSERT INTO challenges (challengeName, createdBy, challengeType, target, deadline, reward) 
VALUES ('Weekly XP Sprint', 'USR12345', 'xp', 500, '2025-02-01 23:59:59', 100);
```

### **Join a Challenge**

``` sql
INSERT INTO challenge_participants (challengeId, userId) VALUES (1, 'USR67890');
```

### **Track Challenge Progress**

```sql
UPDATE challenge_participants 
SET progress = progress + 50 
WHERE challengeId = 1 AND userId = 'USR67890';
```