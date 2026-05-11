from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'user', 'department', 'semester', 'cgpa', 'is_active')
    list_filter = ('department', 'semester', 'grade', 'is_active')
    search_fields = ('roll_number', 'user__first_name', 'user__email')
    readonly_fields = ('enrollment_date',)
    fieldsets = (
        ('User Info', {
            'fields': ('user',)
        }),
        ('Academic Info', {
            'fields': ('roll_number', 'department', 'semester', 'cgpa', 'grade')
        }),
        ('Personal Info', {
            'fields': ('phone', 'date_of_birth', 'address')
        }),
        ('Status', {
            'fields': ('is_active', 'enrollment_date')
        }),
    )
