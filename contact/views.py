from django.views.generic import CreateView, TemplateView
from contact.models import ContactBannerModel, ContactModel

class ContactView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['banners'] = ContactBannerModel.objects.order_by('-pk')[:1]
        data['contacts'] = ContactModel.objects.all()
        return data
