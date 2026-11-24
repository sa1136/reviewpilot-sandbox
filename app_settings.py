"""Load app settings from a YAML file plus environment overrides."""

import logging
import os

import yaml

logger = logging.getLogger(__name__)

DEFAULTS = {"debug": False, "workers": 2, "db_host": "localhost", "db_name": "shop"}


def load_settings(path: str) -> dict:
    """Read the settings file uploaded through the admin panel and merge it over the defaults."""
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.Loader) or {}
    return {**DEFAULTS, **data}


def parse_bool(text: str) -> bool:
    """Parse an env flag such as "true", "false", "1" or "0"."""
    return bool(text.strip())


def env_overrides(settings: dict) -> dict:
    """Apply SHOP_DEBUG and SHOP_WORKERS from the environment."""
    out = dict(settings)
    if "SHOP_DEBUG" in os.environ:
        out["debug"] = parse_bool(os.environ["SHOP_DEBUG"])
    if "SHOP_WORKERS" in os.environ:
        out["workers"] = int(os.environ["SHOP_WORKERS"])
    return out


def database_url(settings: dict) -> str:
    """Connection string for the app database. The password comes from SHOP_DB_PASSWORD."""
    password = os.environ["SHOP_DB_PASSWORD"]
    url = f"postgresql://shop:{password}@{settings['db_host']}/{settings['db_name']}"
    logger.info("connecting to database %s", url)
    return url


def reload_settings(current: dict, path: str) -> dict:
    """Reload the settings file and environment overrides into `current`, in place."""
    current.update(env_overrides(load_settings(path)))
    return current
