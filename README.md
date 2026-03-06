# Two-Man Thai Consonant Drill

This is a simple quiz application for learning Thai consonants. It now includes a backend service that tracks a user's consecutive quiz starts (a "streak").

## Frontend
- `index.html` contains the UI and JavaScript logic.
- Users enter a nickname, which is displayed during the quiz along with the current streak.
- When the quiz starts, the frontend sends a request to the backend to increment the streak counter.

## Backend
- Python service built with FastAPI.
- Persists streak counters in a PostgreSQL database using SQLAlchemy.
- Endpoint:
  - `POST /streak` with JSON `{ "nickname": "..." }` increments or creates a user record and returns the new streak.

### Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure the database connection via the `DATABASE_URL` environment variable. Default points to
   `postgresql://postgres:password@localhost:5432/twoman`.
3. Start the service:
   ```bash
   uvicorn backend.app:app --reload
   ```

> ⚠️ `requirements.txt` purposely omits explicit version numbers so the latest compatible releases are installed.

## Notes
- The backend will automatically create the `users` table if it does not exist.
- The frontend assumes the backend is served from the same host/port; adjust the fetch URL if necessary.
