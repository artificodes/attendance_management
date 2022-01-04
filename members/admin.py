from django.contrib import admin
from members import models as gmodels
admin.site.register(gmodels.Member)
admin.site.register(gmodels.HostedEvent)
admin.site.register(gmodels.Event)
admin.site.register(gmodels.EventTicket)
admin.site.register(gmodels.EventImage)
admin.site.register(gmodels.EventCenterCategory)
admin.site.register(gmodels.EventSpecialOffer)
admin.site.register(gmodels.Registration)
admin.site.register(gmodels.Arrangement)
admin.site.register(gmodels.EventDay)
admin.site.register(gmodels.LraMembersBiodata)
