from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, TemplateView, DeleteView, DetailView
from notes.forms import TopicForm, EntryForm
from notes.models import Topic, Entry


# Create your views here.


class DashboardView(TemplateView):
    template_name = "base.html"


class TopicListView(ListView):
    model = Topic
    template_name = "notes/topic_list.html"
    login_url = reverse_lazy('notes:dashboard')


class TopicDetailView(DetailView):
    model = Topic
    template_name = "notes/topic_detail.html"


class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "notes/topic_form.html"
    success_url = reverse_lazy("notes:topic_list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["back_btn_url"] = self.request.META.get("HTTP_REFERER")
        return ctx


class TopicUpdateView(UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = "notes/topic_form.html"
    success_url = reverse_lazy("notes:topic_list")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["back_btn_url"] = self.request.META.get("HTTP_REFERER")
        return ctx


class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy("notes:topic_list")


class EntryListView(ListView):
    model = Entry
    template_name = "notes/entry_list.html"


class EntryDetailView(DetailView):
    model = Entry
    template_name = "notes/entry_detail.html"


class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = "notes/Entry_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["back_btn_url"] = self.request.META.get("HTTP_REFERER")
        return ctx

    def get_success_url(self):
        return str(self.request.META.get("HTTP_REFERER"))


class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = "notes/entry_form.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["back_btn_url"] = self.request.META.get("HTTP_REFERER")
        return ctx

    def get_success_url(self):
        return str(self.request.META.get("HTTP_REFERER"))


class EntryDeleteView(DeleteView):
    model = Entry

    def get_success_url(self):
        return str(self.request.META.get("HTTP_REFERER"))