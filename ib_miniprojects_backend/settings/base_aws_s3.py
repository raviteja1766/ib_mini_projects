import os

# ********************** Static Files *************************
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'Cache-Control': 'max-age=94608000',
}

AWS_ACCESS_KEY_ID = os.environ.get("CUSTOM_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("CUSTOM_AWS_SECRET_ACCESS_KEY")

AWS_CLOUDFRONT_DOMAIN = os.environ.get("AWS_CLOUDFRONT_DOMAIN")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN', '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME)
AWS_S3_HOST = 's3-ap-south-1.amazonaws.com'

STATICFILES_STORAGE = 'ib_miniprojects_backend.common.aws.custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'ib_miniprojects_backend.common.aws.custom_storages.MediaStorage'

STATICFILES_LOCATION = '%s/static' % os.environ.get("STAGE")
MEDIAFILES_LOCATION = '%s/media' % os.environ.get("STAGE")

STATIC_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = '//%s/%s/' % (AWS_CLOUDFRONT_DOMAIN, MEDIAFILES_LOCATION)

AWS_ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")
AWS_S3_REGION_NAME = os.environ.get("AWS_S3_REGION_NAME", "ap-south-1")
DEFAULT_CLOUDFRONT_PROTOCOL = os.environ.get(
    "DEFAULT_CLOUDFRONT_PROTOCOL", "https")
