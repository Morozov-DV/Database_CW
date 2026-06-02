from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='todo/login.html'), name='login'),
    
   
    path('signup/', RedirectView.as_view(url='/'), name='signup'),
    
    path('', include('todo.urls')),
]