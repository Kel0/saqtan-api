import logging
import sys
from typing import List

from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

from core.logging import InterceptHandler

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "0.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_HOST: str = config("DATABASE_HOST", cast=str)
DATABASE_PORT: int = config("DATABASE_PORT", cast=int)
DATABASE_USER: str = config("DATABASE_USER", cast=str)
DATABASE_PASSWORD: str = config("DATABASE_PASSWORD", cast=str)
DATABASE_NAME: str = config("DATABASE_NAME", cast=str)
APP_SECRET: str = config("APP_SECRET", cast=str)


PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS", cast=CommaSeparatedStrings, default="",
)

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
