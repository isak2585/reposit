from django.contrib import admin
from .models import db01


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "phone", "joined_date",)


admin.site.register(db01, MemberAdmin)
