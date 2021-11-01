from django.contrib import admin
from .models import Book, Author, BookInstance, Genre, Language


# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.StackedInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') # Отображение формы Админа Авторов
    # fields = ['first_name',  ('date_of_birth', 'date_of_death')] Изменение порядок формы Админ понели про Авторов
    # exclude = ['last_name'] Исключение форму Админа Авторов
    inlines = [BookInline]


class BooksInstanceInline(admin.TabularInline): #StackedInline-вертикальное, TabularInline-горизантальное расположение
    model = BookInstance
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline] # Показать BookInstance в модели Books


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back') # Добавление фильтрация товаров
    fieldsets = (
                (None, {'fields': ('book', 'imprint', 'id')}),
                ('Availability', {'fields': ('status', 'due_back', 'borrower')})
                )


    


