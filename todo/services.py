import datetime
from django.core.exceptions import ValidationError
from .models import Project, Task, Employee

class ProjectService:
    @staticmethod
    def get_all_projects():
        return Project.objects.all()

    @staticmethod
    def create_project(project_id, name, description=None, manager_id=None, budget=None):
        if not project_id or len(project_id) > 10:
            raise ValidationError("ID проєкту має бути заповнений та містити не більше 10 символів.")
        if Project.objects.filter(project_id=project_id).exists():
            raise ValidationError(f"Проєкт з ID {project_id} вже існує в базі даних.")
        
        project = Project.objects.create(
            project_id=project_id,
            name=name,
            description=description,
            manager_id=manager_id,
            start_date=datetime.datetime.now(),
            budget=budget,
            expenses=0.0000
        )
        return project


class KanbanBoardService:
    KANBAN_STATUSES = ['Backlog', 'To Do', 'In Progress', 'Review', 'Done']

    @classmethod
    def get_board_structure(cls, project_id):
        try:
            project = Project.objects.get(project_id=project_id)
        except Project.DoesNotExist:
            raise ValidationError("Запитуваний проєкт не знайдено в системі.")

        all_tasks = Task.objects.filter(project=project).select_related('employee')
        board_data = {status: [] for status in cls.KANBAN_STATUSES}

        for task in all_tasks:
            if task.status in board_data:
                board_data[task.status].append(task)
            else:
                board_data['Backlog'].append(task)

        return {
            'project': project,
            'board_data': board_data
        }


class TaskService:
    @staticmethod
    def create_task(task_id, project_id, name, description='', priority='Середній', deadline=None, employee_id=None):
        if not task_id or len(task_id) > 10:
            raise ValidationError("ID завдання має містити не більше 10 символів.")
        if Task.objects.filter(task_id=task_id).exists():
            raise ValidationError(f"Завдання з ID {task_id} вже існує.")

        project = Project.objects.get(project_id=project_id)
        employee = Employee.objects.filter(employee_id=employee_id).first() if employee_id else None

        task = Task.objects.create(
            task_id=task_id,
            project=project,
            employee=employee,
            name=name,
            description=description,
            status='To Do',
            priority=priority,
            deadline=deadline if deadline else datetime.datetime.now() + datetime.timedelta(days=7)
        )
        return task

    @staticmethod
    def move_task(task_id, new_status):
        if new_status not in KanbanBoardService.KANBAN_STATUSES:
            raise ValidationError("Передано некоректний статус для Kanban-колонки.")

        try:
            task = Task.objects.get(task_id=task_id)
            task.status = new_status
            task.save()
            return True
        except Task.DoesNotExist:
            return False