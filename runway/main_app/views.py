from django.shortcuts import render
from django.http import HttpResponse
from .forms import RunwayForm

def index(request):
	form = RunwayForm()
	return render(request, 'index.html', {'form' : form})

def result(request):
	form = RunwayForm(request.GET)
	if form.is_valid():
		nd35 = float(form.cleaned_data['nd35'])
		nlod = float(form.cleaned_data['nlod'])
		elod = float(form.cleaned_data['elod'])
		tod1 = 1.15 * nd35
		cl1 = 0.5*(tod1 - 1.15*(nlod))
		if cl1>1000:
			cl1 = 1000
		tor1 = tod1 - cl1
		tod2 = float(form.cleaned_data['ed35'])
		cl2 = 0.5*(tod2 - elod)
		if cl2>1000:
			cl2 = 1000
		tor2 = tod2 - cl2
		das = float(form.cleaned_data['efdas'])
		sd = float(form.cleaned_data['nlsd'])
		ld = sd/0.6
		fl = max(tod1, tod2, das, ld)
		fs = max(tor1, tor2, ld)
		sw = das - fs
		cl = min(fl-das, cl1, cl2)
		runl = fs + 2*sw
		context = {'fl' : fl, 'fs' : fs, 'sw' : sw, 'cl' : cl, 'runl' : runl}
	return render(request, 'result.html', context)



