from django.contrib import admin
from .models import Trip, Expense

# Inline model for Expense
class ExpenseInline(admin.TabularInline):  # You can also use admin.StackedInline
    model = Expense
    extra = 1  # Number of empty forms to display for adding expenses
    fields = ('title', 'amount', 'category')  # Fields to display in the inline form

# Trip Admin customization
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'budget', 'code', 'created_at')  # Columns to display in the list view
    search_fields = ('title',)  # Enable search by title
    list_filter = ('created_at',)  # Filter trips by creation date
    ordering = ('-created_at',)  # Order by creation date descending
    inlines = [ExpenseInline]  # Show expenses inline within the trip admin

# Expense Admin customization
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'trip', 'created_at')  # Columns to display in the list view
    list_filter = ('category', 'trip')  # Filter expenses by category and trip
    search_fields = ('title',)  # Enable search by title
    ordering = ('-created_at',)  # Order by creation date descending

# Register your models here
admin.site.register(Trip, TripAdmin)
admin.site.register(Expense, ExpenseAdmin)