# Online Shop — Docker Compose

Three-tier app: nginx (frontend) → Flask (backend) → PostgreSQL (db), plus Adminer.

## Run
    cp .env.example .env      # then edit the password
    docker compose up -d --build

- Shop: http://localhost:8081
- Adminer: http://localhost:8082 (PostgreSQL, server `db`, values from `.env`)

## Architecture
- `front-net`: frontend + backend
- `back-net`: backend + db + adminer (the frontend cannot reach the database)
- `db-data`: named volume, keeps the data across restarts
- Only ports 8081 and 8082 are published; backend and db are internal.

## Stop
    docker compose down       # keeps the data
    docker compose down -v    # deletes the data too
