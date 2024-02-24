from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import *
from .forms import *
def project_list(request):
    project = Project.objects.all()
    
    return render(request, "pages/project_details.html", {"projects": project})

def newProject(request, group_id=None):
    groupObj = None
    if request.method == 'POST':
        group_form = NewProjectForm(request.POST)
        if group_form.is_valid():
           groupF = group_form.save()
           groupF.save()
           return HttpResponseRedirect('/pages/list/')
    else:
        if request.method == 'GET':
            if group_id:
                groupObj = Project.objects.get(pk=group_id)
                #Only Task creater can make task Public or Private
                group_form = NewProjectForm(instance=groupObj)
            else:
                group_form = NewProjectForm()

    return render(request, 'pages/NewProject.html', {'GroupForm_form': group_form,
                                                              'groupobj': groupObj, })

def newCulture(request, group_id=None):
    groupObj = None
    if request.method == 'POST':
        group_form = CultureForm(request.POST)
        if group_form.is_valid():
           groupF = group_form.save()
           groupF.save()
           return HttpResponseRedirect('/pages/list/')
    else:
        if request.method == 'GET':
            if group_id:
                groupObj = Cultures.objects.get(pk=group_id)
                #Only Task creater can make task Public or Private
                group_form = CultureForm(instance=groupObj)
            else:
                group_form = CultureForm()

    return render(request, 'pages/NewCulture.html', {'GroupForm_form': group_form,
                                                              'groupobj': groupObj, })

def culture_list(request):
    cultures = Cultures.objects.all()
    
    return render(request, "pages/culture_details.html", {"cultures": cultures})


def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "pages/project_index.html", context)

def home(request):
    return render(request, "pages/home.html", {})

def books(request):
    return render(request, "pages/books.html", {})