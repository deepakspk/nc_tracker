from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy
from . import models
from . forms import AdminForm
from . import forms
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from bp_ecm.settings import EMAIL_HOST_USER


# Create your views here.
# create a view that authenticate user with email
def email_login_view(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
        else:
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')

class AdminView(CreateView):
    template_name = 'accounts/admins.html'
    form_class = AdminForm
    success_url = reverse_lazy("accounts:admins")

    def form_valid(self, form_class):
        password = "NCM12345"
        email = self.request.POST['email']
        newuser = User.objects.create_user(email, email, password)
        form_class.instance.user = newuser    
        return super().form_valid(form_class)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = AdminForm()
        admins = models.Admin.objects.all().order_by('-id')
        context['admins'] = admins      
        return context


class AdminUpdateView(UpdateView):
    model = models.Admin
    form_class = AdminForm
    template_name='accounts/admin_update.html'
    success_url = reverse_lazy("accounts:admins")


class AdminDeleteView(DeleteView):
    model = models.Admin
    success_url = reverse_lazy("accounts:admins")

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'hris.nepalcangroup.com',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, 
                            email, EMAIL_HOST_USER, [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("accounts:password_reset_done")
	password_reset_form = forms.PasswordResetForm()
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})
