from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .forms import PersonForm , RentForm
from .models import Person , User , Rent , Car


from django.shortcuts import render
# Create your views here.

# class CreateProfileView(CreateView):
# 	queryset = User()
# 	template_name='user.html'
# 	form_class = UserForm
# 	success_url = '/admin'

# class CreatePersonView(CreateView):
# 	queryset = Person()
# 	template_name='create.html'
# 	form_class = PersonForm
# 	success_url = '/admin'

class CreateRentView(CreateView):
	queryset = Rent() ,Car()
	template_name='rent.html'
	form_class = RentForm
	success_url = '/profiles/'

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(CreateRentView, self).form_valid(form)
 

# class ListPersonView(ListView):
# 		model = Person
# 		template_name='list.html'

class ListCarView(ListView):
		model = Car
		template_name='Car.html'

def TestPage(request):
	if(request.method == 'GET'):
		print ('Test GET method')
	return render(request,"test.html")




# def login(request):
#     if request.method == 'POST':
#         print('dfsasfas')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if  login(request, user) :
#             request.session['username'] = username
#             return redirect('/admin')
#         else:
#             messages.error(request, 'Error wrong username/password')
#     return render(request, 'login.html')
		
				