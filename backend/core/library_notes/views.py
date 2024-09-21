
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse

from library_notes.forms import ContentForm, ThemeForm
from library_notes.models import Content, Theme



def notes_index(request):
    contents = Content.objects.all().order_by('-pk')[:10]
    return render(request, "library_notes/notes.html", locals())



def get_theme(request, theme_id):
    theme_id = int(theme_id)
    theme = Theme.objects.get(pk=theme_id)
    contents = Content.objects.filter(theme=theme)
    return render(request, "library_notes/gettheme.html", locals())


def add_theme(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            id = obj.id
            url = reverse('add-content')+"?id=" + str(id)
            messages.success(request, 'OK')
            return redirect(url)
    else:
        form = ThemeForm()
    return render(request, "library_notes/add_theme.html", locals())


def get_content(request, content_id):
    content_id = int(content_id)
    content = Content.objects.get(id=content_id)
    return render(request, "library_notes/get_content.html", locals())


def content_add(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Доступ запрещен!')
        return redirect('notes-index')
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        id = request.GET.get('id', None)
        form = ContentForm()
        form.fields['theme'].initial = id
    return render(request, "library_notes/add_content.html", locals())