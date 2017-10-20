from django.views.generic.base import TemplateView

#Create your views here.

#--- templateView
class HomeView(TemplateView):
    template_name = '../home.html'

#def create(request):
#    return render(request, '/template/home.html', {'form':form})
