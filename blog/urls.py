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
    path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)