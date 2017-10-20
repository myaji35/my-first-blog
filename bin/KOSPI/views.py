from django.views.generic.base import TemplateView

#Create your views here.

#--- templateView
class HomeView(TemplateView):
    template_name = 'home.html'
