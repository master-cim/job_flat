from django.contrib import admin


from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'created', 'author', 'post', 'parent_comm')
    search_fields = ('author', 'parent_comm')
    list_filter = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

