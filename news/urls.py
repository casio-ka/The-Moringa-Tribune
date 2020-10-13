from django.urls import path
from .views import welcome, news_of_day, past_days_news

urlpatterns = [
    path ('', welcome, name='welcome'),
    path ('today/',news_of_day,name='newsToday'),
    path ('archives/<slug:past_date>/', past_days_news, name = 'pastNews'),
]