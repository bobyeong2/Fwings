from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from commentapp.forms import CommentCreationForm
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25


class ProjectDeleteView(DeleteView):
    model = Project
    context_object_name = 'target_project'
    success_url = reverse_lazy('projectapp:list')
    template_name = 'projectapp/delete.html'


class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    form_class = CommentCreationForm
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25


    def get_context_data(self, **kwargs):

        project = self.object
        user = self.request.user

        if user.is_authenticated :
            subscription = Subscription.objects.filter(user=user,
                                                       project=project)

        else:
            subscription = None

        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(
            subscription=subscription,
            object_list=object_list, **kwargs)


class ProjectUpdateView(UpdateView):
    model = Project
    context_object_name = 'target_project'
    form_class = ProjectCreationForm
    template_name = 'projectapp/update.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})
