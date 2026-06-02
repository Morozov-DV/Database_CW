from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=10, primary_key=True, db_column='TeamID')
    name = models.CharField(max_length=50, db_column='TeamName')
    description = models.TextField(blank=True, null=True, db_column='TeamDescription')
    leader_id = models.CharField(max_length=10, blank=True, null=True, db_column='TeamLeaderID')
    members = models.TextField(blank=True, null=True, db_column='TeamMembers')

    class Meta:
        managed = False
        db_table = 'TEAMS'

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_id = models.CharField(max_length=10, primary_key=True, db_column='EmployeeID')
    first_name = models.CharField(max_length=30, db_column='EmployeeFirstName')
    last_name = models.CharField(max_length=30, db_column='EmployeeLastName')
    skills = models.TextField(blank=True, null=True, db_column='EmployeeSkills')
    team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True, db_column='TeamID')

    class Meta:
        managed = False
        db_table = 'EMPLOYEES'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    project_id = models.CharField(max_length=10, primary_key=True, db_column='ProjectID')
    name = models.CharField(max_length=50, db_column='ProjectName')
    description = models.TextField(blank=True, null=True, db_column='ProjectDescription')
    manager_id = models.CharField(max_length=10, blank=True, null=True, db_column='ProjectManagerID')
    start_date = models.DateTimeField(blank=True, null=True, db_column='ProjectStartDate')
    end_date = models.DateTimeField(blank=True, null=True, db_column='ProjectEndDate')
    budget = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, db_column='Budget')
    expenses = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, db_column='Expenses')

    class Meta:
        managed = False
        db_table = 'PROJECTS'

    def __str__(self):
        return self.name


class Milestone(models.Model):
    milestone_id = models.CharField(max_length=10, primary_key=True, db_column='MilestoneID')
    project = models.ForeignKey(Project, models.CASCADE, db_column='ProjectID')
    name = models.CharField(max_length=50, db_column='MilestoneName')
    start_date = models.DateTimeField(blank=True, null=True, db_column='MilestoneStartDate')
    end_date = models.DateTimeField(blank=True, null=True, db_column='MilestoneEndDate')
    status = models.CharField(max_length=20, blank=True, null=True, db_column='MilestoneStatus')

    class Meta:
        managed = False
        db_table = 'MILESTONES'

    def __str__(self):
        return self.name


class Task(models.Model):
    task_id = models.CharField(max_length=10, primary_key=True, db_column='TaskID')
    project = models.ForeignKey(Project, models.CASCADE, db_column='ProjectID')
    employee = models.ForeignKey(Employee, models.SET_NULL, blank=True, null=True, db_column='EmployeeID')
    name = models.CharField(max_length=50, db_column='TaskName')
    description = models.TextField(blank=True, null=True, db_column='TaskDescription')
    status = models.CharField(max_length=20, blank=True, null=True, db_column='TaskStatus')
    priority = models.CharField(max_length=10, blank=True, null=True, db_column='TaskPriority')
    deadline = models.DateTimeField(blank=True, null=True, db_column='TaskDeadline')

    class Meta:
        managed = False
        db_table = 'TASKS'

    def __str__(self):
        return self.name