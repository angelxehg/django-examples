from django.contrib import admin
from bookstore.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'descr')


admin.site.register(Book, BookAdmin)
