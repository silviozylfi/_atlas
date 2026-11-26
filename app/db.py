import json
from contextlib import contextmanager
import psycopg
from psycopg.rows import dict_row
from app.config import settings

@contextmanager
def connection():
    url = settings().database_url
    if not url:
        raise RuntimeError("Database URL is not set in the environment variables.")
    with psycopg.connect(url, row_factory=dict_row, connect_timeout=10) as conn:
        yield conn

def audit(conn, actor, tenant, action, detail):
    conn.execute("INSERT INTO audit_events (actor, tenant_id, action, detail) VALUES (%s,%s,%s,%s)",
                 (actor, tenant, action, json.dumps(detail)))