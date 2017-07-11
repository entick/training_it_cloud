from django.contrib import admin
from django.contrib.auth.models import User
from .models import Coach
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class IsStaffFilter(admin.SimpleListFilter):

    title = 'is staff'

    parameter_name = 'is staff'

    def lookups(self, request, model_admin):
        return (
            ('True', 'True'),
            ('False', 'False'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return  queryset.filter(user=User.objects.filter(is_staff=True))
        if self.value() == 'False':
            return  queryset.filter(user=User.objects.filter(is_staff=False))

class CoachAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'gender', 'skype', 'description')
    list_filter = (IsStaffFilter,)




admin.site.register(Coach, CoachAdmin)
