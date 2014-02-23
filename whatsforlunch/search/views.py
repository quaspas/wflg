from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from whatsforlunch.search.form import SearchForm


class SearchView(TemplateView):

    template_name = 'search/search.html'

    def get(self, request):

        form = SearchForm()

        return self.render_to_response({
            'form': form,
        })

    def post(self, request):
        form = SearchForm(data=request.POST)

        if form.is_valid():
            return HttpResponseRedirect(reverse('home'))
        else:
            return self.render_to_response({
            'form': form,
            })