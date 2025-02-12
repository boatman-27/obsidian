# **Customization Documentation**

## **Overview**
The customization feature allows users to personalize their experience through:  
1. **Themes**: Modify the app's visual appearance.  
2. **Avatars**: Represent the user with customizable profile icons.  

---
## **1. Themes**

### **Theme Options**
Users can choose from a variety of themes to suit their preferences.  
- **Default Themes** (Available to all users):  
  - Light Theme  
  - Dark Theme  
  
- **Unlockable Themes** (Require specific progress):  
  - Solarized Theme (Unlock at Intermediate Rank)  
  - Neon Glow Theme (Unlock at Advanced Rank)  
  - Cosmic Theme (Unlock at Expert Rank)  

### **Theme Settings**
- **Customization Options**:  
  - Primary and secondary colors.  
  - Font styles (limited to system fonts for performance).  
  - Background patterns or solid colors.  

### **Database Schema**
```sql
CREATE TABLE themes (
    themeId SERIAL PRIMARY KEY,
    themeName TEXT NOT NULL UNIQUE,
    isUnlocked BOOLEAN DEFAULT FALSE,
    requiredRank TEXT CHECK (requiredRank IN ('Beginner', 'Intermediate', 'Advanced', 'Expert')) DEFAULT 'Beginner'
);

CREATE TABLE user_themes (
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    themeId INT NOT NULL REFERENCES themes(themeId),
    PRIMARY KEY (userId, themeId)
);
```
### **User Interaction**
- **Default Theme**: Automatically assigned to new users.
- **Unlock Themes**: Themes are unlocked based on rank and added to the user's theme list.
- **Theme Selection**: Users can switch between unlocked themes via the **Settings Menu**.

---
## **2. Avatars**

### **Avatar Options**
Users can select and customize their avatars to reflect their personality.
#### **Base Avatars**:
- Circle
- Square
- Animal
- Abstract
#### **Customizable Features**:
- **Color Palette**: Change skin, hair, and clothing colors.
- **Accessories**: Add hats, glasses, etc.
- **Expressions**: Choose from happy, neutral, or excited expressions.
### **Unlockable Avatars**
- Avatars can be unlocked through milestones or purchases in the shop.
    - Example:
        - "Robot Avatar" unlocks at 500 XP.
        - "Golden Crown Accessory" is purchasable for 100 coins.
### **Database Schema**
```sql
CREATE TABLE avatars (
    avatarId SERIAL PRIMARY KEY,
    avatarName TEXT NOT NULL UNIQUE,
    isUnlocked BOOLEAN DEFAULT FALSE,
    requiredXP INT DEFAULT 0,
    price INT DEFAULT NULL CHECK (price >= 0)
);

CREATE TABLE user_avatars (
    userId VARCHAR(8) NOT NULL REFERENCES users(userId),
    avatarId INT NOT NULL REFERENCES avatars(avatarId),
    PRIMARY KEY (userId, avatarId)
);
```
### **User Interaction**
- **Default Avatar**: New users start with a basic avatar.
- **Customization Options**: Users can access the avatar editor to modify colors, expressions, and accessories.
- **Shop Integration**: Unlockable avatars and accessories can be purchased in the **Generic Shop** using coins.

---
## **3. Progress-Based Unlocks**
Both themes and avatars are tied to the progress system:

- Ranks unlock specific themes.
- XP milestones unlock exclusive avatars.

|**Unlock Type**|**Requirement**|**Reward**|
|---|---|---|
|Theme Unlock|Reach "Advanced Rank"|Cosmic Theme|
|Avatar Unlock|Earn 500 XP|Robot Avatar|
|Accessory Purchase|Buy with 100 coins|Golden Crown|

---
## **4. Future Enhancements**
1. **Dynamic Themes**: Allow users to upload custom background images.
2. **Animated Avatars**: Introduce animated accessories or effects for avatars.
3. **Seasonal Themes**: Add themes for holidays or special events (e.g., Halloween, New Year).
4. **Avatar Sharing**: Allow users to share their customized avatars with friends.

---

## **Sample Queries**

### **Unlock a Theme**

```sql
INSERT INTO user_themes (userId, themeId)
SELECT 'USR12345', themeId FROM themes WHERE themeName = 'Solarized Theme';
```

### **Unlock an Avatar**

```sql
INSERT INTO user_avatars (userId, avatarId)
SELECT 'USR12345', avatarId FROM avatars WHERE avatarName = 'Robot Avatar';
```

### **Purchase an Accessory**

```sql
UPDATE users
SET coins = coins - 100
WHERE userId = 'USR12345' AND coins >= 100;

INSERT INTO user_avatars (userId, avatarId)
SELECT 'USR12345', avatarId FROM avatars WHERE avatarName = 'Golden Crown';
```

---
## **5. User Interface**

### **Theme Customization**
- **Preview Panel**: Show live previews of themes.
- **Apply Button**: Confirm the selection to save changes.

### **Avatar Editor**
- **Drag-and-Drop Interface**: Users can drag accessories onto their avatar.
- **Color Picker**: Interactive tool to modify avatar colors.
- **Save Changes**: Updates the user's profile with the customized avatar.
