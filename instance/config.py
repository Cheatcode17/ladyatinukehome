from sqlalchemy import create_engine
import psycopg2

config = {
    'user': 'laohm_user',
    'password': 'QFw1knJoPApRIxWCKzrGwDClHBzxFJpy',
    'host': 'dpg-cpm91qtds78s73bis370-a.virginia-postgres.render.com',
    'database': 'laohm'
}

# Connect to PostgreSQL using psycopg2
connection = psycopg2.connect(
    user=config['user'],
    password=config['password'],
    host=config['host'],
    database=config['database']
)

SECRET_KEY = "THTD673&?/YHG/@H393_YEU"
ADMIN_EMAIL = "admin@personal.com"


# SQLAlchemy database URI for PostgreSQL
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://laohm_user:QFw1knJoPApRIxWCKzrGwDClHBzxFJpy@dpg-cpm91qtds78s73bis370-a.virginia-postgres.render.com/laohm"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)

