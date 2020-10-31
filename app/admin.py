from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Voca, Today, Profile


@admin.register(Voca)
class VocaAdmin(ImportExportModelAdmin):
    pass


@admin.register(Today)
class TodayAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Profile)