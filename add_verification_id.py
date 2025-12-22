import os
from sqlalchemy import create_engine, text

# Get the DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Connect to the database
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    # Run the SQL command to add the column
    conn.execute(text("""
        ALTER TABLE otp
        ADD COLUMN IF NOT EXISTS verification_id VARCHAR(255) UNIQUE NOT NULL;
    """))
    conn.commit()

print("Column 'verification_id' added successfully!")
