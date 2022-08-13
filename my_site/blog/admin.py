from django.contrib import admin
from blog.models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created', 'modified', 'publish', 'status', 'review_status')
    list_filter = ('status', 'review_status', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)



