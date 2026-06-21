# Wealth Management System - Project Plan

## üìã Ringkasan Proyek

**Wealth Management System** adalah aplikasi web untuk manajemen keuangan pribadi yang membantu pengguna mengelola portofolio investasi dan melacak pencapaian tujuan keuangan. Proyek ini dikembangkan sebagai proyek pembelajaran untuk memahami pengembangan aplikasi full-stack modern menggunakan ReactJS, Spring Boot, dan MySQL.

### Informasi Proyek

- **Nama Proyek**: Wealth Management System
- **Tipe**: Learning Project / Educational Application
- **Status**: Phase 1 - Requirements Analysis (Completed)
- **Tanggal Mulai**: 21 Juni 2026
- **Target Completion MVP**: TBD

---

## üéØ Tujuan Pembelajaran

Proyek ini dirancang untuk mencapai tujuan pembelajaran berikut:

### 1. Frontend Development (ReactJS)
- Memahami component-based architecture
- Implementasi state management
- Integrasi dengan REST API
- Data visualization dengan charts
- Form handling dan validation
- Responsive UI design

### 2. Backend Development (Spring Boot)
- RESTful API design dan implementation
- Business logic layer development
- Security implementation (JWT authentication)
- Database interaction dengan JPA/Hibernate
- Service-oriented architecture
- Error handling dan validation

### 3. Database Design (MySQL)
- Relational database schema design
- Data normalization
- Query optimization
- Transaction management
- Data migration strategy

### 4. Full-Stack Integration
- Frontend-backend communication
- API contract management
- Authentication flow
- State synchronization
- Error handling across layers

### 5. Software Development Best Practices
- Clean code principles
- Version control dengan Git
- Project structure organization
- Documentation practices
- Testing strategies
- AI-assisted development dengan OpenCode

---

## üéØ Scope MVP (Minimum Viable Product)

### Fitur yang TERMASUK dalam MVP:

#### 1. User Management (Basic)
- User registration
- User login/logout
- Basic profile management
- Risk profile assessment (simple questionnaire)

#### 2. Portfolio Recommendation
- User input: tujuan keuangan (amount, timeline)
- User input: tingkat toleransi risiko (Low/Medium/High)
- Sistem memberikan rekomendasi portofolio dari 3-5 template pre-defined
- Rekomendasi berdasarkan rules engine sederhana
- Display alokasi aset (e.g., 60% stocks, 40% bonds)

#### 3. Financial Goal Management
- Create financial goal (target amount, target date, category)
- View list of goals
- Update goal progress
- Delete goal

#### 4. Goal Progress Tracking
- Visual progress indicator (progress bar/percentage)
- Status indicator (on track / at risk / off track)
- Basic insights generation:
  - "Target dapat tercapai dalam X bulan"
  - "Tabungan Anda terlalu kecil untuk mencapai target"
  - "Perlu menambah tabungan Rp X per bulan"

#### 5. What-If Simulator
- Simulate perubahan income (increase/decrease)
- Simulate perubahan expenses (increase/decrease)
- Calculate impact terhadap goal achievement timeline
- Display comparison: current vs simulated scenario

#### 6. Dashboard
- Portfolio overview (allocation, value)
- Goals summary (active goals, progress)
- Key metrics display
- Portfolio performance chart (sample data)
- Recent activity/insights

### Success Criteria MVP:
- ‚úÖ User dapat register dan login
- ‚úÖ User dapat complete risk profile assessment
- ‚úÖ User dapat receive portfolio recommendation
- ‚úÖ User dapat create dan track financial goals (minimum 1-3 goals)
- ‚úÖ User dapat view dashboard dengan portfolio dan goals
- ‚úÖ User dapat run What-If simulation
- ‚úÖ System dapat generate basic insights

---

## ‚ùå Fitur yang TIDAK Termasuk MVP

Fitur-fitur berikut akan dikembangkan di fase post-MVP:

