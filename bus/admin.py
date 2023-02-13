from django.contrib import admin

from .models import *
from .forms import TimeAssignModelForm
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError



class CompositionElementFormSet(BaseInlineFormSet):
    def clean(self):
        super(CompositionElementFormSet, self).clean
        
        for (i, form) in enumerate(self.forms): 
            if form.cleaned_data == {}:
                return 

            if i > 0:
                prev = self.forms[i-1].cleaned_data
                current = form.cleaned_data

                if current.get('from_time') >= prev.get('from_time') and \
                current.get('from_time') < prev.get('to_time'):
                    raise ValidationError("Bus runs on same route")



class TimeAssignInline(admin.TabularInline):
    model = TimeAssignModel
    form = TimeAssignModelForm
    
    extra = 0
    formset = CompositionElementFormSet

    
 



class BusAdmin(admin.ModelAdmin):
    inlines = [TimeAssignInline]

class RouteAdmin(admin.ModelAdmin):
    inlines = [TimeAssignInline]


admin.site.register(Bus, BusAdmin)
admin.site.register(Route, RouteAdmin)