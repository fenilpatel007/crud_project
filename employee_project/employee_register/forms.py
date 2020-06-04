from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('fullName', 'empCode', 'mobileNo', 'position')  # To display all fields on form, use fields = '__all__'
        labels = {
            'fullName': 'Full Name',
            'empCode': 'EMP. CODE'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['empCode'].required = False
