from django.forms import ModelForm, CharField, TextInput, Textarea, BooleanField, CheckboxInput

from .models import Todo


class TodoForm(ModelForm):
    title = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=250, widget=Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Todo
        fields = ('title', 'description')


class UpdateForm(ModelForm):
    title = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=250, widget=Textarea(attrs={"class": "form-control"}))
    completed = BooleanField(widget=CheckboxInput(attrs={"class": "form-check-input"}))

    class Meta:
        model = Todo
        fields = ('title', 'description', 'completed')
