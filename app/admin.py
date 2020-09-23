from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Voca

@admin.register(Voca)
class VocaAdmin(ImportExportModelAdmin):
    pass