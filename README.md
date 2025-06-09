## Project Overview

PricePulse helps savvy shoppers and deal-hunters stay ahead of price drops on their favorite products. Users register, add product URLs along with target price thresholds, and let PricePulse do the rest:

- Continuously scrape hundreds of online retailers’ product pages  
- Store full price history for trend analysis  
- Notify users immediately when their target price is reached (email, WebSocket, SMS, push)  
- Offer dashboard and exportable reports

---

## Core Features

1. **User Management & Security**  
   - FastAPI-powered REST API with JWT authentication  
   - Email confirmation, password reset workflows  
   - Role-based access control (user, admin)

2. **Product Tracking**  
   - Add/remove product by URL and target price  
   - Track multiple price tiers (e.g. 10%, 20%, 30% drop)  
   - Auto-detect currency, region, and stock status  

3. **Asynchronous Data Collection**  
   - `httpx` + `BeautifulSoup` for non-blocking scraping  
   - Redis-backed task queues (RQ) with retry/backoff policies  
   - Parallel scraping with adjustable concurrency limits

4. **Price History & Analytics**  
   - PostgreSQL + SQLModel: normalized schema for users, products, and timestamped price records  
   - REST endpoints to fetch min/max/average prices over custom intervals  
   - Export CSV/JSON/Excel reports

5. **Multichannel Notifications**  
   - **Email** via SMTP or SendGrid  
   - **WebSocket** for real-time browser alerts  
   - **SMS** via Twilio (configurable)  
   - **Push Notifications** for mobile apps (future)

6. **Caching & Performance**  
   - Redis cache for last-known prices and HTML snapshots  
   - Configurable TTLs per domain or product  
   - Rate-limiting and polite headers/robots.txt adherence

7. **Containerization & Orchestration**  
   - Docker images for all services (API, worker, Redis, PostgreSQL)  
   - `docker-compose` for local dev & testing  
   - Helm charts / Kubernetes manifests (optional)

8. **Observability & Monitoring**  
   - Prometheus metrics (request latencies, queue depths, scrape success rates)  
   - Grafana dashboards (example dashboards included)  
   - Structured logging (JSON) and Sentry integration for error tracking

9. **CI/CD & Testing**  
   - GitHub Actions pipeline: lint, type-check (mypy), pytest, build & publish Docker images  
   - 80%+ test coverage (unit + integration)  
   - Pre-commit hooks (black, isort, flake8)

---

## 🛠️ Tech Stack

| Layer               | Technology                  |
| ------------------- | --------------------------- |
| **API**             | Python, FastAPI            |
| **Asynchronous Tasks** | Redis Queue (RQ), RQ Dashboard |
| **Web Scraping**    | httpx, BeautifulSoup       |
| **Database**        | PostgreSQL, SQLModel       |
| **Cache & Queue**   | Redis                      |
| **Containerization**| Docker, Docker Compose     |
| **CI/CD**           | GitHub Actions             | 
| **Monitoring**      | Prometheus, Grafana, Sentry|
