from django.contrib import admin

from notes.models import Topic, Entry


# Register your models here.


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'created', 'modified']


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'text', 'topic', 'date_added']

