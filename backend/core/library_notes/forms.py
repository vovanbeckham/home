from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from library_notes.models import Content


class ContentForm(forms.ModelForm):
      """Form for comments to the article."""

      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["content"].required = False

      class Meta:
          model = Content
          fields = ("theme", "name", "content")
          widgets = {
              "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="comment"
              )
          }

