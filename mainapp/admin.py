from django.contrib import admin
from mainapp import models
# Register your models here.

admin.site.register([
    models.appuser,
    models.doubts,
    models.solution,
    models.book,
    models.contact,
    models.extra_info,
    models.reviews
    ])
