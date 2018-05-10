from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


class Paste(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python', max_length=100)
