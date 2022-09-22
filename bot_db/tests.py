from rest_framework.test import APITestCase
from .models import Member, Event
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class test_db(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_member1 = Member.objects.create(
            name="James",
            guild=1,
            availability=[[None], [1200, 1500], [None], [None], [1000, 1800], [1300, 1700], [1500, 2200]],
        )
        test_member1.save()
        test_member2 = Member.objects.create(
            name="Abby",
            guild=2,
            availability=[[800, 1230], [1200, 1500], [None], [None], [None], [1300, 1700], [1500, 2200]],
        )
        test_member2.save()
        test_event = Event.objects.create(
            name="Demo",
            description="Test Event",
            duration=100,
            guild=1,
            start_time=1200,
            end_time=1300,
            day="Monday",
        )
        test_event.save()


    def test_member_model(self):
        member = Member.objects.get(id=1)
        actual_guild = str(member.guild)
        actual_name = str(member.name)
        actual_availability = str(member.availability)
        self.assertEqual(actual_guild, '1')
        self.assertEqual(actual_name, "James")
        self.assertEqual(
            actual_availability, "[[None], [1200, 1500], [None], [None], [1000, 1800], [1300, 1700], [1500, 2200]]"
        )


    def test_event_model(self):
        event = Event.objects.get(id=1)
        actual_guild = str(event.guild)
        actual_name = str(event.name)
        actual_description = str(event.description)
        actual_duration = str(event.duration)
        actual_start_time = str(event.start_time)
        actual_end_time = str(event.end_time)
        actual_day=str(event.day)
        self.assertEqual(actual_guild, '1')
        self.assertEqual(actual_name, 'Demo')
        self.assertEqual(actual_description, 'Test Event')
        self.assertEqual(actual_duration, '100')
        self.assertEqual(actual_start_time, '1200')
        self.assertEqual(actual_end_time, '1300')
        self.assertEqual(actual_day, 'Monday')


    def test_create_member(self):
        url = reverse("member-list")
        self.client.login(username='testuser1', password="pass")
        data = {"guild": 1, "name": "Maia", "availability": [[None], [1200, 1500], [600, 1500], [None], [1000, 1800], [1300, 1700], [1500, 2200]]}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        members = Member.objects.all()
        self.assertEqual(len(members), 3)
        self.assertEqual(Member.objects.get(id=3).name, "Maia")
        self.assertEqual(Member.objects.get(id=3).availability, [[None], [1200, 1500], [600, 1500], [None], [1000, 1800], [1300, 1700], [1500, 2200]])


    # def test_create_event(self):
    #     url = reverse("event-list")
    #     self.client.login(username='testuser1', password="pass")
    #     data = {"name":"Demo2",
    #         "description":"Test2",
    #         "duration":200,
    #         "guild":1,
    #         "start_time":1000,
    #         "end_time":1200,
    #         "day":"Thursday"}
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     events = Event.objects.all()
    #     self.assertEqual(len(events), 2)
    #     self.assertEqual(Event.objects.get(id=2).name, "Demo2")


    # def test_update_member(self):
    #     url = reverse("member-detail", args=(1,))
    #     data = {
    #         "name": "James",
    #         "guild": 1,
    #         "availability": [[None], [None], [None], [None], [1000, 1800], [1300, 1700], [1500, 2200]],
    #     }
    #     self.client.login(username='testuser1', password="pass")
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     member = Member.objects.get(id=1)
    #     self.assertEqual(member.name, data["name"])
    #     self.assertEqual(member.guild, data["guild"])
    #     self.assertEqual(member.availability, data["availability"])