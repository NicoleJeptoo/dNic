from django import forms
from Nicole.models import course

class CourseForm(forms.ModelForm):
    class Meta:
        model = course
        fields = 'title','description','instructor'
        widgets ={
            'tittle':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter course title'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter course description'}),
            'instructor':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter course instructor'}),

        }
