from django.shortcuts import render_to_response
from django.views.generic.base  import TemplateView
from whatsforlunch.search.form import SearchSimpleForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        form = SearchSimpleForm()
        return self.render_to_response({
            'form': form,
        })