from django.db import models

# Create your models here.


class Project(models.Model):
    # writer = models.ForeignKey(User, on_delete=models.SET_NULL,
    #                            related_name='project', null=True)
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateField(auto_created=True, null=True)