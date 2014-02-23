from django.views.generic.base import TemplateView


class SearchView(TemplateView):

    template_name = 'search/search.html'

    def get(self, request):
        form = 'form to come'
        return self.render_to_response({
            'form': form,
        })