### Phase 2+ (Future Enhancements):
- Real-time market data integration
- Multiple portfolios per user
- Portfolio rebalancing recommendations
- Advanced risk metrics (Sharpe ratio, volatility, beta)
- Recurring transactions tracking
- Income/expense management
- Multi-scenario comparison
- Export reports (PDF/Excel)
- Email notifications
- Advanced analytics dashboard
- Mobile responsive optimization
- Multi-currency support
- Social features (portfolio comparison, sharing)
- Machine learning recommendations
- Admin dashboard
- User activity analytics
- API rate limiting
- Advanced security features (2FA, session management)

---

## üó∫Ô∏è Roadmap Pengembangan

### PHASE 0: Environment Setup
**Duration**: 1-2 hari  
**Objective**: Setup development environment dan project structure

**Tasks**:
- [x] Install Java JDK 11+
- [x] Install Node.js dan npm
- [x] Install MySQL 8.0+
- [x] Install IDE (IntelliJ IDEA / VS Code)
- [x] Install Postman untuk API testing
- [ ] Setup Git repository
- [ ] Create project directories
- [ ] Initialize Spring Boot project dengan Maven
- [ ] Initialize React project dengan Create React App
- [ ] Verify all tools installation

**Deliverables**:
- Configured development environment
- Initialized project repositories
- Basic README.md

---

### PHASE 1: Requirements Analysis
**Duration**: 1-2 hari  
**Objective**: Understand dan document project requirements

**Tasks**:
- [x] Analyze functional requirements
- [x] Analyze non-functional requirements
- [x] Identify core modules
- [x] Define MVP scope
- [x] Create project plan document
- [ ] Define user stories
- [ ] Create feature breakdown

**Deliverables**:
- PROJECT_PLAN.md (this document)
- User stories document
- Feature requirements list

---

### PHASE 2: System Design
**Duration**: 2-3 hari  
**Objective**: Design system architecture dan technical specifications

**Tasks**:
- [ ] Design system architecture (high-level)
- [ ] Define API contracts (REST endpoints)
- [ ] Design data flow diagrams
- [ ] Define component hierarchy (React)
- [ ] Design service layer structure (Spring Boot)
- [ ] Define authentication flow
- [ ] Create mockups/wireframes (optional)
- [ ] Design recommendation rules engine
- [ ] Design insights generation logic

**Deliverables**:
- ARCHITECTURE.md
- API_SPECIFICATION.md
- Component design documents
- Wireframes (optional)

---

### PHASE 3: Database Design
**Duration**: 2-3 hari  
**Objective**: Design database schema dan relationships

**Tasks**:
- [ ] Design Entity-Relationship Diagram (ERD)
- [ ] Define database tables dan columns
- [ ] Define relationships dan foreign keys
- [ ] Design indexes untuk performance
- [ ] Create sample data plan
- [ ] Write database migration scripts
- [ ] Document database schema

**Deliverables**:
- DATABASE_DESIGN.md
- ERD diagram
- SQL migration scripts
- Sample data scripts

---

### PHASE 4: Spring Boot Backend Foundation
**Duration**: 5-7 hari  
**Objective**: Build backend core infrastructure

**Tasks**:
- [ ] Setup Spring Boot project structure
- [ ] Configure MySQL connection
- [ ] Setup JPA/Hibernate entities
- [ ] Implement JWT authentication
- [ ] Create User Management APIs
  - POST /api/auth/register
  - POST /api/auth/login
  - GET /api/users/profile
  - PUT /api/users/profile
- [ ] Create exception handling
- [ ] Setup request validation
- [ ] Configure CORS
- [ ] Test APIs dengan Postman
- [ ] Write unit tests

**Deliverables**:
- Working backend authentication system
- User management APIs
- API documentation
- Unit tests

---

### PHASE 5: React Frontend Foundation
**Duration**: 5-7 hari  
**Objective**: Build frontend core infrastructure

**Tasks**:
- [ ] Setup React project structure
- [ ] Configure routing (React Router)
- [ ] Setup state management (Context API / Redux)
- [ ] Create authentication pages
  - Login page
  - Register page
