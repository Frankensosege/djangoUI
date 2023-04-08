from django.urls import path
from . import views

# static 폴더 인식 안될시 사용해 볼 것
from django.conf.urls.static import static
from django.conf import settings

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # static 폴더 인식 안될시 사용해 볼 것