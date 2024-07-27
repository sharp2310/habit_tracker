from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from habits.models import Habit, Reward
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@email.com", password="123", chat_id="255450278"
        )
        self.habit = Habit.objects.create(
            owner=self.user,
            activity="Test",
            place="Home",
            time="10:00:00",
            duration="120",
            is_pleasant=False,
        )
        self.reward = Reward.objects.create(
            owner=self.user,
            title="Test reward",
            description="Test reward description",
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse("habits:habit_create")

        data = {
            "owner": 1,
            "activity": "Test_2",
            "place": "Home",
            "time": "08:00:00",
            "duration": "120",
            "is_pleasant": False,
            "reward": 1,
        }

        data_2 = {
            "owner": 1,
            "activity": "Test_2",
            "place": "Home",
            "time": "08:00:00",
            "duration": "-1",
            "is_pleasant": False,
            "reward": 1,
        }

        pleasant_habit_bad = {
            "owner": 1,
            "activity": "Test_3",
            "place": "Home",
            "time": "08:00:00",
            "duration": "120",
            "is_pleasant": True,
            "reward": 1,
        }
        pleasant_habit = {
            "owner": 1,
            "activity": "Shower",
            "place": "Home",
            "duration": "120",
            "is_pleasant": True,
        }

        data_3 = {
            "owner": 1,
            "reward": 1,
            "related_habit": 3,
            "activity": "Test_3",
            "place": "Home",
            "time": "08:00:00",
            "duration": "120",
            "is_pleasant": False,
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)
        self.assertEqual(Habit.objects.last().activity, "Test_2")
        self.assertEqual(Habit.objects.last().owner, self.user)
        self.assertEqual(Habit.objects.last().reward.title, self.reward.title)

        response_2 = self.client.post(url, pleasant_habit)

        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 3)
        self.assertEqual(Habit.objects.last().activity, "Shower")
        self.assertEqual(Habit.objects.last().owner, self.user)

        response_3 = self.client.post(url, data_2)

        self.assertEqual(response_3.status_code, status.HTTP_400_BAD_REQUEST)

        response_3 = self.client.post(url, pleasant_habit_bad)

        self.assertEqual(response_3.status_code, status.HTTP_400_BAD_REQUEST)

        response_3 = self.client.post(url, data_3)

        self.assertEqual(response_3.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_update(self):
        data = {"activity": "test_2_update"}

        response = self.client.patch(f"/habits/update/{self.habit.pk}/", data)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("activity"), "test_2_update")

    def test_habit_retrieve(self):
        response = self.client.get(f"/habits/{self.habit.pk}/")
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("activity"), self.habit.activity)

        url_2 = reverse("habits:habit_retrieve", args=(26,))
        response_2 = self.client.get(url_2)
        self.assertEqual(response_2.status_code, status.HTTP_404_NOT_FOUND)

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", args=(self.habit.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit_delete", args=(5,))
        self.client.delete(url)

        url = reverse("habits:habit_list")
        print(url)

        result = {
            "count": 0,
            "next": None,
            "previous": None,
            "results": [],
        }

        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class RewardTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email="test@email.com", password="123", chat_id="255450278"
        )
        self.reward = Reward.objects.create(
            owner=self.user,
            title="Test reward",
            description="Test reward description",
        )
        self.client.force_authenticate(user=self.user)

    def test_reward_retrieve(self):
        response = self.client.get(f"/habits/rewards/{self.reward.pk}/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get("title"), self.reward.title)

        response_2 = self.client.get(f"/habits/rewards/65/")

        self.assertEqual(response_2.status_code, status.HTTP_404_NOT_FOUND)

    def test_reward_create(self):
        data = {
            "owner": self.user.pk,
            "title": "test_reward_2",
            "description": "test_reward_description",
        }
        response = self.client.post("/habits/rewards/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Reward.objects.all().count(), 2)
        self.assertEqual(Reward.objects.last().title, "test_reward_2")
        self.assertEqual(Reward.objects.last().owner, self.user)

    def test_reward_update(self):
        data = {
            "title": "test_reward_3",
        }

        response = self.client.patch(f"/habits/rewards/{self.reward.pk}/", data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "test_reward_3")

    def test_reward_delete(self):
        response = self.client.delete(f"/habits/rewards/{self.reward.pk}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reward.objects.all().count(), 0)

    def test_reward_list(self):
        response = self.client.get(f"/habits/rewards/")

        result = [
            {
                "id": self.reward.pk,
                "title": "Test reward",
                "description": "Test reward description",
                "owner": self.user.pk,
            }
        ]

        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Reward.objects.all().count(), 1)
        self.assertEqual(Reward.objects.last().title, "Test reward")
        self.assertEqual(Reward.objects.last().owner, self.user)
        self.assertEqual(data, result)