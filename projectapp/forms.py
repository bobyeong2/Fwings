from django.forms import ModelForm, models

from projectapp.models import Project


class ProjectCreationForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'image', 'description']
