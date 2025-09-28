---
tags:
  - backend
  - ts
date: 2025-09-28T12:56:00
---
# PenguinAPI Backend
A comprehensive REST API providing detailed information about penguin species, facts, and analytics. Built with TypeScript, Express, Prisma ORM, and PostgreSQL.

## Table of Contents
- [Features](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#features)
- [Tech Stack](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#tech-stack)
- [Getting Started](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#getting-started)
- [Environment Variables](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#environment-variables)
- [Database Schema](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#database-schema)
- [API Routes](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#api-routes)
- [Authentication](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#authentication)
- [Error Handling](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#error-handling)
- [Usage Analytics](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#usage-analytics)
- [Email Services](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#email-services)
- [Development](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#development)
- [Deployment](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#deployment)

## Features
- **Comprehensive Penguin Data**: Species information, distribution, diet, migration patterns
- **Random Penguin Facts**: Curated facts with sources
- **User Management**: Registration, authentication, API key management
- **Usage Analytics**: Detailed tracking and reporting of API usage
- **Rate Limiting**: Per-key rate limiting with customizable tiers
- **Email Notifications**: Welcome emails, password resets, API key delivery
- **Geographic Filtering**: Species data by region, breeding months, conservation status
- **Flexible Authentication**: Support for both JWT tokens and API keys

## Tech Stack
- **Runtime**: Bun
- **Framework**: Express.js
- **Language**: TypeScript
- **Database**: PostgreSQL (Supabase)
- **ORM**: Prisma
- **Authentication**: JWT + API Key
- **Email**: Resend
- **Password Hashing**: bcrypt
- **Validation**: Custom error classes

## Getting Started

### Prerequisites

- Bun (latest version)
- PostgreSQL database (Supabase recommended)
- Resend account for email services

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd penguin-api
```

2. Install dependencies:
```bash
bun install
```

3. Set up environment variables (see [Environment Variables](https://claude.ai/chat/0c673241-088c-43e9-86b8-30348544a956#environment-variables))
4. Set up the database:

```bash
bunx prisma migrate dev
bunx prisma db seed
```

5. Start the development server:

```bash
bun run dev
```

The server will start on `http://localhost:3000` (or your specified PORT).

## Environment Variables

Create a `.env` file in the root directory:

```env
# Database
DATABASE_URL="postgresql://username:password@host:port/database"
DIRECT_URL="postgresql://username:password@host:port/database"

# JWT
ACCESS_SECRET="your-jwt-secret-key"

# Email Service
RESEND_API_KEY="your-resend-api-key"

# Frontend URL (for email links)
FRONTEND_URL="http://localhost:3000"

# Server
PORT=3000
```

## Database Schema

### Core Models

#### Users

- User accounts with authentication
- Links to API keys and usage analytics
- Password reset functionality

#### ApiKey

- API key management with hashing and lookup
- Rate limiting per key
- Usage tracking and statistics

#### Species

- Comprehensive penguin species data
- Physical characteristics, conservation status
- Related distribution, diet, and migration data

#### Facts

- Curated penguin facts with sources
- Used for random fact endpoints

#### Analytics Models

- ApiUsage: Detailed request logging
- Geographic and endpoint usage tracking

## API Routes

### Public Endpoints

#### Authentication

```
POST /auth/register          # User registration
POST /auth/login            # User login
POST /auth/forgot-password  # Password reset request
POST /auth/reset-password   # Complete password reset
```

#### Public Data

```
GET /public/facts/sample    # Sample facts (no auth required)
GET /public/pricing        # Pricing tier information
GET /public/food           # Available food types
GET /public/regions        # Available regions
GET /public/conservations  # Conservation statuses
```

#### Facts (API Key Required)

```
GET /v1/facts              # Get fact by ID
GET /v1/facts/random       # Random fact (no auth)
GET /v1/facts/search       # Search facts
```

#### Species (Public)

```
GET /v1/species/full                    # All species data
GET /v1/species/summary                 # Species summaries
GET /v1/species/breeding-month          # Filter by breeding month
GET /v1/species/diet                    # Filter by diet
GET /v1/species/seasonal-diet           # Seasonal diet data
GET /v1/species/region                  # Filter by region
GET /v1/species/status                  # Filter by conservation status
GET /v1/species/min-weight              # Minimum weight filter
GET /v1/species/max-weight              # Maximum weight filter
GET /v1/species/range-weight            # Weight range filter
GET /v1/species/min-population          # Minimum population filter
GET /v1/species/max-population          # Maximum population filter
GET /v1/species/range-population        # Population range filter
```

### Protected Endpoints (JWT Required)

#### User Management

```
GET /public/keys           # Get user's API keys
POST /public/keys          # Generate new API key
PATCH /public/keys         # Rename API key
DELETE /public/keys        # Delete API key
```

#### Analytics

```
GET /analytics/overview           # Usage overview
GET /analytics/usage             # Usage analytics
GET /analytics/keys              # Key usage stats
GET /analytics/endpoints         # Endpoint statistics
GET /analytics/status-codes      # Status code distribution
GET /analytics/geographic        # Geographic usage
GET /analytics/errors            # Error analysis
GET /analytics/report            # Comprehensive report
GET /analytics/dashboard-data    # Public dashboard data
```

## Authentication

### JWT Authentication

For user-specific operations, include the JWT token in the Authorization header:

```
Authorization: Bearer <jwt-token>
```

### API Key Authentication

For API endpoints, include your API key in the header:

```
x-api-key: <your-api-key>
```

### Flexible Authentication

Some endpoints support both authentication methods. The middleware checks for API key first, then falls back to JWT.

## Error Handling

The API uses custom error classes for consistent error responses:

- `ValidationError` (400): Invalid input data
- `AuthenticationError` (401): Invalid credentials or tokens
- `AuthorizationError` (403): Insufficient permissions
- `NotFoundError` (404): Resource not found
- `ConflictError` (409): Resource conflicts (e.g., email already exists)
- `RateLimitError` (429): Rate limit exceeded
- `InternalServerError` (500): Server errors

### Error Response Format

```json
{
  "success": false,
  "error": {
    "name": "ValidationError",
    "message": "Invalid email format",
    "status": 400
  }
}
```

## Usage Analytics

The system provides comprehensive analytics for API usage:

### Tracked Metrics

- Request counts and success rates
- Endpoint usage statistics
- Geographic usage patterns
- Status code distributions
- Error analysis and rates
- API key performance metrics

### Analytics Features

- Daily usage tracking
- Rate limit utilization
- User-specific analytics
- Public dashboard metrics
- Comprehensive reporting

## Email Services

Powered by Resend for reliable email delivery:

### Email Types

- **Welcome Email**: Sent after successful registration with API key
- **Password Reset**: Secure password reset with time-limited tokens
- **API Key Delivery**: New API key notifications
- **Verification Email**: Email address verification (if implemented)

### Email Configuration

- Custom HTML templates with inline CSS
- Responsive design for mobile compatibility
- Branded styling with PenguinAPI theme
- Proper error handling and logging

## Development

### Project Structure

```
penguin-api/
├── src/
│   ├── controllers/     # Request handlers
│   ├── services/        # Business logic
│   ├── middleware/      # Auth, validation, logging
│   ├── routes/          # Route definitions
│   ├── types/           # TypeScript types and errors
│   ├── utils/           # Helper functions and services
│   └── generated/       # Prisma client
├── prisma/
│   ├── schema.prisma    # Database schema
│   └── seed.ts          # Database seeding
└── package.json
```

### Development Commands

```bash
bun run dev              # Start development server
bunx prisma studio       # Open database browser
bunx prisma migrate dev  # Run database migrations
bunx prisma db seed      # Seed database with sample data
bunx prisma generate     # Generate Prisma client
```

### Code Style

- TypeScript with strict mode enabled
- Class-based architecture for services and controllers
- Custom error handling with proper HTTP status codes
- Comprehensive input validation
- Async/await for database operations

## Security Features

### Password Security

- bcrypt hashing with 12 rounds
- Password strength validation
- Common password detection
- Secure password reset flow

### API Key Security

- SHA256 hashing for database lookups
- bcrypt verification for additional security
- Rate limiting per key
- Usage tracking and monitoring

### General Security

- Helmet.js for security headers
- CORS configuration
- Input validation and sanitization
- SQL injection protection via Prisma
- Error message sanitization

## Deployment

### Environment Setup

1. Set up production database (Supabase recommended)
2. Configure environment variables for production
3. Set up Resend for email delivery
4. Configure frontend URL for email links

### Database Migration

```bash
bunx prisma migrate deploy
bunx prisma db seed
```

### Production Considerations

- Enable database connection pooling
- Set up proper logging and monitoring
- Configure rate limiting for production loads
- Set up SSL/TLS certificates
- Enable database backups

## API Response Formats

### Success Response

```json
{
  "success": true,
  "data": {
    // Response data
  },
  "metadata": {
    "count": 10,
    "page": 1,
    "totalPages": 5
  }
}
```

### Error Response

```json
{
  "success": false,
  "error": {
    "name": "ValidationError",
    "message": "Description of the error",
    "status": 400
  }
}
```

## Rate Limiting

- Default: 1000 requests per day per API key
- Configurable per pricing tier
- Automatic reset at midnight
- Usage tracking and notifications
- Graceful error handling when limits exceeded

## Contributing

1. Follow TypeScript best practices
2. Use the existing error handling patterns
3. Add proper input validation
4. Include comprehensive logging
5. Update documentation for new endpoints
6. Test authentication and authorization flows

## License

[Add your license information here]

## Support

For questions or support, please contact [your-contact-information].