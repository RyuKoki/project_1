# project_1

### Django
- Install `Django` on project's folder `python -m pip install Django`
- Check version Django `python -m django --version`
- Create Django project `django-admin startproject <project name>`
  - Running server `python manage.py runserver`
- Create the app `python manage.py startapp <app name>`
- Model-View-Template 
  - http response at return function in app > views.py
  - mapping views with project > urls.py and import views from app by `from <project name> import views`
    - in list of urlpatterns add the page that want to render from app > views.py such as `path('', views.index), # HOMEPAGE`
