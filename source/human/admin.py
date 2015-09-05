from django.contrib import admin

# Register your models here.
from .forms import UserForm
from .models import Phone, Offender, User, State, Problem


class OffenderAdmin(admin.ModelAdmin):

    list_display = ["__unicode__", "name", "location", "person_image"]

    class Meta:

        model = Offender


class UserAdmin(admin.ModelAdmin):

    form = UserForm

    # class Meta:
    #
    #     model = User


admin.site.register(Phone)
admin.site.register(State)
admin.site.register(Problem)
admin.site.register(Offender, OffenderAdmin)
admin.site.register(User, UserAdmin)



