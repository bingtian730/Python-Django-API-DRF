from django.urls import path
from . import views


urlpatterns = [
# Add URL configuration for the path() function here
path('book/', views.BookView.as_view()),
path('book/<int:pk>', views.SingleBookView.as_view()),
] 