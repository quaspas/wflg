from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from whatsforlunch.account.form import AccountLoginForm


class AccountLoginView(TemplateView):

    template_name = 'account/account-login.html'

    def dispatch(self, request):
        if request.user.is_authenticated():
            return redirect('home')
        return super(AccountLoginView, self).dispatch(request)

    def get(self, request):
        form = AccountLoginForm()
        return self.render_to_response({
            'form': form,
        })
