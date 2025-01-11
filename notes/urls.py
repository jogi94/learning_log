from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import TopicCreateView, TopicUpdateView, TopicListView, DashboardView, TopicDeleteView, TopicDetailView, \
    EntryDeleteView, EntryUpdateView, EntryCreateView, EntryDetailView, EntryListView

app_name = 'notes'

urlpatterns = [
    path('', login_required(DashboardView.as_view()), name='dashboard'),
]

urlpatterns += [
    path('topic/', login_required(TopicListView.as_view()), name='topic_list'),
    path('topic/detail/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('topic/create/', TopicCreateView.as_view(), name='topic_create'),
    path('topic/update/<int:pk>/', TopicUpdateView.as_view(), name='topic_update'),
    path('topic/delete/<int:pk>/', TopicDeleteView.as_view(), name='topic_delete'),
]

urlpatterns += [
    path('entry/', login_required(EntryListView.as_view()), name='entry_list'),
    path('entry/detail/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('entry/create/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/update/<int:pk>/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/delete/<int:pk>/', EntryDeleteView.as_view(), name='entry_delete'),
]