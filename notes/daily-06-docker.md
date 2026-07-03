# Docker & Testing Workflow Summary (DSA)
# Date: July 2, 2026
## Core Commands

- **Start the app:**  
  ```bash
  docker compose -f docker/docker-compose.yml --env-file .env up --build
  ```
  - Builds image, sets up network, starts containers:
    - PostgreSQL (`postgresql_container`)
    - FastAPI (`fastapi_container`)

- **Run Tests (Recommended):**  
  ```bash
  docker compose -f docker/docker-compose.yml --env-file .env run --rm tests
  ```
  - Launches a temporary container using the API image, running `pytest -v`
  - Cleans up automatically after tests finish

- **Stop all containers:**  
  ```bash
  docker compose down
  ```

## Key Behaviors & Tips

- **PostgreSQL Initialization:**
  - First run: DB initialized if empty
  - Later runs: Skips if volume persists (normal behavior)

- **Environment Variables:**
  - Use `--env-file .env` to ensure variables like `POSTGRES_USER` and `POSTGRES_DB` are set.
  - If missing, warnings like `POSTGRES_USER not set` may appear.

- **Common Pitfall:**  
  - Always specify the compose file (`-f docker/docker-compose.yml`).  
  - Missing this causes config errors.

## Conceptual Takeaways

- **Service Types:**
  - **API / DB:** Long-running containers
  - **Tests:** One-off jobs (run only on demand, not auto-run by `up`)

- **Command Purposes:**
  | Command                                | Purpose            |
  |-----------------------------------------|--------------------|
  | `docker compose up`                     | Start full system  |
  | `docker compose run --rm tests`         | Run on-demand job  |

- **Container Lifecycle:**
  - API & DB: Run persistently
  - Tests: Run, exit, and container gets removed (`--rm`)

- **Best Practice:**
  - Don’t run tests automatically in `up`
  - Tests should not be long-running containers

## Sample Test Results
- Integration: API routes (home, valid/invalid URL)
- Unit: Data cleaning, model transformation
- All tests: 5/5 passed (~33s)

## Takeaway

**Docker Compose separates:**
- Services (API & DB): Always running
- Jobs (Tests): Run **only** when triggered