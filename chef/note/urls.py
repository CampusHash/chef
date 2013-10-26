from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('',
    url(r'^note/', views.home, name='home'),
    url(r'^create/', views.create, name='create'),
    url(r'^all_notes/', views.all_notes, name='all_notes'),
    url(r'^get_notes/(?P<note_id>\d+)/', views.get_notes, name='get_notes'),
    
)



