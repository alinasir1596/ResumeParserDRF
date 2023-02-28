from django.contrib import admin
from api.models import Keyword, KeywordTag


class KeywordAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('keyword_value', 'keyword_tag',)
    list_filter = ('keyword_tag',)
    search_fields = (
        'keyword_value',
        'keyword_tag'
    )


class KeywordTagAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name',)
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(KeywordTag, KeywordTagAdmin)
