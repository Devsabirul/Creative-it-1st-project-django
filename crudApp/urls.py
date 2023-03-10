from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name="Home"),
    path('', createProfile, name="createProfile"),
    path('profile/<int:id>', Profile, name="Profile"),
    path('update/<int:id>', Update, name="Update"),
    path('delete/<int:id>', Delete, name="Delete"),
    path('signup', Signup, name="signup"),
]
