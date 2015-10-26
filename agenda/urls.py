from django.conf.urls import patterns, url, include
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

"""urlpatterns = patterns('agenda.tarefas.views',

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),#

   url (r'^admin/', include(admin.site.urls)),
   """
urlpatterns = patterns('',
                       (r'^tarefas/$', 'agenda.tarefas.views.index'),
                       (r'^task/$', 'agenda.task.views.list_task'),
                       (r'^admin/', include(admin.site.urls)),
                      )