from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Subject, Attendance

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'user_type', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['user_type', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']
    
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Type', {'fields': ('user_type',)}),
    )

# Subject Admin
class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ['name', 'teacher', 'get_teacher_email', 'get_student_count', 'get_attendance_count']
    list_filter = ['teacher']
    search_fields = ['name', 'teacher__username']
    raw_id_fields = ['teacher']
    
    def get_teacher_email(self, obj):
        return obj.teacher.email
    get_teacher_email.short_description = 'Teacher Email'
    
    def get_student_count(self, obj):
        # Count unique students who have attendance records for this subject
        return Attendance.objects.filter(subject=obj).values('student').distinct().count()
    get_student_count.short_description = 'Students'
    
    def get_attendance_count(self, obj):
        return Attendance.objects.filter(subject=obj).count()
    get_attendance_count.short_description = 'Attendance Records'

# Attendance Admin
class AttendanceAdmin(admin.ModelAdmin):
    model = Attendance
    list_display = ['student', 'subject', 'date', 'is_present', 'get_teacher']
    list_filter = ['subject', 'date', 'is_present', 'subject__teacher']
    search_fields = ['student__username', 'subject__name', 'date']
    date_hierarchy = 'date'
    raw_id_fields = ['student', 'subject']
    
    def get_teacher(self, obj):
        return obj.subject.teacher.username
    get_teacher.short_description = 'Teacher'

# Inline for Attendance in Student detail view
class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 0
    readonly_fields = ['subject', 'date', 'is_present']
    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False

# Custom filters for user types
class StudentFilter(admin.SimpleListFilter):
    title = 'user type'
    parameter_name = 'user_type'
    
    def lookups(self, request, model_admin):
        return (
            ('student', 'Students'),
            ('teacher', 'Teachers'),
        )
    
    def queryset(self, request, queryset):
        if self.value() == 'student':
            return queryset.filter(user_type='student')
        if self.value() == 'teacher':
            return queryset.filter(user_type='teacher')

# Action for bulk marking attendance
def mark_present(modeladmin, request, queryset):
    queryset.update(is_present=True)
mark_present.short_description = "Mark selected attendance as present"

def mark_absent(modeladmin, request, queryset):
    queryset.update(is_present=False)
mark_absent.short_description = "Mark selected attendance as absent"

# Enhanced Attendance Admin with actions
class EnhancedAttendanceAdmin(AttendanceAdmin):
    actions = [mark_present, mark_absent]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.has_perm('attendance.change_attendance'):
            del actions['mark_present']
            del actions['mark_absent']
        return actions

# Register models - ONLY ONCE
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Attendance, EnhancedAttendanceAdmin)