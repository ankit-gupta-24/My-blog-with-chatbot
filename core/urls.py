from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/',views.contact, name='contact'),
    path('education/',views.education, name='education'),
    path('workdone/',views.workdone, name='workdone'),
    path('skills/',views.skills, name='skills'),
    path('experience/',views.experience, name='experience'),
    path('get_message/',views.get_message, name='get_message'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
