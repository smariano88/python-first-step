#  pylint: disable=C0103
#    ^ eventually we should be able to override or update the
#      CONST_NAME_RGX value

from django.urls import path
from meetings.views import meeting_detail, room_list

urlpatterns = [
    path('<int:id>', meeting_detail, name='meeting_detail'),
    path('rooms', room_list, name='room_list'),
]
