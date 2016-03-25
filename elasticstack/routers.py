from django.conf import settings
from django.utils import translation
from haystack import routers
from haystack.constants import DEFAULT_ALIAS


class MultilingualRouter(routers.BaseRouter):
    prefix = DEFAULT_ALIAS

    def for_write(self, **hints):
        return filter(lambda c: c.startswith(self.prefix), settings.HAYSTACK_CONNECTIONS)

    def for_read(self, **hints):
        lang = translation.get_language()[:2]
        localized_conn = "{}_{}".format(self.prefix, lang)
        if localized_conn in settings.HAYSTACK_CONNECTIONS:
            return localized_conn
        return self.prefix
