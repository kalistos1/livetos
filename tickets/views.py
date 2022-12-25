from django.shortcuts import render,redirect, get_object_or_404
from . models import TicketMessage
from django.contrib import messages
from .forms import TicketMessageForm
from django.core.mail import send_mail

# Create your views here.

def all_tickets(request):

    template = "admin/all_tickets.html"
    all_tickets = TicketMessage.objects.all()
    context ={
        'all_tickets':all_tickets
    }
    return render(request, template, context)


def delete_ticket(request, id ):
    ticket = get_object_or_404(TicketMessage,id=id).delete()
    messages.success(request, 'ticket was deleted successfully')
    return redirect('tickets:all_ticket')


def read_ticket(request, id):
    template = "admin/read_ticket.html"
    ticket = get_object_or_404(TicketMessage,id=id)
    context ={
        'ticket':ticket,
    }
    return render(request, template, context)


def create_ticket(request):
    template = "admin/create_ticket.html"
    if request.method == "POST":
        form = TicketMessageForm(request.POST, request.FILES)
        if  form.is_valid():
            cd = form.cleaned_data

            subject = cd['title']
            message =  cd['message'] 

            ticket_data = form.save(commit=False)
            ticket_data.sender = request.user
            ticket_data.save() 
            
           
            get_email = request.user.email
            get_username = request.user.username 

            get_subject = subject
            get_message = f" Ticket from {get_username} and email {get_email} /n {message}"

            send_mail(get_subject, get_message, get_email,['oniccapitals@gmail.com', get_email])
            messages.success(request, 'ticket was sent')
            return redirect('')
        else:
            messages.error(request,'something went wrong , try resending the tickets again')
            return redirect('tickets:create_ticket')
    else:
       form = TicketMessageForm()

       context ={
        'form':form
       }
       return render(request, template,context)