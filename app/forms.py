from django import forms 


from app.models import user

class userForm(forms.ModelForm):
    class Meta:
        model = user

        fields = '__all__'

    








