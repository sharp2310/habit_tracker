from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):
    """Тестирование модели Habit"""

    def setUp(self):
        """Создание тестовой модели Пользователя (с авторизацией) и Привычки"""

        self.user = User.objects.create(email="test@test.com", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            user=self.user,
            place="GYM",
            time="18:00:00",
            action="Go to the GYM",
            periodicity="Раз в день",
        )

    def test_create_habit(self):
        """Тестирование создания привычки"""

        url = reverse("habits:habits_create")
        data = {
            "user": self.user.pk,
            "place": "GYM",
            "time": "18:00:00",
            "action": "Go to the GYM",
            "periodicity": "Раз в день",
        }

        response = self.client.post(url, data=data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("place"), "GYM")
        self.assertEqual(data.get("time"), "18:00:00")
        self.assertEqual(data.get("action"), "Go to the GYM")
        self.assertEqual(data.get("periodicity"), "Раз в день")

    def test_list_habit(self):
        """Тестирование вывода всех привычек"""

        response = self.client.get(reverse("habits:habits_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        """Тестирование просмотра одной привычки"""

        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("time"), self.habit.time)
        self.assertEqual(data.get("action"), self.habit.action)
        self.assertEqual(data.get("periodicity"), self.habit.periodicity)

    def test_update_habit(self):
        """Тестирование изменений привычки"""

        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {
            "place": "Pool",
            "time": "19:00:00",
            "action": "Go to the pool",
            "periodicity": "Раз в три дня",
        }
        response = self.client.patch(url, data)
        data = response.json()
        print(data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Pool")
        self.assertEqual(data.get("time"), "19:00:00")
        self.assertEqual(data.get("action"), "Go to the pool")
        self.assertEqual(data.get("periodicity"), "Раз в три дня")

    def test_delete_habit(self):
        """Тестирование удаления привычки"""

        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        print(response)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)