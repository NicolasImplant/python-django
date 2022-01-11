from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import SignupForm
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Create your views here.

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    slug_field  = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""

        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user = user).order_by('-created')

        return context


class SignupView(FormView):
    """Users sign up view"""

    template_name = 'users/signup.html'
    form_class    = SignupForm
    success_url   = reverse_lazy('users:Login') 

    def form_valid(self, form):
        """Save form data."""

        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update user profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['webside', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile
    
    def get_success_url(self):
        """Return to user's profile"""

        username = self.object.user.username
        return reverse('users:detail', kwargs = {'username': username})





def login_view(request):
    """Login View"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts:Feed')
        else:
            return render(request, 'users/login.html', {'error':'Invalid username or password'})

    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout view"""
    logout(request)
    return redirect('users:Login')
