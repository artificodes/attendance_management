from django.contrib import admin
from children import models as chmodels
admin.site.register(chmodels.Parent)
admin.site.register(chmodels.Dependant)
admin.site.register(chmodels.LraMembersChildren)
admin.site.register(chmodels.General)
admin.site.register(chmodels.Administrator)
admin.site.register(chmodels.Guardian)
admin.site.register(chmodels.Teacher)
admin.site.register(chmodels.Group)
admin.site.register(chmodels.ClassRoomRegistration)
admin.site.register(chmodels.ClassRoom)
admin.site.register(chmodels.Article)
