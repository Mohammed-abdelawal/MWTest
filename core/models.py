from django.db import models
from django.forms import IntegerField

class PageAnalyticsCount(models.Model):
    visit_time = models.DateTimeField('Visit Time', auto_now_add=True, editable=False)
    url = models.CharField('URL', max_length=2000)
    process_time = models.FloatField('Process Time')
    lang = models.CharField('Language',max_length=100)
    method = models.CharField('Method',max_length=100)
    user_agent = models.CharField('User Data',max_length=220)
    user_ip = models.CharField('User IP', max_length=100)

    class Meta:
        ordering = ('-visit_time',)
        get_latest_by = 'visit_time'
        verbose_name = "Page Analytic Count"
        verbose_name_plural = "Page Analytic Counts"

    def __str__(self):
        return self.url

