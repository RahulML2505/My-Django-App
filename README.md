# My-Django-App

A demo Django application with cheat sheet.

## Getting Started

- Install Python:

  install the lettest version of python from [`https://www.python.org`](https://www.python.org/downloads/)

- Create a Project Directory:

  ```bash
  $ mkdir my-django-app
  $ cd my-django-app
  ```

- Create a Virtual Environment and Activate it:

  ```bash
  $ python -m venv env
  $ ./env/Scripts/activate
  ```

- Install Django Module:

  ```bash
  $ pip install --upgrade pip
  $ pip install django
  ```

- Create main Django app, and sub applications:

  ```bash
  $ django-admin startproject project .
  ```

  ```bash
  $ python manage.py startapp frontend
  $ python manage.py startapp api
  ```

- Configer New apps:

  open [`project/settings.py`](./project/settings.py)

  add `api.apps.ApiConfig`, `frontend.apps.FrontendConfig` in `INSTALLED_APPS`

  ```python
  INSTALLED_APPS = [
      # Django Apps
      ...
      # Project Apps
      'api.apps.ApiConfig',
      'frontend.apps.FrontendConfig',
  ]

  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      ...
  ]
  ```

- Configer `Root Urls`:

  open [`project/urls.py`](./project/urls.py)

  import `path`, and `include` from `django.urls`

  ```python
  from django.urls import path, include
  ```

  add `path('api/', include('api.urls')),`, `path('', include('frontend.urls')),` in `urlpatterns`

  ```python
  urlpatterns=[
      ...
      path('api/', include('api.urls')),
      path('', include('frontend.urls')),
  ]
  ```

- Configer `Frontend Urls`:

  make [`frontend/urls.py`](./frontend/urls.py)

  import `path` from `django.urls` and import `views` from `.` (current module)

  ```python
  from django.urls import path
  from . import views
  ```

  add `path('', views.index),` in `urlpatterns`

  ```python
  urlpatterns=[
      path('', views.index),
      ...
  ]
  ```

- Configer `Api Urls`:

  make [`api/urls.py`](./frontend/urls.py)

  import `path` from `django.urls` and import `views` from `.` (current module)

  ```python
  from django.urls import path
  from . import views
  ```

  add `path('', views.api),` in `urlpatterns`

  ```python
  urlpatterns=[
      path('', views.api),
      ...
  ]
  ```

- Add views to `frontend` and `api`:

  - open [`frontend/views.py`](./frontend/views.py):

    import `render` from `django.shortcuts`

    ```python
    from django.shortcuts import render
    ```

    ```python
    # Create your views here.
    def index(request, *args, **kwargs):
        return render(request, 'index.html', {'title': 'cloutcoders'})
    ```

  - open [`api/views.py`](./frontend/views.py):

    import `render` from `django.shortcuts`

    ```python
    from django.http.response import JsonResponse
    ```

    ```python
    # Create your views here.
    def api(request):
        return JsonResponse("ok", safe=False)
    ```
