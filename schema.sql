CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  role TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS queries (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  query_id TEXT UNIQUE NOT NULL,
  user_id INTEGER,
  title TEXT,
  description TEXT,
  status TEXT DEFAULT 'open',
  created_at TEXT,
  closed_at TEXT,
  FOREIGN KEY(user_id) REFERENCES users(id)
);