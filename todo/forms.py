from django import forms

class TodoForm(forms.Form):
	text = forms.CharField(max_length=80,
		widget = forms.TextInput(
			attrs={'class' : 'form-control', 'placeholder' : 'Enter todo e.g. Finish your Assignment!', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn'}))


