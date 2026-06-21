# Architecture & Project Decisions Log

## 📋 Overview

This document records all significant architectural and project decisions made during the Wealth Management System development. Each decision includes the context, rationale, alternatives considered, and implications.

**Recording Period**: Phase 0-1 (21 Juni 2026)  
**Decision Framework**: Architecture Decision Records (ADR)

---

## Decision 1: MVP Scope - Lean Feature Set

**Date**: 21 Juni 2026  
**Category**: Project Scope  
**Status**: ✅ **APPROVED**

### Context
The project is a learning initiative with 2-3 month timeline. Need to balance comprehensive features with delivery feasibility and learning objectives.

### Decision
**Adopt a lean MVP with exactly 8 core features** instead of including advanced features like real-time data, ML recommendations, or social features.

### Features Included:
1. User authentication
2. Risk profile assessment
3. Portfolio recommendation (pre-defined templates)
4. Financial goal management
5. Goal progress tracking
6. Basic insights generation
7. What-If simulation (single scenario)
8. Dashboard overview

### Features Excluded from MVP:
- Real-time market data
- Multiple portfolios per user
- Advanced risk metrics (Sharpe ratio, volatility)
- Email notifications
- Mobile app
- Admin dashboard
- Machine learning recommendations

### Rationale
- **Speed to MVP**: Focus on core flows reduces development time
- **Learning Value**: Master fundamentals before advanced concepts
- **Quality**: Fewer features = more thorough testing and polishing
- **Scope Control**: Prevents scope creep and ensures completion
- **Future Extensibility**: Clean design allows easy feature additions

### Alternatives Considered
1. ❌ **Full-featured MVP**: Would require 4-6 months, too long for learning project
2. ❌ **Minimal MVP**: Only authentication + goals; lacks investment portfolio aspect
3. ✅ **Lean MVP (Chosen)**: Balanced scope, achievable timeline, good learning value

### Implications
- **Trade-off**: Some advanced features postponed to Phase 2+
- **Quality Focus**: More time for testing and refinement
- **User Feedback**: Can validate core concept before adding features
- **Extension Path**: Clear roadmap for future enhancements

### Related Decisions
- Decision 2 (Tech Stack) supports this decision
- Decision 5 (State Management) influenced by scope

---

## Decision 2: Tech Stack Selection

**Date**: 21 Juni 2026  
**Category**: Technology Selection  
**Status**: ✅ **APPROVED**

### Frontend: React 18 + Context API

**Decision**: Use React 18 with Context API for state management (initial approach)

**Rationale**:
- React dominance in modern web development
- Component-based architecture aligns with project structure
- Context API sufficient for MVP (can migrate to Redux later)
- Large community and abundant learning resources
- Virtual DOM ensures good performance

**Alternatives**:
- ❌ Vue.js: Smaller ecosystem for this project scale
- ❌ Angular: Overkill complexity for MVP
- ❌ Redux immediately: Unnecessary complexity for MVP scope

**Implications**:
- Must learn React hooks (modern approach)
- Can easily upgrade to Redux if needed
- Component reusability becomes critical

---

### Backend: Spring Boot 3 + JWT + JPA

**Decision**: Use Spring Boot 3.x with JWT authentication and Spring Data JPA

**Rationale**:
- Spring Boot industry standard for enterprise Java
- Excellent ecosystem for rapid development
- JPA/Hibernate abstracts database complexity
- Spring Security provides robust authentication/authorization
- Well-suited for REST API development

**Alternatives**:
- ❌ Node.js/Express: Different tech stack, adds complexity
- ❌ Python/Django: Overkill for this scale
- ✅ Spring Boot 3 (Chosen): Perfect for learning Java ecosystem

**Implications**:
- Must learn Spring Boot conventions and annotations
- JPA/Hibernate learning curve
- Access to entire Spring ecosystem (security, testing, etc.)

---

### Database: MySQL 8.0+

**Decision**: Use MySQL 8.0+ (relational database)

