from hello_polls.models import MyPoll
from django.contrib import admin
from hello_polls.models import MyChoice

class ChoiceInline(admin.TabularInline):
    model = MyChoice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
    fieldsets=[
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
       
admin.site.register(MyPoll,PollAdmin)    
