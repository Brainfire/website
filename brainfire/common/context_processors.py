from django.conf import settings # import the settings file

def common_settings(context):
    # return the value you want as a dictionnary. you may add multiple values in there.
    try:
        google_analytics_id = settings.GOOGLE_ANALYTICS_ID
    except AttributeError:
        google_analytics_id = None
    
    return {
        'GOOGLE_ANALYTICS_ID': google_analytics_id,
        'DEBUG': settings.DEBUG,
        'SITE_TITLE': settings.SITE_TITLE,
        'SITE_TAGLINE': settings.SITE_TAGLINE,
    }