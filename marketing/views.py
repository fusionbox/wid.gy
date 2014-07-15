from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'marketing_home.html'

    def get_context_data(self, **kwargs):
        kwargs = super(HomeView, self).get_context_data(**kwargs)
        kwargs['demo_url'] = 'http://demo.%s/create-demo-site/' % (self.request.get_host(),)
        return kwargs

home = HomeView.as_view()
