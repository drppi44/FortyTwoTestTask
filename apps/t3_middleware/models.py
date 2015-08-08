from django.db import models


class MyHttpRequest(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=1000)
    path = models.CharField(max_length=1000)
    method = models.CharField(max_length=50)
    uri = models.CharField(max_length=2000)
    query_string = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return unicode(self.uri)
