from django.contrib import admin

from .models import Birthday


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday')
    search_fields = ('first_name', 'last_name')
    list_filter = ('birthday',)

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('birthday')
