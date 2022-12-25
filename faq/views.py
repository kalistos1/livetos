from django.shortcuts import render,redirect,get_object_or_404
from .forms import FaqForm
from django.contrib import messages
from .models import Faq
from django.contrib.auth.decorators import login_required
# Create your views here.


def all_faq(request):
    template ="pages/all_faq.html"
    
    all_faq = Faq.objects.all()
    context = {
        'faq':all_faq
    }
    return render(request, template ,context)


@login_required
def create_faq (request):
    template ="pages/add_faq.html"
    if request.method =="POST":
        
        form = FaqForm(request.POST)
        if form.is_valid():
            faq_form = form.save(commit=False)
            faq_form.user = request.user
            faq_form.save()
            messages.success(request,'frequently ased questions was saved successfully')
            return redirect('faq:all_faq')
        else:
            messages.error(request,'unable to save frequently asked question')
    else:
        form = FaqForm()
        context ={
            "form":form,
        }
    return render(request,template,context)


@login_required
def update_faq(request,id):

    template ="pages/edit_faq.html"
    post = get_object_or_404(Faq, id=id)
    form =  FaqForm(request.POST, instance=post)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save
            messages.success(request,"faq was saved succesfully")
            return redirect('faq:all_faq')
        else:
            messages.error(request, 'faq was not saved something went wrong')
            form =  FaqForm(instance=post)
            context = {
                'form':form
            }
            return render(request, template, context)

    else:
        form = FaqForm(instance=post)
        context = {
                'form':form
            }
    return render(request, template, context)


@login_required
def delete_faq(request,id):
 faq = get_object_or_404(Faq, id =id).delete()
 messages.success(request, 'faq was deleted successfully')
 return redirect('faq:all_faq')