from django.contrib import admin

from categories.admin import CategoryBaseAdmin

from .models import Term

class TermAdmin(CategoryBaseAdmin):
    pass

admin.site.register(Term, TermAdmin)
