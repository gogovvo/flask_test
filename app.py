import os
from flask import Flask
from sqlalchemy import create_engine, text

app = Flask(__name__)

# DB URI (환경변수로 관리하는게 좋아요)
DB_URI = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://qa_user:spsp123!@mariadb:3306/qa?charset=utf8mb4"
)

engine = create_engine(DB_URI, pool_pre_ping=True, pool_recycle=1800, future=True)

@app.get("/")
def index():
    return "Flask is alive", 200

@app.get("/pingdb")
def pingdb():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT NOW()")).scalar_one()
        return {"db_time": str(result)}
