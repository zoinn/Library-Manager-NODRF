from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views
from .views import login, library, member


urlpatterns = [
    path('', login),
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('library/', library, name='library'),
    path('library/borrow/', views.borrowBook, name='borrow'),
    path('library/return/', views.returnBook, name='return'),
    path('library/addbook/', views.addBook, name='addbook'),
    path('library/delbook/', views.delBook, name='delbook'),
    path('member/', member, name='member'),
]
