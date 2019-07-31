from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name ='update'),
    path('delete/<int:pk>', views.delete, name='delete'),

    path('new/', views.new, name='new'),
    path('comment/<int:post_pk>', views.comment, name='comment'),
    path('upda/<int:post_pk>',views.upda, name='upda'),
    path('dele/<int:post_pk>', views.dele, name='dele'),
    path('newblog/', views.blogpost, name ="newblog"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
