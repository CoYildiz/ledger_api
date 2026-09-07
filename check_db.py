from app.db.session import engine
from sqlalchemy import text

with engine.connect() as conn:
    out = conn.execute(text("SELECT 1"))
    print(out.fetchall())
