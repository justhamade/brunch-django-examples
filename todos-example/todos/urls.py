from django.conf.urls.defaults import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import TodoList, TodoDetail, api_root

urlpatterns = patterns('todos.views',
    url(r'^$', api_root, name='api_root'),
    url(r'^todos/$', TodoList.as_view(), name='todo-list'),
    url(r'^todos/(?P<pk>[0-9]+)/$', TodoDetail.as_view(), name='todo-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