**Rationale**:
- Relational model fits financial data perfectly
- MySQL industry standard for web applications
- Native support for transactions (important for financial data)
- Wide hosting support (future deployment)
- Good learning value for database design

**Alternatives**:
- ❌ NoSQL (MongoDB): Poor fit for structured financial data
- ❌ PostgreSQL: More advanced, but MySQL sufficient for MVP
- ✅ MySQL 8.0+ (Chosen): Good balance of capability and simplicity

**Implications**:
- Must design normalized schema in Phase 3
- ACID compliance ensures data integrity
- Need for proper indexing strategy

---

## Decision 3: Module Architecture - Layered 3-Tier

**Date**: 21 Juni 2026  
**Category**: Architecture Pattern  
**Status**: ✅ **APPROVED**

### Decision
Adopt **Layered 3-Tier Architecture**:
- **Presentation Layer**: React frontend components
- **Business Logic Layer**: Spring Boot services
- **Data Access Layer**: Spring Data JPA repositories

### Rationale
- Clear separation of concerns
- Each layer has single responsibility
- Standard pattern for web applications
- Facilitates testing at each layer
- Team scalability (multiple developers on different layers)

### Alternatives Considered
- ❌ Monolithic structure: Would mix concerns
- ❌ Microservices: Overkill for MVP, adds operational complexity
- ✅ Layered 3-Tier (Chosen): Perfect balance for learning project

### Implications
- Must maintain clear API boundaries between layers
- Each layer has distinct responsibilities
- Testing strategy varies by layer (unit, integration, e2e)

---

## Decision 4: Authentication Method - JWT Tokens

**Date**: 21 Juni 2026  
**Category**: Security  
**Status**: ✅ **APPROVED**

### Decision
Use **JWT (JSON Web Tokens)** for stateless authentication instead of session-based approach.

### Rationale
- **Stateless**: Server doesn't maintain session state (easier to scale)
- **RESTful**: Natural fit for REST API architecture
- **Token-based**: Supports future mobile app development
- **Security**: Can include claims and validation
- **Modern Standard**: Industry best practice for APIs

### Implementation Details
- Tokens signed with HS256 (HMAC SHA-256)
- Token expiry: 24 hours (configurable)
- Refresh token strategy: TBD in Phase 2

### Alternatives Considered
- ❌ Session-based: Couples frontend to server, harder to scale
- ❌ OAuth/OpenID: Overkill for MVP, adds external dependency
- ✅ JWT (Chosen): Perfect for stateless REST API

### Implications
- Frontend must store and send token with each request
- Must implement token refresh strategy
- Secure token storage important (localStorage vs secure cookie)

---

## Decision 5: State Management - Context API Initial

**Date**: 21 Juni 2026  
**Category**: Frontend Architecture  
**Status**: ✅ **APPROVED**

### Decision
Start with **React Context API** for state management, with clear upgrade path to Redux if needed.

### Rationale
- Sufficient for MVP complexity
- No external dependency overhead
- Good learning opportunity for Context/hooks
- Can migrate to Redux later without major refactoring
- Smaller bundle size initially

### Upgrade Path
If state complexity increases:
1. Identify global state (user, portfolio, goals)
2. Create Redux store incrementally
3. Migrate contexts to Redux reducers one by one

### Alternatives Considered
- ❌ Redux immediately: Unnecessary complexity for MVP
- ❌ MobX: Less common in learning context
- ✅ Context API (Chosen): Right tool for current scope

### Implications
- Context API usage documented in components
- Clear prop drilling rules to prevent deep nesting
- Redux migration path documented

---

## Decision 6: Recommendation Engine - Rules-Based

**Date**: 21 Juni 2026  
**Category**: Business Logic  
**Status**: ✅ **APPROVED**

### Decision
Implement **rules-based recommendation engine** (simple if-then rules) instead of statistical models or ML.

### Rules Structure
**Risk Profile → Portfolio Template Mapping**:
- Low Risk: 70% bonds, 20% stocks, 10% cash
- Medium Risk: 50% stocks, 40% bonds, 10% cash
- High Risk: 80% stocks, 15% bonds, 5% cash

