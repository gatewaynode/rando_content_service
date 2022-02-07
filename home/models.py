from email.policy import default
from turtle import window_height
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]

    api_fields = [
        APIField("body"),
    ]


class MainSys(Page):
    body = RichTextField(blank=True)
    stuff = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        FieldPanel("stuff", classname="full"),
    ]

    api_fields = [
        APIField("body"),
        APIField("stuff"),
    ]


class BlogPage(Page):
    content = RichTextField()
    description = models.TextField()
    weight = models.IntegerField(default=0)
    author = models.TextField(default="Anon")
    license = models.TextField(default="cc-by-sa")
    created = models.DateTimeField()
    modified = models.DateTimeField()

    content_panels = Page.content_panels + [
        FieldPanel("content", classname="full"),
        FieldPanel("description", classname="full"),
        FieldPanel("weight", classname="yazza"),
        FieldPanel("author", classname="full"),
        FieldPanel("license", classname="full"),
        FieldPanel("created", classname="full"),
        FieldPanel("modified", classname="full"),
    ]

    api_fields = [
        APIField("content"),
        APIField("description"),
        APIField("weight"),
        APIField("author"),
        APIField("license"),
        APIField("created"),
        APIField("modified"),
    ]
