from django.contrib import admin
from django.urls import path
from authentication import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('list/',views.list, name='list'),
    path('createitem/',views.createitem,name='createitem'),
    path('<int:pk>/update/',views.update, name='update'),
    path('<int:pk>/delete',views.delete, name='delete'),
    path('Logout',views.Logout,name='Logout'),
    path('profile/',views.profile, name='profile'),
    path('addcomment/<int:item_id>/', views.addcomment, name='addcomment'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)