# ADR-001 – FitFlow Technology Stack

## Status
Accepted

## Context
FitFlow requires Android, iOS, and web support, real-time functionality, structured health/fitness data, secure authentication, and AI-powered recommendations.

## Decision
Use:
- React Native + React Native Web
- Node.js / NestJS
- Python / FastAPI
- PostgreSQL
- Firebase Authentication

## Rationale
The selected stack provides a strong balance of performance, scalability, development speed, security, cost, AI/ML support, real-time capability, and maintainability.

## Consequences

### Positive
- High frontend code reuse
- Strong backend real-time support
- Reliable relational data handling
- Easy-to-integrate authentication
- Strong Python AI/ML ecosystem

### Trade-offs
- Multiple technology ecosystems must be maintained
- Some React Native features may require native modules
- Firebase introduces an external-service dependency
- AI and backend services require clearly defined APIs
