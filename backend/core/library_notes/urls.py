

from django.urls import path

from library_notes import views as vs


urlpatterns = [
    path('', vs.notes_index, name='notes-index'),
    path('theme/<int:theme_id>/', vs.get_theme, name='get-theme'),
    path('theme/add/', vs.add_theme, name='add-theme'),
    path('content/<int:content_id>/', vs.get_content, name='get-content'),
    path('content/add/', vs.content_add, name='add-content'),

]



