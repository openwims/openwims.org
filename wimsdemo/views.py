import json
import time

from wimsdemo.forms import WimDemoForm
from wimsdemo.wimss import WIMsService
from django.views.generic import FormView

class DemoView(FormView):

    form_class    = WimDemoForm
    template_name = "wim-demo.html"
    service = WIMsService()

    def form_valid(self, form):
        _t1 = time.time()
        sentence = form.cleaned_data['sentence']
        result = json.dumps(self.service.analyze(sentence), indent=4)
        _t2 = time.time()
        delta = _t2 - _t1
        return self.render_to_response(self.get_context_data(
                    form=form, result=result, analyze_time=delta))

    def get_context_data(self, **kwargs):
        context = super(DemoView, self).get_context_data(**kwargs)
        if hasattr(self, 'result') and hasattr(self, 'analyze_time'):
            context['result'] = self.result
            context['analyze_time'] = self.analyze_time
        return context