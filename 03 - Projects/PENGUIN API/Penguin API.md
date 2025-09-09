# 🐧 Penguin Facts API - Your First SaaS Project

A simple SaaS API to learn the fundamentals before building complex systems. This project teaches you hosting, billing, API design, and customer management without overwhelming complexity.

## 🎯 Why This Project?

**Learn SaaS Basics:**

- API design and versioning
- Authentication with API keys
- Usage tracking and rate limiting
- Simple subscription billing
- Customer management
- Hosting and deployment

**Skills You'll Gain:**

- TypeScript/Node.js API development
- Database design and management
- Stripe billing integration
- API documentation
- Error handling and validation
- Deployment and monitoring

## 🏗️ Project Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   API Gateway   │    │  Rate Limiter   │    │   Auth Layer    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
         ┌───────────────────────▼───────────────────────┐
         │           Express.js Application              │
         └───────────────────────┬───────────────────────┘
                                 │
    ┌────────────────────────────┼────────────────────────────┐
    │                            │                            │
┌───▼────┐              ┌───────▼────────┐           ┌──────▼──────┐
│PostgreSQL│              │     Redis      │           │   Stripe    │
│- Facts   │              │   (Rate Limit, │           │    API      │
│- Users   │              │   Cache)       │           │             │
│- Usage   │              │                │           │             │
└──────────┘              └────────────────┘           └─────────────┘
```

## 🌟 Features

### Core API Features

- **Random penguin facts** with categories
- **Species-specific facts** (Emperor, Adelie, etc.)
- **Fact categories** (habitat, diet, behavior, conservation)
- **Image URLs** for penguin species
- **Difficulty levels** (kids, general, scientific)

### SaaS Features

- **API key authentication**
- **Usage tracking and analytics**
- **Rate limiting** (free vs paid tiers)
- **Simple billing** with Stripe
- **Customer dashboard**
- **API documentation** with examples

### Business Model

```typescript
const PRICING_TIERS = {
  FREE: {
    price: 0,
    requests_per_day: 100,
    requests_per_minute: 10,
    features: ['basic_facts', 'random_facts']
  },
  BASIC: {
    price: 5, // per month
    requests_per_day: 10000,
    requests_per_minute: 100,
    features: ['basic_facts', 'random_facts', 'species_facts', 'images']
  },
  PRO: {
    price: 15,
    requests_per_day: 100000,
    requests_per_minute: 1000,
    features: ['all_features', 'premium_facts', 'bulk_endpoints', 'analytics']
  }
};
```

## 📊 Database Schema

```sql
-- Users (your SaaS customers - developers)
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  company VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- API Keys for authentication
CREATE TABLE api_keys (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  key_hash VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(100) NOT NULL,
  last_used_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  is_active BOOLEAN DEFAULT true
);

-- Subscriptions
CREATE TABLE subscriptions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  stripe_customer_id VARCHAR(255),
  stripe_subscription_id VARCHAR(255),
  plan VARCHAR(50) NOT NULL DEFAULT 'FREE',
  status VARCHAR(50) NOT NULL DEFAULT 'active',
  current_period_start TIMESTAMP,
  current_period_end TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

-- Usage tracking
CREATE TABLE api_usage (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  api_key_id UUID REFERENCES api_keys(id) ON DELETE CASCADE,
  endpoint VARCHAR(100) NOT NULL,
  method VARCHAR(10) NOT NULL,
  response_time_ms INTEGER,
  status_code INTEGER,
  requested_at TIMESTAMP DEFAULT NOW(),
  date DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Penguin facts data
CREATE TABLE penguin_facts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  fact TEXT NOT NULL,
  species VARCHAR(100), -- 'emperor', 'adelie', 'chinstrap', etc.
  category VARCHAR(100), -- 'habitat', 'diet', 'behavior', 'conservation'
  difficulty VARCHAR(50) DEFAULT 'general', -- 'kids', 'general', 'scientific'
  image_url TEXT,
  source VARCHAR(255),
  created_at TIMESTAMP DEFAULT NOW()
);

-- Daily usage summary for quick lookups
CREATE TABLE daily_usage_summary (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  date DATE NOT NULL,
  total_requests INTEGER DEFAULT 0,
  successful_requests INTEGER DEFAULT 0,
  failed_requests INTEGER DEFAULT 0,
  PRIMARY KEY (user_id, date)
);
```

## 🚀 API Endpoints

### Public Endpoints (No Auth)

```typescript
GET  /api/v1/facts/sample        // 3 sample facts (for demos)
POST /auth/register              // Developer registration
POST /auth/login                 // Developer login
GET  /docs                       // API documentation
GET  /pricing                    // Pricing information
```

### Authenticated Endpoints (Require API Key)

```typescript
// Core penguin facts
GET  /api/v1/facts/random                    // Random fact
GET  /api/v1/facts/random/:count             // Multiple random facts
GET  /api/v1/facts/species/:species          // Species-specific facts
GET  /api/v1/facts/category/:category        // Facts by category
GET  /api/v1/facts/difficulty/:level         // Facts by difficulty

