from django.db import transaction
from django.core.management import call_command
from www.models import MoodOfTheDay
from django.contrib.auth import get_user_model


def populate_db(apps, schema_editor):
    with transaction.atomic():
        populate_moods()

    call_command("createinitialrevisions")


def depopulate_db():
    MoodOfTheDay.objects.all().delete()


def populate_moods():
    pass


def populate_user_groups():
    User = get_user_model()

    admin_user = User(username="admin", is_superuser=True, is_staff=True, email="admin@admin.com")
    admin_user.set_password(raw_password="password")
    admin_user.save()

    return admin_user
