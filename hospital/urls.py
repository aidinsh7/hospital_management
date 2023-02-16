from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('bookings', views.bookings, name='bookings'),
    path('doctors', views.doctors, name='doctors'),
    path('contact', views.contact, name='contact'),
    path('department', views.department, name='departments'),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("profile", views.profile, name="profile"),
    path("viewbooking", views.viewbooking, name="viewbooking"),
    path('adddoctors', views.add_doctors, name='adddoctors'),

]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)