**Modifiers**:
- Investment timeline: Adjust conservativeness based on years-to-goal
- Goal type: Different templates for retirement vs education vs emergency

### Rationale
- **Simplicity**: Easy to implement and understand
- **Transparency**: Users understand why they got this recommendation
- **Maintainability**: Rules easily modified without model retraining
- **Learning Value**: Focus on logic, not ML complexity
- **Extensibility**: Can add more sophisticated logic later

### Future Enhancement
Phase 2+ can upgrade to:
- Statistical models
- Machine learning (collaborative filtering)
- Backtesting results

### Alternatives Considered
- ❌ ML/Statistical models: Overkill for MVP, requires data science expertise
- ❌ Random recommendations: Unrealistic
- ✅ Rules-based (Chosen): Perfect for MVP with clear learning progression

### Implications
- Rules must be documented and testable
- Easy to validate against financial best practices
- Clear audit trail for recommendations

---

## Decision 7: Insights Generation - Template-Based Messages

**Date**: 21 Juni 2026  
**Category**: Business Logic  
**Status**: ✅ **APPROVED**

### Decision
Use **message templates with calculated parameters** for insights instead of NLP/AI-generated messages.

### Insight Categories
1. **Goal Achievability**:
   - Template: "Target dapat tercapai dalam {months} bulan"
   - Calculation: (target_amount - current_saved) / monthly_savings_rate

2. **Savings Adequacy**:
   - Template: "Perlu menambah tabungan Rp {amount} per bulan"
   - Calculation: target_savings_rate - actual_savings_rate

3. **Risk Assessment**:
   - Template: "Goal ini {status}" (on track / at risk / off track)
   - Calculation: Compare progress % vs time elapsed %

### Rationale
- **Clarity**: Consistent, understandable messages
- **Predictability**: No variability in message quality
- **Maintainability**: Simple to add new insight types
- **Testing**: Easy to validate correctness
- **Localization**: Easy to translate to different languages

### Alternatives Considered
- ❌ AI-generated (NLP): Complex, unpredictable output
- ❌ Simple numeric output: Lacks user-friendly interpretation
- ✅ Template-based (Chosen): Best balance of simplicity and usefulness

### Implications
- Message templates maintained in configuration
- Clear calculation logic documented
- Threshold values defined (e.g., "at risk" threshold)

---

## Decision 8: Sample Data Strategy - Static Mock Data

**Date**: 21 Juni 2026  
**Category**: Data Management  
**Status**: ✅ **APPROVED**

### Decision
Use **static seed data** for portfolio performance and market data instead of live API integration.

### Data Scope
- Pre-defined assets (stocks, bonds, funds)
- Static historical prices (month historical trend)
- Seed portfolios for demonstration
- Sample user accounts for testing

### Rationale
- **Focus on Core**: Avoids dependency on external APIs
- **Reliability**: No API outages affecting learning project
- **Simplicity**: No rate limiting or authentication headaches
- **Testing**: Reproducible scenarios
- **Phase Plan**: Real data integration can be Phase 2+ feature

### Data Refresh Strategy
- Manual refresh: Admin updates seed data periodically
- Version control: Data definitions in Git
- Documentation: Clear seed data specifications

### Alternatives Considered
- ❌ Live API (Alpha Vantage, IEX Cloud): Adds complexity, requires API key management
- ❌ No data: Can't demonstrate key features
- ✅ Static mock data (Chosen): Perfect for MVP learning

### Implications
- Data seed scripts required in Phase 3
- Realistic data values important for demo purposes
- Documentation of data assumptions needed

---

## Decision 9: Testing Strategy - Test Pyramid Approach

**Date**: 21 Juni 2026  
**Category**: Quality Assurance  
**Status**: ✅ **APPROVED**

### Decision
Follow **Test Pyramid** with majority unit tests, fewer integration tests, minimal E2E tests.

### Distribution Target
- 70% Unit Tests (individual components/services)
- 20% Integration Tests (layer-to-layer interaction)
- 10% E2E Tests (full user workflows)

