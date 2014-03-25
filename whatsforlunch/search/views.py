from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from whatsforlunch.search.form import SearchSimpleForm


class SearchView(TemplateView):

    template_name = 'search/search-results.html'

    def get(self, request):
        form = SearchSimpleForm(data=request.GET)
        if form.is_valid():
            return self.render_to_response({
                'results': form.search(),
            })
        else:
            return redirect(reverse('search'))
