from django.contrib import admin
from .models import Companies


@admin.register(Companies)                  #Админка
class AdminCompanies(admin.ModelAdmin):
    list_display = ["CompanyName", "AddressCompany"]
# Register your models here.
