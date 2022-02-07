from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField


class MainSys(Page):
    body = RichTextField(blank=True)
    title = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        FieldPanel("title", classname="full"),
    ]

    api_fields = [
        APIField("body"),
        APIField("title"),
    ]