// Advanced features (paid plans only)
GET  /api/v1/facts/bulk                      // Bulk fact retrieval
GET  /api/v1/species                         // List all species
GET  /api/v1/categories                      // List all categories
GET  /api/v1/facts/:id                       // Specific fact by ID
```

### Customer Dashboard API

```typescript
GET  /api/dashboard/usage                    // Usage statistics
GET  /api/dashboard/api-keys                 // List API keys
POST /api/dashboard/api-keys                 // Create new API key
DELETE /api/dashboard/api-keys/:id           // Delete API key
GET  /api/dashboard/subscription             // Current subscription
POST /api/dashboard/subscription/upgrade     // Upgrade subscription
POST /api/dashboard/subscription/cancel      // Cancel subscription
```

## 💻 Implementation Example

### Basic Express Setup

```typescript
import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import { authenticateApiKey } from './middleware/auth';
import { trackUsage } from './middleware/usage';
import { factsRouter } from './routes/facts';

const app = express();

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: 'Too many requests, please try again later'
});
app.use('/api', limiter);

// Routes
app.use('/api/v1/facts', authenticateApiKey, trackUsage, factsRouter);
app.use('/auth', authRouter);
app.use('/api/dashboard', authenticateUser, dashboardRouter);

export default app;
```

### Facts Controller Example

```typescript
export class FactsController {
  
  static async getRandomFact(req: Request, res: Response) {
    try {
      const { difficulty, category, species } = req.query;
      
      const fact = await FactsService.getRandomFact({
        difficulty: difficulty as string,
        category: category as string,
        species: species as string
      });
      
      if (!fact) {
        return res.status(404).json({
          error: 'No facts found matching criteria'
        });
      }
      
      res.json({
        success: true,
        data: {
          id: fact.id,
          fact: fact.fact,
          species: fact.species,
          category: fact.category,
          difficulty: fact.difficulty,
          image_url: fact.image_url
        }
      });
      
    } catch (error) {
      res.status(500).json({
        error: 'Internal server error'
      });
    }
  }
  
