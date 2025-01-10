from django.db import models
from django.utils.translation import gettext_lazy, ngettext_lazy


class Greeting(models.Model):
    text = models.TextField(verbose_name=gettext_lazy("Text"), null=False, blank=False)

    def __str__(self):
        return self.text

    @property
    def info(self):
        return ngettext_lazy(
            "This greeting has %(count)s word.",
            "This greeting has %(count)s words.",
            "count"
        ) % {"count": len(self.text)}

    class Meta:
        verbose_name = gettext_lazy("Greeting")
        verbose_name_plural = gettext_lazy("Greetings")

