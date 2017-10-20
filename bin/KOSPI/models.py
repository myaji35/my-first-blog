from django.db import models

# Create your models here.
class Post(models.Model):
    st_market   = models.CharField("종목시장", max_length=10, unique=True)
    market_memo = models.CharField("시장설명", max_length=200)

    def __str__(self):
        return self.st_market