  static async getFactsBySpecies(req: Request, res: Response) {
    try {
      const { species } = req.params;
      const { limit = 10, offset = 0 } = req.query;
      
      const facts = await FactsService.getFactsBySpecies(
        species, 
        parseInt(limit as string), 
        parseInt(offset as string)
      );
      
      res.json({
        success: true,
        data: facts,
        pagination: {
          limit: parseInt(limit as string),
          offset: parseInt(offset as string),
          total: facts.length
        }
      });
      
    } catch (error) {
      res.status(500).json({
        error: 'Internal server error'
      });
    }
  }
}
```

### Authentication Middleware

```typescript
export async function authenticateApiKey(req: Request, res: Response, next: NextFunction) {
  try {
    const authHeader = req.headers.authorization;
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return res.status(401).json({
        error: 'Missing or invalid API key'
      });
    }
    
    const apiKey = authHeader.substring(7); // Remove 'Bearer '
    const keyHash = crypto.createHash('sha256').update(apiKey).digest('hex');
    
    const apiKeyRecord = await prisma.apiKey.findFirst({
      where: {
        key_hash: keyHash,
        is_active: true
      },
      include: {
        user: {
          include: {
            subscriptions: {
              where: {
                status: 'active'
              }
            }
          }
        }
      }
    });
    
    if (!apiKeyRecord) {
      return res.status(401).json({
        error: 'Invalid API key'
      });
    }
    
    // Check rate limits based on subscription plan
    const subscription = apiKeyRecord.user.subscriptions[0];
    const plan = subscription?.plan || 'FREE';
    const rateLimitPassed = await checkRateLimit(apiKeyRecord.user.id, plan);
    
    if (!rateLimitPassed) {
      return res.status(429).json({
        error: 'Rate limit exceeded',
        message: 'Upgrade your plan for higher limits'
      });
    }
    
    // Add user and subscription info to request
    req.user = apiKeyRecord.user;
    req.subscription = subscription;
    req.apiKey = apiKeyRecord;
    
    // Update last used timestamp
    await prisma.apiKey.update({
      where: { id: apiKeyRecord.id },
      data: { last_used_at: new Date() }
    });
    
    next();
  } catch (error) {
    res.status(500).json({
      error: 'Authentication failed'
    });
  }
}
```

## 📈 Usage Tracking & Analytics

```typescript
export async function trackUsage(req: Request, res: Response, next: NextFunction) {
  const startTime = Date.now();
  
  // Override res.json to capture response
  const originalJson = res.json;
  res.json = function(data) {
    const responseTime = Date.now() - startTime;
    
    // Log the API usage
    prisma.apiUsage.create({
      data: {
        user_id: req.user.id,
        api_key_id: req.apiKey.id,
        endpoint: req.path,
        method: req.method,
        response_time_ms: responseTime,
        status_code: res.statusCode,
        requested_at: new Date()
      }
    }).catch(console.error); // Don't block response for logging errors
    
    return originalJson.call(this, data);
  };
  
  next();
}
```

## 💳 Simple Billing Integration

```typescript
// Stripe webhook handler
app.post('/webhooks/stripe', express.raw({type: 'application/json'}), async (req, res) => {
  const sig = req.headers['stripe-signature'];
  let event;
  
  try {
    event = stripe.webhooks.constructEvent(req.body, sig, process.env.STRIPE_WEBHOOK_SECRET);
  } catch (err) {
    return res.status(400).send(`Webhook signature verification failed.`);
  }
  
  switch (event.type) {
    case 'customer.subscription.created':
    case 'customer.subscription.updated':
      await handleSubscriptionUpdate(event.data.object);
      break;
      
    case 'customer.subscription.deleted':
      await handleSubscriptionCancellation(event.data.object);
      break;
      
    case 'invoice.payment_succeeded':
      await handleSuccessfulPayment(event.data.object);
      break;
      
    case 'invoice.payment_failed':
      await handleFailedPayment(event.data.object);
      break;
  }
  
  res.json({received: true});
});
```

## 🎨 Customer Dashboard (Optional Frontend)

Simple React dashboard for customers to:

- View API usage statistics
- Manage API keys
- Upgrade/downgrade subscriptions
- View documentation and examples

## 📦 Sample Data

```typescript
const sampleFacts = [
  {
    fact: "Emperor penguins can dive up to 500 meters deep and hold their breath for over 20 minutes.",
    species: "emperor",
    category: "behavior",
    difficulty: "general",
    image_url: "https://example.com/emperor-penguin.jpg"
  },
  {
    fact: "Penguins have a special gland above their eyes that filters salt from seawater.",
    species: null, // applies to all penguins
    category: "anatomy",
    difficulty: "scientific"
  },
  {
    fact: "Baby penguins are called chicks and they're super fluffy!",
    species: null,
    category: "general",
    difficulty: "kids"
  }
];
```

## 🚢 Deployment & Hosting

### Simple Deployment Options:

1. **Heroku** (easiest for beginners)
2. **Railway** (modern alternative)
3. **DigitalOcean App Platform**
4. **AWS Elastic Beanstalk**

```bash 
docker run --name penguin \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=Ao260221_@ \
  -e POSTGRES_DB=penguin \
  -p 5432:5432 \
  -d postgres

```

### Environment Variables:

```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/penguin_facts"

# Redis (for rate limiting)
REDIS_URL="redis://localhost:6379"

# JWT for customer dashboard
JWT_SECRET="your-jwt-secret"

# Stripe
STRIPE_SECRET_KEY="sk_test_..."
STRIPE_WEBHOOK_SECRET="whsec_..."

# App
NODE_ENV="production"
PORT=3000
API_BASE_URL="https://your-penguin-api.com"
```

## 🎯 Learning Outcomes

After building this project, you'll understand:

### SaaS Fundamentals

- API-first product design
- Customer onboarding and management
- Usage-based billing models
- Rate limiting and quotas

### Technical Skills

- RESTful API design
- Database modeling for SaaS
- Authentication and authorization
- Payment processing integration
- API documentation

### Business Understanding

- SaaS pricing strategies
- Customer analytics and metrics
- Product positioning and marketing
- Developer experience (DX) design

## 🔄 Next Steps

Once you master this simple SaaS:
1. **Add complexity gradually:**
    - Webhook system for real-time updates
    - Multiple API versions (v1, v2)
    - Advanced analytics and reporting
2. **Scale the concept:**
    - Add more animal fact APIs
    - Build an "Animal Facts Platform"
    - Create SDKs for popular languages
3. **Apply learnings to auth SaaS:**
    - Multi-tenant architecture
    - Complex permissions and roles
    - Enterprise features

