from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.translation import gettext as _


class Home(TemplateView):
    template_name = "core/dashboard.html"
    name = _("name")

    def get_context_data(self, **kwargs):
        print("-------------", self.name)
        return super().get_context_data(**kwargs)



def home(request):
    print("---------------", _("hello"))
    return render(request, "core/dashboard.html")

