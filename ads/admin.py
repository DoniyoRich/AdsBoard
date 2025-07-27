from django.contrib import admin

from .models import Ad, Feedback


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ("id", "title", "price", "author", "created_at")
    list_filter = ("id", "title", "price", "author", "created_at")
    search_fields = ("id", "title", "price", "author", "created_at")


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ("id", "text", "author", "ad", "created_at")
    list_filter = ("id", "text", "author", "ad", "created_at")
    search_fields = ("id", "text", "author", "ad", "created_at")

    # не выводим в раскрывающемся списке самого себя
    # чтобы исключить возможность оставлять себе отзыв
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if obj is None:
            form.base_fields["author"].queryset = form.base_fields["author"].queryset.exclude(id=request.user.id)

        return form
