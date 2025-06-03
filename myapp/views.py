from django.shortcuts import render, redirect, get_object_or_404
from .models import Snippet
from .forms import SnippetForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return redirect('snippets')
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('snippets')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('snippets')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def snippets(request):
    snippets = Snippet.objects.filter(user=request.user)
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
            messages.success(request, 'Snippet created successfully')
            return redirect('snippets')
    else:
        form = SnippetForm()

    query = request.GET.get('q', '')
    tags = request.GET.get('tags', '')

    if query:
        snippets = snippets.filter(title__icontains=query)
    if tags:
        tag_list = tags.split(',')
        for tag in tag_list:
            snippets = snippets.filter(tags__icontains=tag.strip())    
    
    return render(request, 'snippets/snippets.html', {
        'snippets': snippets,
        'form': form,
        'query': query,
        'tags': tags
    })

@login_required
def edit_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Snippet update sucessfully')
            return redirect('snippets')
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/edit_snippet.html', {'form': form, 'snippet': snippet})

@login_required
def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    if request.method == 'POST':
        snippet.delete()
        messages.success(request, 'Snippet deleted sucessfully')
        return redirect('snippets')
    return render(request, 'snippets/delete_snippet.html', {'snippet': snippet})


@login_required
def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk, user=request.user)
    # Process tags before sending to template
    snippet.tag_list = [tag.strip() for tag in snippet.tags.split(',') if tag.strip()]
    return render(request, 'snippets/snippet_detail.html', {'snippet': snippet})
                      
