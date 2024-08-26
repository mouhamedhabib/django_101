from django.conf import settings 
from django.conf.urls.static import static
from django.urls import path
from .views import HomePageView , postDetailView , AddPostView

app_name = 'feed'

urlpatterns = [
     path('', HomePageView.as_view(), name='index'),
     path ('detail/<int:pk>/',postDetailView.as_view(), name='detail'),
     path ('post/', AddPostView.as_view(), name='post'),
]

if settings.DEBUG :
     urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)