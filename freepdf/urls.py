from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from app.views import index, product_detail,mes_ebooks,telecharger_ebook
from new.views import newsletter
from compte.views import login_user,logout_user,signup
from django.conf import settings

urlpatterns = [
    path('',index,name="index"),
    path('ebook/<str:slug>/',product_detail, name="ebook"),
    path('login_user/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('singup/',signup, name='singup'),
    path('newsletter/',newsletter,name="newsletter"),
    path("mes-ebooks/",mes_ebooks, name="mes_ebooks"),
    path("telecharger/<slug:slug>/",telecharger_ebook, name="telecharger_ebook"),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
