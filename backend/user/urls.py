from django.urls import path
from .views import (
    CreateUserView, CreateTokenView, ManageUserView, ChangePasswordView,
    # UserImageUpdateView,
)
urlpatterns = [
    # path('upload/', FileList.as_view()),
    path('user/create/', CreateUserView.as_view(), name='create'),
    path('user/token/', CreateTokenView.as_view(), name='token'),
    path('user/me/', ManageUserView.as_view(), name='me'),
    path('user/change-password/',
         ChangePasswordView.as_view(), name='password-change'),
    # path("users/<int:id>/image/", UserImageUpdateView.as_view(), name="user-image-update"),
]
