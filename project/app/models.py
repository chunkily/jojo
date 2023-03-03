from django.db import models


# System can support multiple projects
# Each project has a standup conducted regularly at a certain time, typically daily
class Project(models.Model):
    name = models.CharField(max_length=200)
    standup_schedule = models.CharField(
        max_length=500
    )  # Stored as an iCalendar recurrence rule?


# Each project has multiple staff who should report
class ProjectUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    userid = models.CharField(max_length=200)


class StandUpReport(models.Model):
    userid = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    submitted_on = models.DateTimeField()
    what_you_did = models.TextField(max_length=1000)
    what_you_plan_to_do = models.TextField(max_length=1000)
    blockers = models.TextField(max_length=1000)
    others = models.TextField(max_length=1000)


class Away(models.Model):
    userid = models.CharField(max_length=200)
    start_on = models.DateTimeField()
    end_on = models.DateTimeField()


class Holiday(models.Model):
    start_on = models.DateTimeField()
    end_on = models.DateTimeField()


# Allow for soft delete restoration
class Deleted(models.Model):
    deleted_on = models.DateTimeField()
    obj_json = models.JSONField()
