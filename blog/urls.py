from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostView.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),
    path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_likes'),
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
    path('about/', views.about_view, name='about'),  
    path('categories/', views.categories_view, name='categories'),
    path('tags/', views.tags_view, name='tags'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('my-articles/', views.my_articles_view, name='my_articles'),
    path('article/create/', views.create_article_view, name='create_article'),
    path('manage-announcements/', views.manage_announcements_view, name='manage_announcements')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
