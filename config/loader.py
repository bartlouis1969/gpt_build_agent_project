"""
config/loader.py

Beheert laden en valideren van configuratie.
"""

import os
import logging
from dotenv import load_dotenv


def configure_logging(level=None, fmt=None):
    """
    Configureer logging niveau en formattering.
    level: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
        (default uit .env of INFO)
    fmt: logging formatter string (optioneel)
    """
    if level is None:
        level = os.getenv("LOG_LEVEL", "INFO").upper()
    if fmt is None:
        fmt = os.getenv("LOG_FORMAT", "%(asctime)s %(levelname)s %(name)s: %(message)s")
    logging.basicConfig(level=level, format=fmt)


def validate_config():
    errors = []
    try:
        get_openai_api_key()
    except Exception as e:
        errors.append(str(e))
    model_name = get_model_name()
    if not model_name:
        errors.append("MODEL_NAME ontbreekt.")
    temp = get_default_temperature()
    if not 0.0 <= temp <= 1.0:
        errors.append("DEFAULT_TEMPERATURE buiten bereik (0.0-1.0).")
    max_tokens = get_max_tokens()
    if not 0 < max_tokens <= 4000:
        errors.append("MAX_TOKENS buiten bereik (1-4000).")
    timeout = get_gpt_timeout()
    if not 5 <= timeout <= 120:
        errors.append("GPT_TIMEOUT buiten bereik (5-120).")
    if errors:
        raise RuntimeError("Configuratie fouten gevonden:\n" + "\n".join(errors))


logger = logging.getLogger(__name__)


def load_environment():
    env = os.getenv("ENV", "development").lower()
    env_file = ".env"
    if env == "production":
        env_file = ".env.production"
    elif env == "staging":
        env_file = ".env.staging"
    elif env == "development":
        env_file = ".env.development"
    # Fallback naar .env als specifiek bestand niet bestaat
    if not os.path.exists(env_file):
        env_file = ".env"
    load_dotenv(env_file)


load_environment()


def get_openai_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY")
    if not key or not key.startswith("sk-"):
        logger.critical("\u274c Ongeldige of ontbrekende OPENAI_API_KEY.")
        raise RuntimeError(
            'OPENAI_API_KEY ontbreekt of is ongeldig. Moet beginnen met "sk-".'
        )
    return key


def get_model_name() -> str:
    return os.getenv("MODEL_NAME", "gpt-4")


def get_default_temperature() -> float:
    try:
        temp = float(os.getenv("DEFAULT_TEMPERATURE", "0.5"))
        if not 0.0 <= temp <= 1.0:
            raise ValueError
        return temp
    except ValueError:
        logger.warning(
            "Onjuiste waarde voor DEFAULT_TEMPERATURE, standaard 0.5 gebruikt."
        )
        return 0.5


def get_max_tokens() -> int:
    try:
        max_tokens = int(os.getenv("MAX_TOKENS", "1000"))
        if max_tokens <= 0 or max_tokens > 4000:
            raise ValueError
        return max_tokens
    except ValueError:
        logger.warning("Onjuiste waarde voor MAX_TOKENS, standaard 1000 gebruikt.")
        return 1000


def get_gpt_timeout() -> int:
    try:
        timeout = int(os.getenv("GPT_TIMEOUT", "30"))
        if timeout < 5 or timeout > 120:
            raise ValueError
        return timeout
    except ValueError:
        logger.warning("Onjuiste waarde voor GPT_TIMEOUT, standaard 30 gebruikt.")
        return 30