- [ ] Implement authentication flow
- [ ] Create layout components (Header, Footer, Sidebar)
- [ ] Setup API service layer
- [ ] Implement JWT token management
- [ ] Create protected routes
- [ ] Setup error handling
- [ ] Test authentication flow end-to-end

**Deliverables**:
- Working frontend authentication
- Reusable layout components
- API integration layer

---

### PHASE 6: Financial Goal Module
**Duration**: 5-7 hari  
**Objective**: Implement complete goal management feature

**Backend Tasks**:
- [ ] Create Goal entity dan repository
- [ ] Implement Goal Management APIs
  - POST /api/goals (create)
  - GET /api/goals (list)
  - GET /api/goals/{id} (detail)
  - PUT /api/goals/{id} (update)
  - DELETE /api/goals/{id} (delete)
- [ ] Implement goal progress calculation logic
- [ ] Implement insights generation engine
- [ ] Write unit tests

**Frontend Tasks**:
- [ ] Create Goal List page
- [ ] Create Goal Form (Create/Edit)
- [ ] Create Goal Detail view
- [ ] Implement goal progress visualization
- [ ] Display insights
- [ ] Integrate with backend APIs
- [ ] Test CRUD operations

**Deliverables**:
- Working goal management feature
- Progress tracking functionality
- Basic insights generation

---

### PHASE 7: Investment Portfolio Module
**Duration**: 7-10 hari  
**Objective**: Implement portfolio recommendation system

**Backend Tasks**:
- [ ] Create Portfolio entity dan repository
- [ ] Create Asset entity (stocks, bonds, etc.)
- [ ] Implement Risk Profile APIs
  - POST /api/risk-profile (save assessment)
  - GET /api/risk-profile (get current)
- [ ] Implement recommendation rules engine
- [ ] Create Portfolio Recommendation APIs
  - POST /api/portfolio/recommend (get recommendation)
  - POST /api/portfolio/save (save portfolio)
  - GET /api/portfolio (get user portfolio)
- [ ] Create sample market data
- [ ] Implement portfolio value calculation
- [ ] Write unit tests

**Frontend Tasks**:
- [ ] Create Risk Profile Questionnaire
- [ ] Create Portfolio Recommendation page
- [ ] Display portfolio allocation (pie chart)
- [ ] Create Portfolio Detail view
- [ ] Show portfolio composition
- [ ] Integrate with backend APIs
- [ ] Test recommendation flow

**Deliverables**:
- Working risk assessment
- Portfolio recommendation engine
- Portfolio visualization

---

### PHASE 8: Dashboard Module
**Duration**: 5-7 hari  
**Objective**: Create main dashboard dengan overview

**Backend Tasks**:
- [ ] Create Dashboard API
  - GET /api/dashboard/summary (portfolio + goals summary)
  - GET /api/dashboard/portfolio-performance (chart data)
- [ ] Aggregate data dari goals dan portfolio
- [ ] Generate key metrics
- [ ] Write unit tests

**Frontend Tasks**:
- [ ] Create Dashboard layout
- [ ] Implement Portfolio Overview section
- [ ] Implement Goals Summary section
- [ ] Create portfolio performance chart
- [ ] Display key metrics
- [ ] Create recent insights section
- [ ] Integrate with backend APIs
- [ ] Make dashboard responsive

**Deliverables**:
- Complete dashboard page
- Data visualization charts
- Key metrics display

---

### PHASE 9: What-If Simulator
**Duration**: 5-7 hari  
**Objective**: Implement financial scenario simulation

**Backend Tasks**:
- [ ] Create Simulation API
  - POST /api/simulation/goal-impact (calculate impact)
- [ ] Implement simulation calculation logic
  - Income change impact
  - Expense change impact
  - Combined scenarios
- [ ] Calculate new timeline projections
- [ ] Write unit tests

**Frontend Tasks**:
- [ ] Create Simulation page
- [ ] Create input controls (sliders/inputs)
- [ ] Display current scenario
- [ ] Display simulated scenario
- [ ] Show comparison view
- [ ] Create visualization (before/after charts)
- [ ] Integrate with backend API
- [ ] Test various scenarios

