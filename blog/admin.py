from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "publish_date"
    list_display = ("title", "publish_date", "published", "author")
    list_editable = ("published", )
    list_filter = ("published", )
    search_fields = ("title", )


admin.site.site_header = admin.site.site_title = "Beginnen met Django Blog"
admin.site.index_title = "Administratie"
