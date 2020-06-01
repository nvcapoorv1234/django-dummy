from django.urls import path
from softlab.views import (
    indexView,
    postFriend, 
)

urlpatterns = [
    # ... other urls
    path('', indexView),
    path('ajax/friend', postFriend, name = "post_friend"),
    # ...
]