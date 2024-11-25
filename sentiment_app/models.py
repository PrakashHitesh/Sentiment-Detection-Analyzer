from django.db import models

class SentimentLog(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
    polarity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sentiment} ({self.polarity}) ({self.timestamp})"
