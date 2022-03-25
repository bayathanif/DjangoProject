from django.contrib import admin
from . import models

# Register your models here.

class BookInline(admin.TabularInline):
    model = models.Book

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    fieldsets = (
        ('مشخصات', {
            'fields': ('first_name', 'last_name')
        }),
        ('تاریخ ها', {
            'fields': ('date_of_birth', 'date_of_death')
        }),
    )
    inlines = [BookInline]



@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author' , 'display_genre')
    list_filter = ('title' , 'author')


@admin.register(models.BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status')
    list_filter = ('book', 'status')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass



