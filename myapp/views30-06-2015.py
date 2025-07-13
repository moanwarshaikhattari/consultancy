from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail  # Optional: For sending mail
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    form = ContactForm()
    message = ''
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            number = form.cleaned_data['number']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['message']

            # ✅ Send email to YOU
            send_mail(
                subject=f"New Contact from {name}",
                message=f"Name: {name}\nPhone: {number}\nEmail: {email}\n\nMessage:\n{msg}",
                from_email='neooliveinfotech@gmail.com',
                recipient_list=['neooliveinfotech@gmail.com'],
                fail_silently=False,
            )

            # ✅ Send confirmation email to USER
            send_mail(
                subject="Thank you for contacting us",
                message=f"Hi {name},\n\nThanks for reaching out! We'll get back to you soon.\n\nYour Message:\n{msg}",
                from_email='neooliveinfotech@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            
            message = "Your message has been sent successfully."
            form = ContactForm()
    return render(request, 'contact-us.html', {'form': form, 'message': message,})
    # return render(request, 'contact-us.html')