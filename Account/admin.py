from django.contrib.auth.admin import UserAdmin as BaseUserAdmin,admin
from .forms import UserChangeForm,UserCreationForm
from .models import User, Otp, OtpCode, Address
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["phone", "fullname","email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["phone", "password"]}),
        ("اطلاعات شخصی", {"fields": ["profile","fullname", "email"]}),
        ("دسترسی ها", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["phone", "fullname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["phone"]
    ordering = ["phone"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Otp)
admin.site.register(OtpCode)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "fullname", "phone", "email","postal_code","address"]
