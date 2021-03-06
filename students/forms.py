import django_filters
from django.forms import ModelForm

from students.models import Students


class StudentsBaseForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    @staticmethod
    def normalize_phone_number(value):
        if value is not None:
            return ''.join(c for c in value if c.isdigit() or c == '+')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    def clean_email(self):
        email = self.cleaned_data['email']
        result = email.lower()
        return result

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        result = self.normalize_phone_number(phone_number)
        return result


class StudentsCreateForm(StudentsBaseForm):
    pass


class StudentsUpdateForm(StudentsBaseForm):
    pass


class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = Students
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
