"""
Staging settings — mirrors production but with relaxed security for QA.
"""
from .base import *  # noqa
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from decouple import config

DEBUG = False

# ── Sentry ────────────────────────────────────────────────────────────
SENTRY_DSN = config('SENTRY_DSN', default='')
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration(), CeleryIntegration()],
        environment='staging',
        traces_sample_rate=1.0,   # capture 100% of transactions in staging
        send_default_pii=True,
    )

# ── Security ──────────────────────────────────────────────────────────
SESSION_COOKIE_SECURE   = True
CSRF_COOKIE_SECURE      = True
SECURE_SSL_REDIRECT     = True
SECURE_HSTS_SECONDS     = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# ── Static/Media via S3 ───────────────────────────────────────────────
USE_S3 = config('USE_S3', default=False, cast=bool)
if USE_S3:
    AWS_ACCESS_KEY_ID        = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY    = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME  = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME       = config('AWS_S3_REGION_NAME', default='us-east-1')
    AWS_S3_CUSTOM_DOMAIN     = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_DEFAULT_ACL          = 'public-read'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    STATICFILES_STORAGE      = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE     = 'storages.backends.s3boto3.S3Boto3Storage'
