from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Voca
from .models import Today


@admin.register(Voca)
class VocaAdmin(ImportExportModelAdmin):
    pass


@admin.register(Today)
class TodayAdmin(ImportExportModelAdmin):
    pass