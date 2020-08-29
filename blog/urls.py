from django.urls import path
from .views import HomePageView, PostDetailPageView, BlogCreateView, BlogDeleteView, BlogUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', PostDetailPageView.as_view(), name='detail'),
    path('post/new/', BlogCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
