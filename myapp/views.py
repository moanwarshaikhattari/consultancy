from django.shortcuts import render
# from .forms import ContactForm
from django.core.mail import send_mail  # Optional: For sending mail
# Create your views here.
def index(request):
    data={
        'title':'Home - NeoOliveInfoTech',
    }
    return render(request, 'index.html',data)

def about(request):
    data={
        'title':'About Us - NeoOliveInfoTech',
    }
    return render(request, 'about-us.html',data)

def services(request):
    data={
        'title':'Services - NeoOliveInfoTech',
    }
    return render(request, 'services.html',data)

def contact(request):
    data={
        'title':'Contact Us - NeoOliveInfoTech',
    }

    message = ''

    if request.method == 'POST':
      
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        msg = request.POST.get('message')
         # Check for empty fields
        if not all([name, number, email]):
            return render(request, 'contact-us.html', {**data, 'error': True})
        # if name and number and email and msg:
            # Send mail to admin
        send_mail(
            subject=f"New Contact from {name}",
            message=f"Name: {name}\nPhone: {number}\nEmail: {email}\n\nMessage:\n{msg}",
            from_email='neooliveinfotech@gmail.com',
            recipient_list=['neooliveinfotech@gmail.com'],
            fail_silently=False,
        )
        # Confirmation mail to user
        send_mail(
            subject="Thanks for contacting us!",
            message=f"Hi {name},\n\nWe received your message:\n\n{msg}\n\nThanks for reaching out! We'll be in touch soon!",
            from_email='neooliveinfotech@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

        message = "Your message has been sent successfully."
      

    # ✅ Always return a response
    return render(request, 'contact-us.html', {**data, 'message': message})
    # return render(request, 'contact-us.html', {'form': form, 'message': message,})
    # return render(request, 'contact-us.html')