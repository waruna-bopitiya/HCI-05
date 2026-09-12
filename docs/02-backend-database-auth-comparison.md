# Activity 2 – Backend, Database and Authentication Comparison

## Backend

| Criteria | Node.js / Express | Python / FastAPI | Go (Gin/Fiber) |
|---|---|---|---|
| Performance | Good; event-driven and strong for real-time | Good; ASGI async support | Excellent; compiled and low latency |
| AI/ML Integration | Moderate | Excellent | Limited |
| Real-Time Capability | Excellent | Good | Good |
| Developer Availability | Very large talent pool | Large and growing | Smaller talent pool |
| Ecosystem | Huge npm ecosystem | Rich scientific/AI ecosystem | Smaller ecosystem |
| Cost / Scaling | Low to moderate | Low to moderate | Very efficient resource usage |

**Recommended:** Node.js / NestJS

## Database

| Criteria | PostgreSQL | MongoDB | Firebase / Firestore | DynamoDB |
|---|---|---|---|---|
| Data Model | Relational | Document | Document | Key-value/document |
| Scalability | Strong | Strong horizontal scaling | Managed automatic scaling | Managed automatic scaling |
| Query Performance | Excellent for complex queries and joins | Good for simple document queries | Good for simple real-time operations | Very fast key-based access |
| Health Data Handling | Strong ACID compliance | Flexible but needs consistency care | Convenient but less relational | Strong consistency options |
| Real-Time Support | Usually needs additional mechanisms | Change streams | Built-in listeners | Streams |
| Cost / Maintainability | Predictable managed/self-managed options | Managed options available | Pay-as-you-go | Pay-per-request |

**Recommended:** PostgreSQL

## Authentication

| Criteria | Firebase Auth | AWS Cognito | Auth0 | Supabase Auth |
|---|---|---|---|---|
| Authentication | Email/password, phone, Google, Apple | Password/social/enterprise | Social, passwordless, MFA | Email/password, magic links, social |
| Security | Secure tokens and encryption support | Strong IAM and encryption | MFA and threat detection | JWT + Row-Level Security |
| Authorization | Firebase rules / backend checks | IAM-based access control | Strong RBAC | Role/database security |
| Scalability | Automatic scaling | Enterprise scale | Highly scalable | Good cloud scalability |
| Real-Time Support | Strong with Firebase ecosystem | Needs additional services | Usually external | Supabase Realtime |
| Cost / Maintenance | Low cost, easy maintenance | More complex | Can become expensive | Cost-effective |

**Recommended:** Firebase Authentication
