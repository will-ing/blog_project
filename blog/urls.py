from django.urls import path
from .views import HomePageView, PostDetailPageView, BasePageView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', BasePageView.as_view(), name='base'),
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', PostDetailPageView.as_view(), name='detail'),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
