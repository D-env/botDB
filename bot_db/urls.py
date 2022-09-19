from django.urls import path
from .views import MemberList, EventList, MemberDetail, EventDetail

urlpatterns = [
    path('', MemberList.as_view(), name='member-list'),
    path('<int:pk>/', MemberDetail.as_view(), name='member-detail'),
    path('', EventList.as_view(), name='event-list'),
    path('<int:pk>/', EventDetail.as_view(), name='event-detail'),
]