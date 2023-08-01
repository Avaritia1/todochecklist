from django.test import TestCase, Client
from django.urls import reverse
from .models import Todo, DeletedTodo
from datetime import datetime

class TodoModelTest(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            task="Test Todo",
            creation_date=datetime.now(),
            completed=False,
        )

    def test_todo_creation(self):
        self.assertEqual(self.todo.task, "Test Todo")
        self.assertEqual(self.todo.completed, False)

class DeletedTodoModelTest(TestCase):

    def setUp(self):
        self.deleted_todo = DeletedTodo.objects.create(
            task="Test Deleted Todo",
            creation_date=datetime.now(),
            deleted_at=datetime.now(),  # Correct field name
        )

class HomePageViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('todo:home')  # Add namespace

class DeleteViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.task = Todo.objects.create(task='Test task', completed=False)
        self.delete_url = reverse('todo:delete', args=[self.task.id])  # Add namespace

class RestoreViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.task = DeletedTodo.objects.create(task='Test task', deleted_at=datetime.now())
        self.restore_url = reverse('todo:restore', args=[self.task.id])  # Add namespace


