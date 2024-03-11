from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from main.models import Habit

from main.paginators import HabitPaginator
from main.permissions import IsOwner
from main.serializers import HabitSerializer
from main.servises import create_reminder, update_reminder, delete_reminder


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        habit = serializer.save()
        habit.user = self.request.user
        create_reminder(habit)
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """ Вывод списка привычек пользователя """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):

        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class HabitPublicListAPIView(generics.ListAPIView):
    """ Вывод списка публичных привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny]

    def get_queryset(self):

        queryset = Habit.objects.filter(habit_is_public=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр одной привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Изменение привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):

        habit = serializer.save()
        update_reminder(habit)
        habit.save()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_destroy(self, instance):

        delete_reminder(instance)
        instance.delete()