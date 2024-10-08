from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Postes
from .forms import FormUser, FormConnect, FormPost
from  django.views.generic import ListView, CreateView
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
#from .models import MonModele

# Create your views here.
def bonjour(request):
    return render(request, 'index.html')

def singin(request):
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        form = FormUser()
    else:
        form = FormUser()
    return render(request, 'inscription.html', {"forms": form})


def connect(request):
    if request.method == 'POST':
        form = FormConnect(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'identifiants incorrect!')
    else:
        form = FormConnect()
    return render(request, 'connect.html', {'forms':form})

class UserListView(ListView):
    model = User
    template_name = "Users.html"
    context_object_name = 'users'

    def get_queryset(self):
        query = super().get_queryset()
        data = User.objects.all()
        return query



def modifier(request, user_id):
    objet = User.objects.get(id=user_id)
    form = FormUser(request.POST or None, instance=objet)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'modify.html', {'forms': form})

def supprimer(request, user_id):
    objet = User.objects.get(id = user_id)
    objet.delete()
    return redirect('')

#Pour soumettre un nouveau poste
def creat_post(request):
    if request.method == 'POST':
        form = FormPost(request.POST, request.FILES)
        if form.is_valid():
            poste=form.save(commit=False)
            poste.utilisateur=request.user
            return redirect('affichage')
        form = FormPost()
    else:
        form = FormPost()
    return render(request, 'post_form.html', {'forms': form})

#class CreatePost(CreateView):
   # model = Postes
   # form_class = FormPost
   # template_name = 'post_form.html'
  # success_url = reverse_lazy('affichage')

  # def form_valid(self, form):
   #    poste = form.save()

#Vue pour afficher les postes
def see_postes(request):
    postes = Postes.objects.all()
    return render(request, 'affichage.html', {'postes': postes})