from django.db import models

class Guest(models.Model):
    name = models.CharField('NAME', max_length=20)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s %s' % (self.date, self.name)

class Reply(models.Model):
    guestid = models.ForeignKey(Guest, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=40)
    content = models.TextField(blank=True)
    def __str__(self):
        return self.name
