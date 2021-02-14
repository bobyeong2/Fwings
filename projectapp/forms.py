from django.forms import ModelForm, models

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    created_at = models.DateField(auto_created=True, null=True)

    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'created_at']
        ordering = ['created_at']
