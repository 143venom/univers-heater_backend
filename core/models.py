from django.db import models


class baseModel(models.Model):
    posted_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    @property
    def created_date(self):
        return self.created_at.date()

    @property
    def updated_date(self):
        return self.updated_at.date()

    class Meta:
        abstract = True
