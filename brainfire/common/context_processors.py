from django.conf import settings # import the settings file

def common_settings(context):
    return {
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
        'GOOGLE_ANALYTICS_DOMAIN': settings.GOOGLE_ANALYTICS_DOMAIN,
        'DEBUG': settings.DEBUG,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_TAGLINE': settings.SITE_TAGLINE,
        'ENABLE_ZENDESK': settings.ENABLE_ZENDESK,
    }