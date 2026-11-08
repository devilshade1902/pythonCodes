from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header= 'Dhruv pet store'
admin.site.site_title= 'my pet store'

admin.site.register(models.Pet)
admin.site.register(models.Pet_Store)
admin.site.register(models.Pet_products)



