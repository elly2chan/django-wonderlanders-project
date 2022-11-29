class AddStyleClassFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (key, field) in self.fields.items():
            if 'class' not in field.widget.attrs or 'style' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
                field.widget.attrs['style'] = ''
            field.widget.attrs['class'] += 'form-control'
            field.widget.attrs['style'] += 'max-width: 300px; resize: none'


class RemoveLabelsFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key not in ['category', 'country']:
                field.label = ""


class AddPlaceholdersFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if key not in ['password', 'password1', 'password2']:
                field.widget.attrs['placeholder'] = key.upper().replace('_', ' ')
