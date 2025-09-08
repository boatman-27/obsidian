---
tags:
  - backend
date: 2025-09-07T14:09:00
link: https://www.prisma.io/docs/getting-started/setup-prisma/start-from-scratch/relational-databases-typescript-postgresql
---
## Table of Contents

- [Installation & Setup](#installation--setup)
- [Prisma CLI Commands](#prisma-cli-commands)
- [Schema Definition](#schema-definition)
- [Data Types](#data-types)
- [Relations](#relations)
- [CRUD Operations](#crud-operations)
- [Advanced Queries](#advanced-queries)
- [Transactions](#transactions)
- [Migrations](#migrations)
- [Best Practices](#best-practices)

## Installation & Setup

### Install Prisma

```bash
# Install Prisma CLI
npm install -g prisma

# Install Prisma Client
npm install @prisma/client

# Install Prisma CLI as dev dependency
npm install prisma --save-dev
```

### Initialize Prisma

```bash
# Initialize Prisma in your project
npx prisma init

# Initialize with specific database
npx prisma init --datasource-provider postgresql
npx prisma init --datasource-provider mysql
npx prisma init --datasource-provider sqlite
```

## Prisma CLI Commands

### Core Commands

```bash
# Generate Prisma Client
npx prisma generate

# Push schema to database (for development)
npx prisma db push

# Create and apply migrations
npx prisma migrate dev --name init

# Apply pending migrations (production)
npx prisma migrate deploy

# Reset database (development only)
npx prisma migrate reset

# View database in browser
npx prisma studio

# Format schema file
npx prisma format

# Validate schema
npx prisma validate

# Introspect existing database
npx prisma db pull

# Seed database
npx prisma db seed
```

### Migration Commands

```bash
# Create new migration
npx prisma migrate dev --name add-user-table

# Deploy migrations to production
npx prisma migrate deploy

# Check migration status
npx prisma migrate status

# Reset migrations (development)
npx prisma migrate reset
```

## Schema Definition

### Basic Schema Structure

```prisma
// prisma/schema.prisma

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql" // or "mysql", "sqlite", "sqlserver", "mongodb"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  email     String   @unique
  name      String?
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  posts     Post[]
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  authorId  Int
  author    User     @relation(fields: [authorId], references: [id])
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

## Data Types

### Scalar Types

#### String Types

```prisma
model User {
  email    String   @unique
  name     String?  // Optional
  bio      String   @db.Text // Large text
  slug     String   @db.VarChar(50) // Limited length
}
```

#### Numeric Types

```prisma
model Product {
  id       Int     @id @default(autoincrement())
  price    Float   // Decimal numbers
  quantity Int     @default(0)
  rating   Decimal @db.Decimal(3, 2) // Precise decimals
  bigNum   BigInt  // Large integers
}
```

#### Boolean and Date Types

```prisma
model User {
  isActive  Boolean  @default(true)
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
  birthDate DateTime?
}
```

#### JSON and Bytes

```prisma
model Settings {
  id       Int  @id @default(autoincrement())
  config   Json // JSON data
  avatar   Bytes? // Binary data
}
```

### Enums

```prisma
enum Role {
  USER
  ADMIN
  MODERATOR
}

enum Status {
  DRAFT
  PUBLISHED
  ARCHIVED
}

model User {
  id   Int  @id @default(autoincrement())
  role Role @default(USER)
}
```

### Arrays (PostgreSQL)

```prisma
model User {
  id   Int      @id @default(autoincrement())
  tags String[] // Array of strings
}
```

## Relations

### One-to-One

```prisma
model User {
  id      Int      @id @default(autoincrement())
  profile Profile?
}

model Profile {
  id     Int  @id @default(autoincrement())
  userId Int  @unique
  user   User @relation(fields: [userId], references: [id])
}
```

### One-to-Many

```prisma
model User {
  id    Int    @id @default(autoincrement())
  posts Post[]
}

model Post {
  id       Int  @id @default(autoincrement())
  authorId Int
  author   User @relation(fields: [authorId], references: [id])
}
```

### Many-to-Many (Explicit)

```prisma
model User {
  id           Int            @id @default(autoincrement())
  userCategories UserCategory[]
}

model Category {
  id           Int            @id @default(autoincrement())
  userCategories UserCategory[]
}

model UserCategory {
  userId     Int
  categoryId Int
  user       User     @relation(fields: [userId], references: [id])
  category   Category @relation(fields: [categoryId], references: [id])
  assignedAt DateTime @default(now())

  @@id([userId, categoryId])
}
```

### Many-to-Many (Implicit)

```prisma
model User {
  id         Int        @id @default(autoincrement())
  categories Category[]
}

model Category {
  id    Int    @id @default(autoincrement())
  users User[]
}
```

### Self Relations

```prisma
model User {
  id       Int    @id @default(autoincrement())
  managerId Int?
  manager  User?  @relation("UserManager", fields: [managerId], references: [id])
  reports  User[] @relation("UserManager")
}
```

## CRUD Operations

### Setup Prisma Client

```javascript
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()
```

### Create Operations

```javascript
// Create single record
const user = await prisma.user.create({
  data: {
    email: 'john@example.com',
    name: 'John Doe',
    posts: {
      create: [
        { title: 'First Post', content: 'Hello World' },
        { title: 'Second Post', content: 'Another post' }
      ]
    }
  },
  include: {
    posts: true
  }
})

// Create many records
const users = await prisma.user.createMany({
  data: [
    { email: 'user1@example.com', name: 'User 1' },
    { email: 'user2@example.com', name: 'User 2' }
  ]
})

// Upsert (create or update)
const user = await prisma.user.upsert({
  where: { email: 'john@example.com' },
  update: { name: 'John Updated' },
  create: { email: 'john@example.com', name: 'John Doe' }
})
```

### Read Operations

```javascript
// Find unique
const user = await prisma.user.findUnique({
  where: { id: 1 },
  include: { posts: true }
})

// Find first
const user = await prisma.user.findFirst({
  where: { email: { contains: '@gmail.com' } }
})

// Find many
const users = await prisma.user.findMany({
  where: {
    posts: {
      some: {
        published: true
      }
    }
  },
  orderBy: { createdAt: 'desc' },
  take: 10,
  skip: 20
})

// Count records
const userCount = await prisma.user.count({
  where: { posts: { some: { published: true } } }
})

// Aggregate
const result = await prisma.user.aggregate({
  _count: { id: true },
  _avg: { age: true },
  _sum: { age: true },
  _min: { age: true },
  _max: { age: true }
})
```

### Update Operations

```javascript
// Update single record
const user = await prisma.user.update({
  where: { id: 1 },
  data: { 
    name: 'Updated Name',
    posts: {
      updateMany: {
        where: { published: false },
        data: { published: true }
      }
    }
  }
})

// Update many records
const updateResult = await prisma.user.updateMany({
  where: { role: 'USER' },
  data: { role: 'MEMBER' }
})
```

### Delete Operations

```javascript
// Delete single record
const deletedUser = await prisma.user.delete({
  where: { id: 1 }
})

// Delete many records
const deleteResult = await prisma.user.deleteMany({
  where: { role: 'INACTIVE' }
})
```

## Advanced Queries

### Filtering

```javascript
// Basic filters
const users = await prisma.user.findMany({
  where: {
    name: { contains: 'John' },
    email: { endsWith: '@gmail.com' },
    age: { gte: 18, lte: 65 },
    role: { in: ['USER', 'ADMIN'] },
    posts: { 
      some: { 
        title: { contains: 'Prisma' },
        published: true 
      }
    }
  }
})

// Complex filters with AND/OR
const users = await prisma.user.findMany({
  where: {
    OR: [
      { name: { contains: 'John' } },
      { email: { contains: 'admin' } }
    ],
    AND: [
      { age: { gte: 18 } },
      { isActive: true }
    ]
  }
})
```

### Selecting Fields

```javascript
// Select specific fields
const users = await prisma.user.findMany({
  select: {
    id: true,
    name: true,
    email: true,
    posts: {
      select: {
        title: true,
        published: true
      }
    }
  }
})
```

### Including Relations

```javascript
const user = await prisma.user.findUnique({
  where: { id: 1 },
  include: {
    posts: {
      where: { published: true },
      orderBy: { createdAt: 'desc' }
    },
    profile: true
  }
})
```

### Pagination

```javascript
// Cursor-based pagination
const posts = await prisma.post.findMany({
  take: 10,
  cursor: { id: lastPostId },
  skip: 1, // Skip the cursor
  orderBy: { id: 'asc' }
})

// Offset pagination
const posts = await prisma.post.findMany({
  skip: 20,
  take: 10,
  orderBy: { createdAt: 'desc' }
})
```

### Sorting

```javascript
const users = await prisma.user.findMany({
  orderBy: [
    { role: 'asc' },
    { createdAt: 'desc' },
    { posts: { _count: 'desc' } } // Sort by relation count
  ]
})
```

## Transactions

### Sequential Transactions

```javascript
const [updatedUser, newPost] = await prisma.$transaction([
  prisma.user.update({
    where: { id: 1 },
    data: { name: 'Updated Name' }
  }),
  prisma.post.create({
    data: {
      title: 'New Post',
      authorId: 1
    }
  })
])
```

### Interactive Transactions

```javascript
const result = await prisma.$transaction(async (tx) => {
  // Transfer money between accounts
  const sender = await tx.account.update({
    where: { id: senderId },
    data: { balance: { decrement: amount } }
  })

  if (sender.balance < 0) {
    throw new Error('Insufficient funds')
  }

  const receiver = await tx.account.update({
    where: { id: receiverId },
    data: { balance: { increment: amount } }
  })

  return { sender, receiver }
})
```

### Transaction Options

```javascript
const result = await prisma.$transaction(
  [
    prisma.user.create({ data: { email: 'test@example.com' } }),
    prisma.post.create({ data: { title: 'Test Post' } })
  ],
  {
    isolationLevel: 'Serializable',
    maxWait: 5000,
    timeout: 10000
  }
)
```

## Migrations

### Development Workflow

```bash
# 1. Update schema.prisma
# 2. Create and apply migration
npx prisma migrate dev --name add-user-profile

# 3. Generate client
npx prisma generate
```

### Production Deployment

```bash
# Deploy migrations to production
npx prisma migrate deploy
```

### Custom Migration SQL

```sql
-- migrations/20231201120000_custom_changes/migration.sql

-- Custom SQL that Prisma can't generate
CREATE INDEX CONCURRENTLY idx_user_email_active ON "User" (email) WHERE active = true;

-- Add custom function
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';
```

### Seeding Database

```javascript
// prisma/seed.js
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  const alice = await prisma.user.upsert({
    where: { email: 'alice@example.com' },
    update: {},
    create: {
      email: 'alice@example.com',
      name: 'Alice',
      posts: {
        create: {
          title: 'Check out Prisma with Next.js',
          content: 'https://www.prisma.io/nextjs',
          published: true,
        },
      },
    },
  })
}

main()
  .catch((e) => {
    console.error(e)
    process.exit(1)
  })
  .finally(async () => {
    await prisma.$disconnect()
  })
```

```json
// package.json
{
  "prisma": {
    "seed": "node prisma/seed.js"
  }
}
```

## Best Practices

### Connection Management

```javascript
// Single instance pattern
// lib/prisma.js
import { PrismaClient } from '@prisma/client'

const globalForPrisma = globalThis

export const prisma = globalForPrisma.prisma || new PrismaClient()

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
```

### Error Handling

```javascript
import { PrismaClientKnownRequestError } from '@prisma/client/runtime/library'

try {
  const user = await prisma.user.create({
    data: { email: 'existing@example.com' }
  })
} catch (error) {
  if (error instanceof PrismaClientKnownRequestError) {
    if (error.code === 'P2002') {
      // Unique constraint violation
      throw new Error('User with this email already exists')
    }
  }
  throw error
}
```

### Schema Best Practices

```prisma
model User {
  id        String   @id @default(cuid()) // Better than autoincrement
  email     String   @unique @db.VarChar(255)
  name      String?  @db.VarChar(100)
  createdAt DateTime @default(now()) @db.Timestamptz
  updatedAt DateTime @updatedAt @db.Timestamptz
  
  // Add indexes for performance
  @@index([email])
  @@index([createdAt])
}
```

### Performance Optimization

```javascript
// Use select/include wisely
const users = await prisma.user.findMany({
  select: {
    id: true,
    name: true,
    _count: {
      select: { posts: true }
    }
  }
})

// Use raw queries for complex operations
const result = await prisma.$queryRaw`
  SELECT u.name, COUNT(p.id) as post_count
  FROM "User" u
  LEFT JOIN "Post" p ON u.id = p."authorId"
  GROUP BY u.id, u.name
  HAVING COUNT(p.id) > 5
`
```

### Environment Configuration

```env
# .env
DATABASE_URL="postgresql://username:password@localhost:5432/mydb?schema=public"

# For connection pooling
DATABASE_URL="postgresql://username:password@localhost:5432/mydb?schema=public&connection_limit=5&pool_timeout=20"
```

### Type Safety

```typescript
// Use Prisma's generated types
import { User, Post, Prisma } from '@prisma/client'

// Type for user with posts
type UserWithPosts = Prisma.UserGetPayload<{
  include: { posts: true }
}>

// Type for creating a user
type CreateUserInput = Prisma.UserCreateInput
```

This guide covers the essential aspects of working with Prisma. Keep it handy as a reference for your development work!