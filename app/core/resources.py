from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from app.core.logging import init_loguru
from app.core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator:  # noqa: ARG001
    await startup()
    try:
        yield
    finally:
        await shutdown()


async def startup() -> None:
    init_loguru()

    logger.info(f"Starting {settings.APPLICATION_TITLE}...")
    if settings.ENVIRONMENT == "DEV":
        logger.warning(
            "Running in development mode, this is not recommended for production!"
        )

    logger.info(f"{settings.APPLICATION_TITLE} is ready to serve requests.")


async def shutdown() -> None:
    logger.info("Shutting down application...")

    logger.info(f"{settings.APPLICATION_TITLE} has been shut down successfully.")
