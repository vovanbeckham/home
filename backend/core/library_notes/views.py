from django.shortcuts import render

from library_notes.forms import ContentForm
from library_notes.models import Content, Theme



def notes_index(request):
    contents = Content.objects.all().order_by('-pk')[:10]
    return render(request, "library_notes/notes.html", locals())



def get_theme(request, theme_id):
    print(theme_id)
    theme_id = int(theme_id)
    theme = Theme.objects.get(pk=theme_id)
    contents = Content.objects.filter(theme=theme)
    print(contents)
    return render(request, "library_notes/gettheme.html", locals())


def add_theme(request):
    return render(request, "library_notes/index.html", locals())


def get_content(request, content_id):
    content_id = int(content_id)
    content = Content.objects.get(id=content_id)
    return render(request, "library_notes/get_content.html", locals())


def content_add(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        print(1)
        if form.is_valid():
            print(2)
            form.save()
    else:
        form = ContentForm()
    return render(request, "library_notes/add_content.html", locals())