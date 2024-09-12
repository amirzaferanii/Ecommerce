from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView
from .forms import ContactForm
from .models import Address
from django.urls import reverse_lazy


# class ContactView(CreateView):
#     model = Contact
#     form_class = ContactForm
#     template_name = 'contactus/contactus.html'
#     success_url = reverse_lazy('contactus:contactus')




class ContactView(View):
    def get(self, request):
        form = ContactForm()
        address = Address.objects.all().last()
        return render(request, 'contactus/contactus.html', {'form': form, 'address': address})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus:contactus')
        return render(request, 'contactus/contactus.html', {'form': form})