**Deliverables**:
- Working What-If simulator
- Scenario comparison functionality
- Impact visualization

---

### PHASE 10: Testing & Polish
**Duration**: 5-7 hari  
**Objective**: Test, fix bugs, dan polish application

**Tasks**:
- [ ] End-to-end testing (manual)
- [ ] Write integration tests (backend)
- [ ] Write component tests (frontend)
- [ ] Fix bugs dan issues
- [ ] Performance optimization
- [ ] UI/UX improvements
- [ ] Code refactoring
- [ ] Documentation updates
- [ ] Security review
- [ ] Prepare deployment configuration
- [ ] Create user guide (optional)

**Deliverables**:
- Tested dan stable MVP
- Bug-free application
- Complete documentation
- Deployment-ready code

---

## ??? Tech Stack

### Frontend
- **Framework**: React 18.x
- **Language**: JavaScript (ES6+) / TypeScript (optional)
- **Routing**: React Router v6
- **State Management**: Context API / Redux Toolkit
- **HTTP Client**: Axios
- **UI Components**: Custom components / Material-UI / Bootstrap (TBD)
- **Charts**: Chart.js / Recharts
- **Form Handling**: React Hook Form (optional)
- **Styling**: CSS Modules / Styled Components / Tailwind (TBD)

### Backend
- **Framework**: Spring Boot 3.x
- **Language**: Java 11+
- **Build Tool**: Maven
- **Security**: Spring Security + JWT
- **ORM**: Spring Data JPA + Hibernate
- **Validation**: Bean Validation (JSR-380)
- **Documentation**: Swagger / SpringDoc OpenAPI (optional)

### Database
- **Database**: MySQL 8.0+
- **Migration**: Flyway / Liquibase (optional)

### Development Tools
- **IDE**: IntelliJ IDEA / VS Code
- **API Testing**: Postman
- **Version Control**: Git + GitHub
- **AI Assistant**: OpenCode

### Testing
- **Backend Testing**: JUnit 5, Mockito, Spring Boot Test
- **Frontend Testing**: Jest, React Testing Library

---

## ??? Struktur Modul Tingkat Tinggi

### Backend Module Structure (Spring Boot)

```
wealth-management-backend/
+-- src/main/java/com/wealthmanagement/
¶   +-- config/                    # Configuration classes
¶   ¶   +-- SecurityConfig.java
¶   ¶   +-- CorsConfig.java
¶   ¶   +-- JwtConfig.java
¶   ¶
¶   +-- controller/                # REST Controllers
¶   ¶   +-- AuthController.java
¶   ¶   +-- UserController.java
¶   ¶   +-- GoalController.java
¶   ¶   +-- PortfolioController.java
¶   ¶   +-- DashboardController.java
¶   ¶   +-- SimulationController.java
¶   ¶
¶   +-- service/                   # Business Logic Layer
¶   ¶   +-- UserService.java
¶   ¶   +-- GoalService.java
¶   ¶   +-- PortfolioService.java
¶   ¶   +-- RecommendationService.java
¶   ¶   +-- InsightsService.java
¶   ¶   +-- SimulationService.java
¶   ¶   +-- DashboardService.java
¶   ¶
¶   +-- repository/                # Data Access Layer
¶   ¶   +-- UserRepository.java
¶   ¶   +-- GoalRepository.java
¶   ¶   +-- PortfolioRepository.java
¶   ¶   +-- AssetRepository.java
¶   ¶   +-- RiskProfileRepository.java
¶   ¶
¶   +-- model/                     # Domain Models
¶   ¶   +-- User.java
¶   ¶   +-- Goal.java
¶   ¶   +-- Portfolio.java
¶   ¶   +-- Asset.java
¶   ¶   +-- RiskProfile.java
¶   ¶
¶   +-- dto/                       # Data Transfer Objects
¶   ¶   +-- request/
¶   ¶   +-- response/
¶   ¶
¶   +-- security/                  # Security Components
¶   ¶   +-- JwtTokenProvider.java
¶   ¶   +-- JwtAuthenticationFilter.java
¶   ¶   +-- UserDetailsServiceImpl.java
¶   ¶
¶   +-- exception/                 # Exception Handling
¶   ¶   +-- GlobalExceptionHandler.java
¶   ¶   +-- CustomExceptions.java
¶   ¶
¶   +-- util/                      # Utility Classes
¶       +-- DateUtil.java
¶       +-- CalculationUtil.java
¶
+-- src/main/resources/
¶   +-- application.properties
¶   +-- application-dev.properties
¶   +-- application-prod.properties
¶
+-- src/test/java/
    +-- (unit tests)
```

