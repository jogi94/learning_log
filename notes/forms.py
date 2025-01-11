from django import forms

from notes.models import Topic, Entry


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ["name", "owner"]


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ["topic", "text"]