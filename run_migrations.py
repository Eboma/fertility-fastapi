import os
from alembic.config import Config
from alembic import command


def run_migrations():
    alembic_cfg = Config("alembic.ini")
    # Make sure we use Postgres, not SQLite
    alembic_cfg.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    run_migrations()
