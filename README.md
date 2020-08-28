# Blog project

Steps 

------

1. poetry init -n
2. poetry shell
3. poetry add django
4. django-admin startproject "project name"
5. python manage.py startapp "app name"
6. python mange.py migrate
7. python manage.py runserver 3000
8. python manage.py createsuperuser
9. add config from apps.py to settings.py installed apps
10. add base_dir and templates to dirs in settings.py
11. Setup views.py

```py
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
```

12. Setup urls.py

```py
from django.urls import path
from .views import HomePageView
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

13. add paths to project/urls.py

```py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]

```

14. setup HTML templates
15. Setup users in admin site
16. Goto Admin.py and register your model

```py
from django.contrib import admin
from .models import blog
# Register your models here.
admin.site.register(blog)
```

17. setup your models how you want to setup

```py
from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField(max_length=64)

    def __str__(self):
        return self.title

```
18. python manage.py makemigrations
19. python manage.py migrate
20. Run makemigrations and migrate everytime you change your models
21. use `{% extends 'page.html'%}` to pull in the base html