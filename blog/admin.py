from django.contrib import admin

from blog.models import Category, Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "publish_date"
    list_display = ("title", "publish_date", "published", "author")
    list_editable = ("published", )
    list_filter = ("published", )
    search_fields = ("title", )


@admin.register(Category)
class Category(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "is_approved")
    list_editable = ("is_approved", )
    list_filter = ("is_approved", )


admin.site.site_header = admin.site.site_title = "Beginnen met Django Blog"
admin.site.index_title = "Administratie"