### Backend Testing
- JUnit 5 for unit tests
- Mockito for mocking dependencies
- Spring Boot Test for integration tests

### Frontend Testing
- Jest for unit tests
- React Testing Library for component tests
- Manual E2E testing initially

### Rationale
- **Speed**: Unit tests run fast (quick feedback)
- **Reliability**: Fewer flaky tests
- **Cost**: E2E tests expensive to maintain
- **Learning**: Focus on testable design

### Alternatives Considered
- ❌ All E2E: Slow, flaky, expensive to maintain
- ❌ No tests: Risky, poor learning value
- ✅ Test Pyramid (Chosen): Optimal balance

### Implications
- Must write testable code from start
- Clear unit test coverage requirements
- Test documentation needed

---

## Decision 10: Documentation Approach - Markdown in Git

**Date**: 21 Juni 2026  
**Category**: Documentation  
**Status**: ✅ **APPROVED**

### Decision
Store all project documentation as **Markdown files in Git repository** under `docs/` directory.

### Documentation Structure
```
docs/
├── PROJECT_PLAN.md          # Master project blueprint
├── ARCHITECTURE.md          # System design (Phase 2)
├── API_SPECIFICATION.md     # REST API details (Phase 2)
├── DATABASE_DESIGN.md       # Schema and ERD (Phase 3)
├── USER_STORIES.md          # Feature specifications
└── DEVELOPMENT_GUIDE.md     # Setup instructions
```

### Rationale
- **Version Control**: Track changes, revert if needed
- **Collaboration**: Easy to review and comment
- **Accessibility**: Plain text, readable everywhere
- **Simplicity**: No special tools required
- **Portability**: Works everywhere Git is available

### Alternatives Considered
- ❌ Wiki (Confluence, GitHub Wiki): Separate from code, sync issues
- ❌ Google Docs: Not in version control
- ✅ Markdown in Git (Chosen): Best for technical teams

### Implications
- Documentation kept up-to-date with code
- Clear commit messages for documentation changes
- Code review includes documentation review

---

## Summary Table

| # | Decision | Chosen | Status |
|---|----------|--------|--------|
| 1 | MVP Scope | Lean (8 features) | ✅ Approved |
| 2a | Frontend | React 18 + Context API | ✅ Approved |
| 2b | Backend | Spring Boot 3 + JWT | ✅ Approved |
| 2c | Database | MySQL 8.0+ | ✅ Approved |
| 3 | Architecture | 3-Tier Layered | ✅ Approved |
| 4 | Authentication | JWT Tokens | ✅ Approved |
| 5 | State Management | Context API (V1) | ✅ Approved |
| 6 | Recommendations | Rules-Based Engine | ✅ Approved |
| 7 | Insights | Template-Based Messages | ✅ Approved |
| 8 | Sample Data | Static Mock Data | ✅ Approved |
| 9 | Testing | Test Pyramid (70-20-10) | ✅ Approved |
| 10 | Documentation | Markdown in Git | ✅ Approved |

---

## Future Decision Points

These decisions will be made in upcoming phases:

### Phase 2 - System Design:
- [ ] UI Component Library (Material-UI, Bootstrap, Tailwind)
- [ ] Chart library (Chart.js, Recharts, Victory)
- [ ] Error handling and logging strategy
- [ ] CORS policy definition
- [ ] API versioning strategy

### Phase 3 - Database Design:
- [ ] Database indexing strategy
- [ ] Backup and recovery procedure
- [ ] Data migration approach
- [ ] Audit logging requirements

### Phase 4+ - Implementation:
- [ ] Deployment platform (Heroku, AWS, Azure, DigitalOcean)
- [ ] CI/CD pipeline tools (GitHub Actions, Jenkins)
- [ ] Monitoring and logging tools
- [ ] Production security hardening

---

**Document Version**: 1.0  
**Last Updated**: 21 Juni 2026, 15:36  
**Decision Framework**: Architecture Decision Records (ADR)  
**Next Review**: End of Phase 2
