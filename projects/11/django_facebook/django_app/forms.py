from django import forms
from django.contrib import admin
# from ckeditor.widgets import CKEditorWidget
from django_app import models


# class PostAdminForm(forms.ModelForm):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'text-danger form-control'}))
#     content = forms.CharField(widget=CKEditorWidget(config_name="awesome_ckeditor"))
#
#     class Meta:
#         model = models.PostModel
#         fields = '__all__'


# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm
#
#
# admin.site.register(models.PostModel, PostAdmin)
