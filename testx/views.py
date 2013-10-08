from django.views.generic import FormView

from .forms import MyForm


class MyFormView(FormView):
    form_class = MyForm
    template_name = 'my_form_app/index.html'
    success_url = './'   # :-(

    def dispatch(self, request, *args, **kwargs):
        return super(MyFormView, self).dispatch(request, *args, **kwargs)