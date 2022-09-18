"""App_for_booking_conference_rooms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from booking_app import views
from booking_app.views import AddConferenceRoomView, ConferenceRoomListView, ConferenceRoomDeleteView, \
    ConferenceRoomModificationView, ConferenceRoomReservationView, ConferenceRoomInfoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home', views.home),
    path('add_conference_room/', AddConferenceRoomView.as_view()),
    path('conference_room_list/', ConferenceRoomListView.as_view()),
    path('conference_room_list/delete/<int:room_id>/', ConferenceRoomDeleteView.as_view()),
    path('conference_room_list/modify/<int:room_id>/', ConferenceRoomModificationView.as_view()),
    path('conference_room_list/reserve/<int:room_id>/', ConferenceRoomReservationView.as_view()),
    path('conference_room_list/<int:room_id>/', ConferenceRoomInfoView.as_view()),
]
