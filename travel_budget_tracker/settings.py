import os
from pathlib import Path
import dj_database_url  # Make sure this is in requirements.txt

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# Secret Key
# -------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-default-key")

# -------------------------------
# Debug
# -------------------------------
DEBUG = os.environ.get("DEBUG", "False") == "True"

# -------------------------------
# Allowed Hosts
# -------------------------------
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    os.environ.get("RENDER_EXTERNAL_HOSTNAME", ""),  # automatically set by Render
    "travel-budget-backend.onrender.com",            # explicitly add your Render URL
]

# -------------------------------
# Installed Apps
# -------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party
    "rest_framework",
    "corsheaders",

    # Your apps
    "tracker",
]

# -------------------------------
# Templates
# -------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # optional templates folder
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# -------------------------------
# Middleware
# -------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # must be high up
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "travel_budget_tracker.urls"

# -------------------------------
# CORS
# -------------------------------
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOWED_ORIGINS = [
        "https://qatta.netlify.app",
    ]

# -------------------------------
# REST Framework
# -------------------------------
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ]
}

# -------------------------------
# Database
# -------------------------------
if os.environ.get("DATABASE_URL"):  # Postgres on Render
    DATABASES = {
        "default": dj_database_url.config(
            default=os.environ["DATABASE_URL"],
            conn_max_age=600,
            ssl_require=True
        )
    }
else:  # Local development (SQLite)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# -------------------------------
# Static and Media Files
# -------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------------------
# Localization
# -------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# -------------------------------
# Default Auto Field
# -------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
