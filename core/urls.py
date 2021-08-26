from django.urls import path
from core.views import (
        HomeView,
        EventLike,
        EventUnlike,
        EventCreate
    )
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', HomeView.as_view(), name='home_view'),
    path('event/create/', EventCreate.as_view(), name='event_create'),
    path('event/like/<int:id>/', EventLike.as_view(), name='event_like_view'),
    path('event/unlike/<int:id>/', EventUnlike.as_view(), name='event_unlike_view'),
]

urlpatterns.extend(
    static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
)
