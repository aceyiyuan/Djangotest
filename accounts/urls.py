
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.userPage, name="user-page"),
    path('account/',views.accountSettings, name='account'),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>', views.customer, name="customer"),
    path('create_order/<int:pk>', views.createOrder, name="create_order"),
    path('update_order/<int:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<int:pk>', views.deleteOrder, name="delete_order")
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)