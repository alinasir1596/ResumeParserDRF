from django.db import models


class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()


class KeywordTag(models.Model):
    name = NameField(unique=True, max_length=100)

    def __str__(self):
        return str(self.name).capitalize()


class Keyword(models.Model):
    keyword_value = NameField(max_length=100, unique=True)
    keyword_tag = models.ForeignKey(KeywordTag, related_name='keyword_tagger', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.keyword_value).capitalize()


