from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BrewForm
from .models import Brew

@login_required
def brew_list(request):
  brews = Brew.objects.all()
  return render(request, 'brews/brew_list.html', {'brews': brews})

@login_required
def brew_detail(request, pk):
  brew = get_object_or_404(Brew, pk=pk)
  return render(request, 'brews/brew_detail.html', {'brew': brew})

@login_required
def brew_new(request):
  if request.method == "POST":
    form = BrewForm(request.POST)
    if form.is_valid():
      brew = form.save(commit=False)
      brew.save()
      return redirect('brew_detail', pk=brew.pk)
  else:
    form = BrewForm()
  return render(request, 'brews/brew_edit.html', {'form': form})

@login_required
def brew_edit(request, pk):
  brew = get_object_or_404(Brew, pk=pk)
  if request.method == "POST":
    form = BrewForm(request.POST, instance=brew)
    if form.is_valid():
      brew = form.save(commit=False)
      brew.save()
      return redirect('brew_detail', pk=brew.pk)
  else:
    form = BrewForm(instance=brew)
  return render(request, 'brews/brew_edit.html', {'form': form})
