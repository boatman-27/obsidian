# **Rewards System Documentation**

## **Overview**
The rewards system is a gamified feature that allows users to redeem coins earned from completing tasks. Users can spend these coins in two shops:  
1. **Developer-Created Shop**: Offers predefined rewards curated by the developer.  
2. **User-Created Shop**: Enables users to create and customize their own rewards.  

This system incentivises task completion by providing tangible and customisable rewards.

---

## **Database Schema**

### **Rewards Table**
The `rewards` table stores all rewards, whether developer-created or user-created.

#### **Table Definition**
```sql
CREATE TABLE rewards (
    rewardId SERIAL PRIMARY KEY,
    rewardName TEXT NOT NULL,
    createdBy TEXT NOT NULL CHECK (createdBy IN ('developer', 'user')),
    userId VARCHAR(8) REFERENCES users(userId),
    price INT NOT NULL CHECK (price > 0),
    category TEXT DEFAULT 'General',
    description TEXT,
    addedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```


---

### **Column Descriptions**

|**Column**|**Type**|**Description**|
|---|---|---|
|`rewardId`|`SERIAL`|Unique identifier for each reward.|
|`rewardName`|`TEXT`|Name of the reward.|
|`createdBy`|`TEXT`|Specifies whether the reward was created by the developer or the user.|
|`userId`|`VARCHAR(8)`|References the `users` table. For developer-created rewards, this value is `NULL`.|
|`price`|`INT`|Coin cost of the reward. Must be greater than 0.|
|`category`|`TEXT`|Category of the reward. Defaults to `General`.|
|`description`|`TEXT`|Optional description providing details about the reward.|
|`addedOn`|`TIMESTAMP`|Timestamp of when the reward was added. Defaults to the current timestamp.|

---

## **Features**

### **1. Developer-Created Shop**

- The developer-curated shop offers fixed rewards that cannot be modified or removed by users.
- Rewards are categorized into groups such as `Entertainment`, `Productivity`, and `Relaxation`.
- Examples of rewards include:
    - Virtual movie tickets
    - Break vouchers
    - App subscriptions (e.g., 1-month premium access)

#### **Logistics**

- Developer-created rewards will always have `createdBy = 'developer'`.
- These rewards are global and visible to all users.
- Users can only redeem rewards if they have enough coins.

---

### **2. User-Created Shop**

- Users can create and manage their own rewards, making the system more personalized.
- Custom rewards are tied to individual users and are not shared globally.
- Examples of custom rewards include:
    - “1 hour of gaming” for 50 coins
    - “Buy a coffee” for 100 coins

#### **Logistics**

- User-created rewards will have `createdBy = 'user'` and must be linked to a valid `userId`.
- Users can update or delete their custom rewards at any time.
- Validation ensures that all rewards have a positive price.

---

### **3. Redeeming Rewards**

- Users can redeem rewards using coins, provided they have enough balance.
- After redemption, the user's coin balance is updated, and the redeemed reward is logged in the `redemptions` table.

#### **Redemptions Table**

```sql 
CREATE TABLE redemptions (
    redemptionId SERIAL PRIMARY KEY,
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    rewardId INT NOT NULL REFERENCES rewards(rewardId),
    redeemedOn TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
#### **Redemption Process**

1. Check if the user has sufficient coins for the reward.
2. Deduct the coin cost from the user's balance.
3. Add an entry to the `redemptions` table.

---

### **4. Reward Categories**

Both developer and user rewards can be categorized for better organization.  
Example categories:

- Entertainment
- Productivity
- Relaxation
- Custom (user-specific rewards)

---

### **5. Reward Filtering**

Users can filter rewards by:

- **Price Range**: Find rewards within a specific coin range.
- **Category**: Filter by categories such as `Entertainment` or `Custom`.
- **Creator**: View rewards by `developer` or `user`.

---

## **Sample Queries**

### **Adding a Developer Reward**

```sql
INSERT INTO rewards (rewardName, createdBy, price, category, description)
VALUES ('1 Hour Break', 'developer', 50, 'Relaxation', 'Take a one-hour break to recharge.');

```

### **Adding a User-Created Reward**

```sql
INSERT INTO rewards (rewardName, createdBy, userId, price, category, description)
VALUES ('Buy a Coffee', 'user', 'USR12345', 100, 'Custom', 'Use 100 coins to treat yourself to coffee.');
```
### **Redeeming a Reward**
```sql
-- Deduct coins from user
UPDATE users
SET coins = coins - 50
WHERE userId = 'USR12345';

-- Log redemption
INSERT INTO redemptions (userId, rewardId)
VALUES ('USR12345', 1);

```
### **Querying Available Rewards**

```sql
SELECT * FROM rewards
WHERE price <= 50
  AND category = 'Relaxation';

```

---

## **Constraints**

### **Database Constraints**

1. **Price**:
    - Rewards must have a positive price.
2. **Creator**:
    - `createdBy` must be either `developer` or `user`.
3. **Category**:
    - Categories can be custom, but defaults to `General`.
4. **Foreign Key**:
    - User-created rewards must reference a valid `userId`.

### **Business Logic**

- Users cannot redeem rewards if they lack sufficient coins.
- Developer rewards cannot be modified or deleted by users.
- User-created rewards are private and not visible to others.

---

## **Future Enhancements**

1. **Limited-Time Rewards**:
    - Add a `validUntil` column to rewards to create exclusive, time-sensitive rewards.
2. **Reward Bundles**:
    - Allow users to purchase multiple rewards at a discounted price.
3. **Reward Sharing**:
    - Enable users to share custom rewards with friends or groups.
4. **Reward Analytics**:
    - Provide users with insights into their most redeemed reward categories.

---

## **Usage Scenarios**

1. **Motivation**:
    - Users are motivated to complete tasks to earn coins and redeem exciting rewards.
2. **Customization**:
    - User-created rewards make the system more personal and meaningful.
3. **Gamification**:
    - The two-shop system adds variety, encouraging both casual and frequent use.

---

## **Sample Data**

### **Rewards Table**

| **Reward ID** | **Name**     | **Created By** | **Price** | **Category** | **Description**                    |
| ------------- | ------------ | -------------- | --------- | ------------ | ---------------------------------- |
| 1             | 1 Hour Break | Developer      | 50        | Relaxation   | Take a one-hour break to recharge. |
| 2             | Buy a Coffee | User           | 100       | Custom       | Treat yourself to coffee.          |

### **Redemptions Table**

| **Redemption ID** | **User ID** | **Reward ID** | **Redeemed On**     |
| ----------------- | ----------- | ------------- | ------------------- |
| 1                 | USR12345    | 2             | 2025-01-26 14:30:00 |