from datetime import date, datetime

from django.shortcuts import render, redirect
from django.views import View
from booking_app.models import ConferenceRoom, RoomReservation

"""Function that redirects to the home page"""


def home(request):
    return render(request, "home.html")


"""The main class responsible for adding conference rooms 
and dynamically completing the page with the list of rooms"""


class AddConferenceRoomView(View):

    def get(self, request):
        return render(request, "add_conference_room.html")

    def post(self, request):
        name = request.POST.get("room_name")
        capacity = request.POST.get("room_capacity")
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("projector") == "on"
        if name == "":
            return render(request, "add_conference_room.html", context={"error": "The name of the conference room is "
                                                                                 "essential"})
        if capacity < 0:
            return render(request, "add_conference_room.html", context={"error": "Capacity must be above zero"})
        if ConferenceRoom.objects.filter(room_name=name):
            return render(request, "add_conference_room.html", context={"error": "The name of the room is already taken"})
        ConferenceRoom(room_name=name, room_capacity=capacity, projector=projector).save()
        #return render(request, "conference_room_list.html")
                      # {'message': f"Added a conference room {name} with capacity {capacity}"})
        return redirect("/conference_room_list/")


"""A class that takes all the objects from the ConferenceRoom model 
and passes them to the html template"""


class ConferenceRoomListView(View):

    def get(self, request):
        conference_rooms = ConferenceRoom.objects.all()
        return render(request, "conference_room_list.html", context={"conference_rooms": conference_rooms})


"""Class which delete the object"""


class ConferenceRoomDeleteView(View):

    def get(self, request, room_id):
        room_to_delete = ConferenceRoom.objects.get(id=room_id)
        room_to_delete.delete()
        return redirect("/conference_room_list/")


"""Class enabling modification of conference rooms"""


class ConferenceRoomModificationView(View):

    def get(self, request, room_id):
        room_to_change = ConferenceRoom.objects.get(id=room_id)
        return render(request, "modify_conference_room.html", {"room": room_to_change})

    def post(self, request, room_id):
        name = request.POST.get("room_name")
        capacity = request.POST.get("room_capacity")
        capacity = int(capacity) if capacity else 0
        projector = request.POST.get("projector") == "on"  #zamiast ifuw dodac == "on" bo chceck box zwraca nona gdy sie nie nic nie zaznaczy
        if name == "":
            return render(request, "conference_room_list.html", context={"error": "The name of the conference room is "
                                                                                 "essential"})
        if capacity < 0:
            return render(request, "conference_room_list.html", context={"error": "Capacity must be above zero"})
        if ConferenceRoom.objects.filter(room_name=name):   #tego ni potrzeba chyba potem to przemysle
            return render(request, "conference_room_list.html", context={"error": "The name of the room is already taken"})
        ConferenceRoom(id=room_id, room_name=name, room_capacity=capacity, projector=projector).save()
        # return render(request, "add_conference_room.html",
        #               {'message': f"Added a conference room {name} with capacity {capacity}"})
        return redirect("/conference_room_list/")


class ConferenceRoomReservationView(View):

    def get(self, request, room_id):
        return render(request, 'conference_room_reservation.html')

    def post(self, request, room_id):
        reservation_date = request.POST.get("date")
        comment = request.POST.get("comment")
        if date.fromisoformat(reservation_date) < date.today():
            return render(request, "conference_room_reservation.html",
                          {"message": "the date is in the past"})
        if RoomReservation.objects.filter(date=reservation_date):
            return render(request, "conference_room_reservation.html",
                          {"message": "the room is already reserved on the selected date"})
        RoomReservation(date=reservation_date, comment=comment, room_id_id=room_id).save()
        return redirect("/conference_room_list/")
