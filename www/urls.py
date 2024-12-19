from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:person_name>/<int:year>", views.get_person, name="Get data of a person"),
    path(
        "<str:person_name>/<int:year>/<int:month>/<int:day>/<int:mood>",
        views.set_mood,
        name="Set mood of a day",
    ),
]
