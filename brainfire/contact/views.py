from django.contrib import messages
from django.views import generic
from forms import ContactForm

class ContactView(generic.FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def get_success_url(self):
        # Redirect to previous url
        return self.request.META.get('HTTP_REFERER', None)

    def form_valid(self, form):
        messages.info(
            self.request,
            "Thank you for your message!"
        )
        
        form.send_email()
        
        return super(ContactView, self).form_valid(form)

    def form_invalid(self, form):
        messages.info(
            self.request,
            "Oops, something went wrong."
        )
        
        return super(ContactView, self).form_invalid(form)