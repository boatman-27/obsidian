---
tags:
  - go
date: 2025-08-03T23:16:00
---
Using the same Service and Controller as [[User Registration and Authentication]].
### View and Edit Profile
- **Get Profile**:
    - `GetUserProfile` retrieves full user details using their `userId`.
    - Returns a sanitized response with personal details.
- **Edit Profile**:
    - `UpdateUser` is used to update profile fields like `name`, `email`, and `phone_number`.
    - Passwords are hashed before being stored.
    - If email changes, new tokens are generated.
    - The `updatedat` field is automatically set to the current timestamp.
