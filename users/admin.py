from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin



CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None,{'fields':('email','password',)}),
        ('Personal_info',{'fields':('first_name','last_name','birth_date','gender',)},),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions',)},),
        ('Important dates',{'fields':("last_login","date_joined",)},),

    )
    add_fieldsets=(
        (None,{'classes':("wide",),'fields':("first_name","last_name","email","password1","password2","birth_date","gender"),},),
        )
    list_display = ("first_name","last_name","email","birth_date","gender",'is_staff',)
    search_fields =("first_name","last_name","email","birth_date","gender",'is_staff')
    ordering =("email",)
    