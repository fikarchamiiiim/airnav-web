from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexMap(TemplateView):
    template_name = "map_index.html"

    def get(self, request, *args, **kwargs):
        context = {
            
        }
        return render(request, self.template_name, context)