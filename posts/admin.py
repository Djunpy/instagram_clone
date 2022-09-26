from django.contrib import admin

from .models import Post, Follow, Stream, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'like_count', 'created', 'published')
    list_filter = ('published', 'created', 'tags')
    list_editable = ('published',)

    def like_count(self, obj):
        return obj.liked.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Follow)
admin.site.register(Stream)
