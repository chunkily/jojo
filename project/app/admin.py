from django.contrib import admin

from .models import Away
from .models import Holiday
from .models import Project
from .models import ProjectUser
from .models import StandUpReport

admin.site.register(Away)
admin.site.register(Holiday)
admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(StandUpReport)
