from django.urls import path
from . import views
## 유져 url patterns~  따로 엡 만들기 귀차너~ account 에 넣고 따로 써야지~ 아 같이 할까..?
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
]