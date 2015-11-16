from apps.hello.forms import TaskForm
from apps.hello.models import Task
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
import re


class TaskListPageTest(TestCase):
    def test_task_page_template_and_code(self):
        """task page uses right template and status code"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('task'))

        self.assertTemplateUsed(response, 'hello/task.html')
        self.assertEquals(response.status_code, 200)

    def test_task_page_show_task_list(self):
        """task page show task list"""
        self.client.login(username='admin', password='admin')

        tasks = []
        for i in range(5):
            tasks.append(Task.objects.create(
                title='title%d' % i,
                description='description%d' % i,
                user=User.objects.first()
            ))

        response = self.client.get(reverse('task'))
        for task in tasks:
            self.assertIn(task.title, response.content)
            self.assertIn(task.description, response.content)

    def test_not_logged_in_user_cant_get_task_page(self):
        """test not logged in user redirects to login"""
        response = self.client.get(reverse('task'))

        expected_url = '%s?next=%s' % (reverse('login'), reverse('task'))
        self.assertRedirects(response, expected_url=expected_url,
                             status_code=302, target_status_code=200)

    def test_sort_by_position(self):
        """test task sort by position"""
        self.client.login(username='admin', password='admin')

        for i in range(5):
            Task.objects.create(
                title='title%d' % i,
                description='description%d' % i,
                user=User.objects.first(),
                position=4-i,
            )

        response = self.client.get(reverse('task'))
        matchs = re.findall(ur'<b>(.+)</b>', response.content)

        for task, title in zip(Task.objects.all(), matchs):
            self.assertEquals(task.title, title)


class TaskCreatePageTest(TestCase):
    def test_task_create_page_template_code(self):
        """test create page uses right temlpate, html"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('task_create'))

        self.assertTemplateUsed(response, 'hello/task_create.html')
        self.assertEquals(response.status_code, 200)

    def test_task_create_page_has_form(self):
        """test task create page has task form and it renders"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('task_create'))

        self.assertIsInstance(response.context['form'], TaskForm)
        self.assertIn('id_title', response.content)
        self.assertIn('id_description', response.content)
        self.assertIn('id_status', response.content)

    def test_task_create_page_can_create_tasks(self):
        """test task create page can create tasks"""
        self.client.login(username='admin', password='admin')
        kwargs = dict(
            title="title1",
            description='description1',
            status='0'
        )
        response = self.client.post(reverse('task_create'), kwargs)

        task = Task.objects.first()
        self.assertEquals(task.title, kwargs['title'])
        self.assertEquals(task.description, kwargs['description'])
        self.assertEquals(task.user, User.objects.first())
        self.assertEquals(task.status, '0')
        self.assertRedirects(response, reverse('task'), status_code=302,
                             target_status_code=200)

    def test_not_logged_in_user_cant_get_task_create_page(self):
        """test not logged in user redirects to login"""
        response = self.client.get(reverse('task_create'))

        expected_url = '%s?next=%s' % (
            reverse('login'), reverse('task_create'))
        self.assertRedirects(response, expected_url=expected_url,
                             status_code=302, target_status_code=200)


class TaskUpdatePageTest(TestCase):
    def test_task_update_page_template_code(self):
        """test add page uses right temlpate, html"""
        self.client.login(username='admin', password='admin')
        task = Task.objects.create(
            title='title',
            description='description',
            user=User.objects.first()
        )
        response = self.client.get(reverse('task_update',
                                           kwargs={'pk': task.id}))

        self.assertTemplateUsed(response, 'hello/task_create.html')
        self.assertEquals(response.status_code, 200)

    def test_task_updatepage_has_form(self):
        """test task update page has task form and task data"""
        self.client.login(username='admin', password='admin')
        task = Task.objects.create(
            title='title123',
            description='description123',
            user=User.objects.first()
        )
        response = self.client.get(
            reverse('task_update', kwargs={'pk': task.id}))

        self.assertIsInstance(response.context['form'], TaskForm)
        self.assertIn('id_title', response.content)
        self.assertIn('id_description', response.content)
        self.assertIn('id_status', response.content)
        self.assertIn(task.title, response.content)
        self.assertIn(task.description, response.content)

    def test_task_update_page_can_update_tasks(self):
        """task update page can update tasks"""
        self.client.login(username='admin', password='admin')
        task = Task.objects.create(
            title="title1",
            description='description1',
            user=User.objects.first()
        )
        kwargs = dict(
            title=task.title + '1',
            description=task.description + '1',
            status='1'
        )
        response = self.client.post(
            reverse('task_update', kwargs={'pk': task.id}), kwargs)
        task = Task.objects.first()

        self.assertEquals(task.title, kwargs['title'])
        self.assertEquals(task.description, kwargs['description'])
        self.assertEquals(task.status, kwargs['status'])
        self.assertRedirects(response, reverse('task'), status_code=302,
                             target_status_code=200)

    def test_not_logged_in_user_cant_get_task_update_page(self):
        """test not logged in user redirects to login"""
        task = Task.objects.create(
            title="title1",
            description='description1',
            user=User.objects.first()
        )
        response = self.client.get(
            reverse('task_update', kwargs={'pk': task.id}))

        expected_url = '%s?next=%s' % (
            reverse('login'), reverse('task_update', kwargs={'pk': task.id}))
        self.assertRedirects(response, expected_url=expected_url,
                             status_code=302, target_status_code=200)
