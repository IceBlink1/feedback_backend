import django.contrib.admin as admin

from fb_backend.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("feedback", "author")