### Frontend Module Structure (React)

```
wealth-management-frontend/
+-- public/
¶   +-- index.html
¶
+-- src/
¶   +-- components/               # Reusable Components
¶   ¶   +-- common/
¶   ¶   ¶   +-- Button.jsx
¶   ¶   ¶   +-- Input.jsx
¶   ¶   ¶   +-- Card.jsx
¶   ¶   ¶   +-- Modal.jsx
¶   ¶   ¶
¶   ¶   +-- layout/
¶   ¶   ¶   +-- Header.jsx
¶   ¶   ¶   +-- Sidebar.jsx
¶   ¶   ¶   +-- Footer.jsx
¶   ¶   ¶   +-- Layout.jsx
¶   ¶   ¶
¶   ¶   +-- charts/
¶   ¶   ¶   +-- PieChart.jsx
¶   ¶   ¶   +-- LineChart.jsx
¶   ¶   ¶   +-- ProgressBar.jsx
¶   ¶   ¶
¶   ¶   +-- forms/
¶   ¶       +-- GoalForm.jsx
¶   ¶       +-- RiskProfileForm.jsx
¶   ¶
¶   +-- pages/                    # Page Components
¶   ¶   +-- auth/
¶   ¶   ¶   +-- LoginPage.jsx
¶   ¶   ¶   +-- RegisterPage.jsx
¶   ¶   ¶
¶   ¶   +-- dashboard/
¶   ¶   ¶   +-- DashboardPage.jsx
¶   ¶   ¶
¶   ¶   +-- goals/
¶   ¶   ¶   +-- GoalListPage.jsx
¶   ¶   ¶   +-- GoalDetailPage.jsx
¶   ¶   ¶   +-- CreateGoalPage.jsx
¶   ¶   ¶
¶   ¶   +-- portfolio/
¶   ¶   ¶   +-- PortfolioPage.jsx
¶   ¶   ¶   +-- RecommendationPage.jsx
¶   ¶   ¶
¶   ¶   +-- simulation/
¶   ¶       +-- SimulationPage.jsx
¶   ¶
¶   +-- services/                 # API Services
¶   ¶   +-- api.js
¶   ¶   +-- authService.js
¶   ¶   +-- goalService.js
¶   ¶   +-- portfolioService.js
¶   ¶   +-- simulationService.js
¶   ¶
¶   +-- context/                  # State Management
¶   ¶   +-- AuthContext.jsx
¶   ¶   +-- PortfolioContext.jsx
¶   ¶   +-- GoalContext.jsx
¶   ¶
¶   +-- hooks/                    # Custom Hooks
¶   ¶   +-- useAuth.js
¶   ¶   +-- useApi.js
¶   ¶
¶   +-- utils/                    # Utility Functions
¶   ¶   +-- formatters.js
¶   ¶   +-- validators.js
¶   ¶   +-- constants.js
¶   ¶
¶   +-- routes/                   # Routing
¶   ¶   +-- AppRoutes.jsx
¶   ¶   +-- ProtectedRoute.jsx
¶   ¶
¶   +-- styles/                   # Global Styles
¶   ¶   +-- global.css
¶   ¶
¶   +-- App.jsx
¶   +-- index.js
¶
+-- package.json
```

---

## ?? Risiko Proyek

### Risiko Teknis

