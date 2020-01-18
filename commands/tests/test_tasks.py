from django.test import TestCase
from commands.moduls import tasks

class TasksWorkTests(TestCase):
    def test_task1(self):
        result = tasks.task_1(10)
        self.assertIs(type(result) == str, True)
    def test_task2(self):
        result = tasks.task_2(10)
        self.assertIs(type(result) == str, True)
    def test_task3(self):
        result = tasks.task_3(10)
        self.assertIs(type(result) == str, True)
    def test_task4(self):
        result = tasks.task_4(10)
        self.assertIs(type(result) == str, True)
    def test_task5(self):
        result = tasks.task_5(10, 5)
        self.assertIs(type(result) == str, True)
    def test_task6(self):
        result = tasks.task_6('aa bb cc dd ff dd gh aa ss dd sa', 'aa')
        self.assertIs(type(result) == str, True)
    def test_task7(self):
        result = tasks.task_7('aaa bbb ccc dd ff gg hh jj kk ll rr ee eeww fds erwer', 2)
        self.assertIs(type(result) == str, True)