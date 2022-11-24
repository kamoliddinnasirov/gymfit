from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views.generic import CreateView, TemplateView
from contact.models import ContactBannerModel, ContactModel, ContactSendModel
from contact.forms import ContactSendForm

# class ContactView(TemplateView):
#     template_name = "contact.html"
#
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['banners'] = ContactBannerModel.objects.order_by('-pk')[:1]
#         data['contacts'] = ContactModel.objects.all()
#         data['contact_sends'] = ContactSendModel.objects.all()
#         return data




# class ContactView(TemplateView):
#     model = ContactModel
#     template_name = 'contact.html'



class ContactSendView(CreateView):
    template_name = 'contact.html'
    # model = ContactSendModel
    form_class = ContactSendForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.post = get_object_or_404(ContactSendModel, pk=self.kwargs.get('pk'))
        print(form)
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('blog:posts')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['banners'] = ContactBannerModel.objects.order_by('-pk')[:1]
        data['contacts'] = ContactModel.objects.all()
        data['contact_sends'] = ContactSendModel.objects.all()
        return data

