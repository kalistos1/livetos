from django.shortcuts import render,redirect,get_object_or_404
from .forms import TestimoneyForm
from django.contrib import messages
from .models import Testimoney
from django.contrib.auth.decorators import login_required
# Create your views here.


def all_testimoney(request):
    template ="testimoney/all_testimoney.html"
    
    all_testimoney = Testimoney.objects.all()
    context = {
        'testimonies':all_testimoney
    }
    return render(request, template ,context)


@login_required
def create_testimoney (request):
    template ="testimoney/add_testimoney.html"
    if request.method =="POST":
        
        form = TestimoneyForm(request.POST, request.FILES)
        if form.is_valid():
            testimoney_form = form.save(commit=False)
            testimoney_form.user = request.user
            testimoney_form.save()
            messages.success(request,'Client testimoney was saved successfully')
            return redirect('testimoney:all_testimoney')
        else:
            messages.error(request,'unable to save testimoney')
    else:
        form = TestimoneyForm()
        context ={
            "form":form,
        }
    return render(request,template,context)


@login_required
def update_testimoney(request,id):

    template ="testimoney/edit_testimoney.html"
   
    if request.method == 'POST':
        post = get_object_or_404(Testimoney, id=id)
        form =  TestimoneyForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"testimoney was saved succesfully")
            return redirect('testimoney:update_testimoney',id)
        else:
            messages.error(request, 'testimoney was not saved something went wrong')
            form =  TestimoneyForm(instance=post)
            context = {
                'form':form
            }
            return render(request, template, context)

    else:
        post = get_object_or_404(Testimoney, id=id)
        form = TestimoneyForm(instance=post)
        context = {
                'form':form
            }
        return render(request, template, context)


@login_required
def delete_testimoney(request,id):
 testimoney = get_object_or_404(Testimoney, id =id).delete()
 messages.success(request, 'testimoney was deleted successfully')
 return redirect('testimoney:all_testimoney')