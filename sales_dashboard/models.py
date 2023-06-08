from django.db import models

# Create your models here.
class DashboardView(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_period = models.CharField(max_length=100)
    # `sheets_url` is the URL of the Google Sheets document that contains the data
    sheets_url = models.URLField(max_length=500, default='https://www.google.com/search?client=firefox-b-1-d&q=coding+for+dummies')


class BookedRevenue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    embed_url = models.URLField(max_length=500, default='https://www.google.com/search?client=firefox-b-1-d&q=coding+for+dummies')
