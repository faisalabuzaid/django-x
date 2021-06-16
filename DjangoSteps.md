# Steps of Create Django_custom_user

-----(To start a project)------#

## in the terminal

- 1 - mkdir 'some folder name'
- 2 - cd 'some folder name '
- 3 - poetry init -n
- 4 - poetry add django
- 5 - poetry add --dev black
- 6 - poetry shell
- 7 - django-admin startproject 'project_name_project' .  (don't forget the dot)
- 8 - python manage.py startapp 'project_name'
- 9 - python manage.py runserver
- 10 - python manage.py makemigrations users
- 11 - python manage.py migrate
- 12 - python manage.py createsuperuser
- 13 - mkdir templates templates/registration (folder for HTML files)
- 10 - mkdir static (folder for CSS files)
- 11 - touch templates/registration/login.html  templates/registration/signup.html templates/base.html touch templates/home.html (HTML files)

*********************************

## Custom User Model

- update name_project/settings.py
- create a new CustomUser model
- create new UserCreation and UserChangeForm
- update the admin

        # name_project/settings.py

        import os

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'name_app.apps.Name_appConfig', # new
        ]

        TEMPLATES = [{'DIRS': [os.path.join(BASE_DIR,'templates')],},]
        
        AUTH_USER_MODEL = 'name_app.CustomUser' # new
        
        STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')] # new

        LOGIN_REDIRECT_URL = 'home' # new
        LOGOUT_REDIRECT_URL = 'home' # new

    ---
        # name_app/models.py
        from django.contrib.auth.models import AbstractUser
        from django.db import models

        class CustomUser(AbstractUser):
            pass
            # add additional fields in here

            def __str__(self):
                return self.username

    ---

        # name_app/forms.py
        from django import forms
        from django.contrib.auth.forms import UserCreationForm, UserChangeForm
        from .models import CustomUser

        class CustomUserCreationForm(UserCreationForm):

            class Meta:
                model = CustomUser
                fields = ('username', 'email')

        class CustomUserChangeForm(UserChangeForm):

            class Meta:
                model = CustomUser
                fields = ('username', 'email')

    ---

        <!-- templates/base.html -->
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>{% block title %}Django Auth Tutorial{% endblock %}</title>
        </head>
        <body>
        <main>
            {% block content %}
            {% endblock %}
        </main>
        </body>
        </html>

    ---

        <!-- templates/home.html -->
        {% extends 'base.html' %}

        {% block title %}Home{% endblock %}

        {% block content %}
        {% if user.is_authenticated %}
        Hi {{ user.username }}!
        <p><a href="{% url 'logout' %}">Log Out</a></p>
        {% else %}
        <p>You are not logged in</p>
        <a href="{% url 'login' %}">Log In</a> |
        <a href="{% url 'signup' %}">Sign Up</a>
        {% endif %}
        {% endblock %}

    ---

        <!-- templates/registration/login.html -->
        {% extends 'base.html' %}

        {% block title %}Log In{% endblock %}

        {% block content %}
        <h2>Log In</h2>
        <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Log In</button>
        </form>
        {% endblock %}

    ---

        <!-- templates/registration/signup.html -->
        {% extends 'base.html' %}

        {% block title %}Sign Up{% endblock %}

        {% block content %}
        <h2>Sign Up</h2>
        <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Sign Up</button>
        </form>
        {% endblock %}

    ---

        # name_project/urls.py
        from django.contrib import admin
        from django.urls import path, include
        from django.views.generic.base import TemplateView

        urlpatterns = [
            path('', TemplateView.as_view(template_name='home.html'), name='home'),
            path('admin/', admin.site.urls),
            path('name_app/', include('name_app.urls')),
            path('name_app/', include('django.contrib.auth.urls')),]

    ---

        # name_app/urls.py
        from django.urls import path
        from .views import SignUpView

        urlpatterns = [
            path('signup/', SignUpView.as_view(), name='signup'),
        ]

    ---

        # name_app/views.py
        from django.urls import reverse_lazy
        from django.views.generic.edit import CreateView

        from .forms import CustomUserCreationForm

        class SignUpView(CreateView):
            form_class = CustomUserCreationForm
            success_url = reverse_lazy('login')
            template_name = 'registration/signup.html'

    ---