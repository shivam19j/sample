from django import forms

class RunwayForm(forms.Form):
	nlod = forms.DecimalField(label='Normal Take Off Lift-off Distance', max_digits=100)
	nd35 = forms.DecimalField(label='Normal Take off D35', max_digits=100)
	elod = forms.DecimalField(label='Engine Failure Lift-off Distance', max_digits=100)
	ed35 = forms.DecimalField(label='Engine Failure D35', max_digits=100)
	efdas = forms.DecimalField(label='Engine Failure Aborted Take-off DAS', max_digits=100)
	nlsd = forms.DecimalField(label='Normal Landing Stop Displace', max_digits=100)