from django.contrib import admin
from .models import education_model,ContactMessages,Experience,MyProjects
from .models import Achievements,TechnicalSkills,interpersonalSkills
# Register your models here.

admin.site.register(education_model)
admin.site.register(ContactMessages)
admin.site.register(Experience)
admin.site.register(MyProjects)
admin.site.register(interpersonalSkills)
admin.site.register(TechnicalSkills)
admin.site.register(Achievements)