| Risiko | Probabilitas | Dampak | Mitigasi |
|--------|--------------|--------|----------|
| Kompleksitas What-If simulation logic | Medium | Medium | Start dengan simple calculation, iterate gradually |
| Performance issues dengan large datasets | Low | Medium | Implement pagination, indexing, lazy loading |
| JWT token management dan security | Medium | High | Follow Spring Security best practices, use proven libraries |
| React state management complexity | Medium | Medium | Start dengan Context API, migrate ke Redux jika perlu |
| Cross-browser compatibility issues | Low | Low | Test di major browsers, use modern React practices |
| Database schema changes during development | High | Medium | Use migration tools (Flyway), maintain version control |

### Risiko Non-Teknis

| Risiko | Probabilitas | Dampak | Mitigasi |
|--------|--------------|--------|----------|
| Scope creep (feature additions) | High | High | Stick to MVP scope, maintain feature backlog |
| Timeline delays | Medium | Medium | Set realistic deadlines, track progress regularly |
| Learning curve untuk new technologies | High | Medium | Allocate learning time, use documentation extensively |
| Lack of testing leading to bugs | Medium | High | Write tests incrementally, don't skip testing phase |
| Poor code quality | Medium | Medium | Follow coding standards, regular code reviews |

### Dependencies & Assumptions

**Assumptions**:
- Development time: 2-3 bulan untuk MVP (part-time learning)
- Single developer project
- No production deployment required initially
- Sample/dummy data acceptable untuk MVP
- Basic UI/UX acceptable (not production-grade design)

**External Dependencies**:
- MySQL database availability
- Java JDK 11+ installed
- Node.js dan npm installed
- Stable internet untuk library downloads

---

## ?? Progress Tracking

### Overall Progress: Phase 1 Completed

| Phase | Status | Completion | Notes |
|-------|--------|------------|-------|
| Phase 0: Environment Setup | ? In Progress | 60% | Core tools installed, project structure pending |
| Phase 1: Requirements Analysis | ? Completed | 100% | Requirements documented |
| Phase 2: System Design | ?? Pending | 0% | - |
| Phase 3: Database Design | ?? Pending | 0% | - |
| Phase 4: Backend Foundation | ?? Pending | 0% | - |
| Phase 5: Frontend Foundation | ?? Pending | 0% | - |
| Phase 6: Financial Goal Module | ?? Pending | 0% | - |
| Phase 7: Portfolio Module | ?? Pending | 0% | - |
| Phase 8: Dashboard Module | ?? Pending | 0% | - |
| Phase 9: What-If Simulator | ?? Pending | 0% | - |
| Phase 10: Testing & Polish | ?? Pending | 0% | - |

### Current Status
- **Current Phase**: Phase 1 (Requirements Analysis) - Completed
- **Next Phase**: Phase 2 (System Design)
- **Last Updated**: 21 Juni 2026
- **Blockers**: None

---

## ?? Dokumentasi Terkait

Dokumen-dokumen yang akan dibuat selama proyek:

1. **PROJECT_PLAN.md** (this document) - Master project plan
2. **ARCHITECTURE.md** - System architecture design
3. **API_SPECIFICATION.md** - REST API documentation
4. **DATABASE_DESIGN.md** - Database schema dan ERD
5. **DEVELOPMENT_GUIDE.md** - Setup dan development instructions
6. **USER_STORIES.md** - Detailed user stories
7. **TESTING_GUIDE.md** - Testing strategy dan test cases
8. **DEPLOYMENT_GUIDE.md** - Deployment instructions (future)

---

## ?? Notes

### Development Principles
- **Keep It Simple**: Focus on MVP scope, avoid over-engineering
- **Incremental Development**: Build features incrementally, test frequently
- **Documentation First**: Document before coding complex features
- **Security First**: Never compromise on security practices
- **Learning Focused**: Prioritize understanding over speed
- **Code Quality**: Write clean, maintainable code

### Next Steps
1. Review dan approve project plan
2. Start Phase 2: System Design
3. Create detailed API specifications
4. Design database schema
5. Setup project repositories

---

**Document Version**: 1.0  
**Last Updated**: 21 Juni 2026  
**Author**: System Architect  
**Status**: Approved ?
