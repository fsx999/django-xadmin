__author__ = 'paulguichon'
from django.apps import AppConfig
from django.core import checks
from django.utils.translation import ugettext_lazy as _


class XAdminConfig(AppConfig):
    """Simple AppConfig which does not do automatic discovery."""
    name = 'xadmin'
    verbose_name = _("Administration")

    def ready(self):
        self.module.autodiscover()