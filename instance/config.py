from sqlalchemy import create_engine

# SQLAlchemy database URI for PostgreSQL
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://laohm_user:QFw1knJoPApRIxWCKzrGwDClHBzxFJpy@dpg-cpm91qtds78s73bis370-a.virginia-postgres.render.com/laohm"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

SECRET_KEY = "THTD673&?/YHG/@H393_YEU"
ADMIN_EMAIL = "admin@personal.com"
