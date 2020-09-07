from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import education_model,Experience,TechnicalSkills,interpersonalSkills,Achievements,MyProjects
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request,'core/index.html')

def contact(request):
    contact_form = ContactForm()
    context = {'contact_form':contact_form}
    return render(request, 'core/contact.html',context)

def get_message(request):
    if request.method == 'POST':
        frm = ContactForm(request.POST)
        if frm.is_valid():
            if frm.save(commit=True):
                msg = "Thank You ! for connecting with me. I will contact you soon."
                messages.add_message(request,messages.SUCCESS,msg)

            return HttpResponseRedirect('/contact/')
            
    msg = "Sorry ! Query processing Failed."
    messages.add_message(request,messages.WARNING,msg)
    return render(request,'core/contact.html')

def education(request):
    edu = education_model.objects.all()
    edu = sorted(edu,key= lambda x:x.start_year, reverse=True)
    context={"edu":edu}
    return render(request, 'core/education.html',context)

def experience(request):
    exp = Experience.objects.all()
    exp = sorted(exp,key=lambda x:x.start_date,reverse=True)
    context = {"exp":exp}
    return render(request, 'core/experience.html',context)

def workdone(request):
    prjs = MyProjects.objects.all()
    n=len(prjs)

    if n%3 == 0:
        n = range(1,n,3)
    else:
        n = range(1,n+3, 3)
    context = {
        "prjs" : prjs,
        'n' : n 
    }
    return render(request, 'core/workdone.html',context )

def skills(request):
    tech_skls = TechnicalSkills.objects.all()
    intpers_skls = interpersonalSkills.objects.all()
    achvmts = Achievements.objects.all()

    context = {
        "tech_skls":tech_skls,
        "intpers_skls":intpers_skls,
        "achievements":achvmts
    }
    return render(request, 'core/skills.html',context)

 