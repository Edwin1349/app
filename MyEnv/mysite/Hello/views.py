from django.shortcuts import render
from django.contrib.auth.models import User as U
# Create your views here.
from Hello.forms import RegistrationForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from .models import User
from .models import Family
from .models import Budget
from django.shortcuts import get_list_or_404, get_object_or_404
import json
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
#def index(request):
    #return HttpResponse("Hello World 13")
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])

def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request))
def register(request):
    if request.method == "POST":
        form= RegistrationForm(request.POST)
        if form.is_valid():
            if Family.objects.get(key=request.POST.get("key")):
                form.save()
                form = U.objects.last()
                print(form)
                #family=Family.objects.create(familyName="qqq",key="#12345678")  
                family= Family.objects.get(key=request.POST.get("key"))
                print(family)
                user=User.objects.create(family=family,user=form)
                #Budget.objects.create(stonks=1048,user=user)
                #login(request, user)
                family=request.POST.get("key")
                #return HttpResponseRedirect(reverse('archive', args=(family,)))
                #return HttpResponseRedirect(reverse('indexClient', kwargs={'username':user.name}))
                return HttpResponseRedirect("/accounts/login")
            return HttpResponse("Invalid key")
        return HttpResponse("Invalid")
    else:
        form= RegistrationForm()
        args={"form":form}
        return render(request,"register.html",args)

def make(request,m):
    current_user = request.user
    m=current_user.username
    if request.method == "POST":
        current_id = request.user.id
        current_users=User.objects.get(user_id=current_id)
        Budget.objects.create(stonks=request.POST.get('budget'),user_id=current_users.id)
    return HttpResponseRedirect(reverse('archive', args=(m,)))
def redirect(request,m):
    current_id = request.user.id
    current_users=User.objects.get(user_id=current_id)
    current_family=Family.objects.get(id=current_users.family_id)
    current_users=User.objects.filter(family_id=current_family.id)
    current_authos={}
    for ids in current_users:
        current_authos.update({ids.id:U.objects.get(id=ids.user_id)})
    us_id=list()
    for user in current_users:
        us_id.append(user.id)
    #print(us_id)
    current_budget={}
    for ids in us_id:
        print(ids,"ids")
        current_budget.update({ids:Budget.objects.filter(user_id=ids)})
        print(current_budget)
        #print(current_budget)
    #current_budget=Budget.objects.all()
    print(current_users,current_budget)
    return render(request,"all_questions.html",{"family": current_family,"us_id":us_id,"budget":current_budget,"current_users":current_users,"current_authos":current_authos})
def homepage(request):
    return render (request,'Hello.html')
def index(request):
    people = User.objects.all()
    return render(request, "index.html", {"people": people})
def create(request):
    if request.method == "POST":
        family = Family()
        family.familyName = request.POST.get("family")
        family.key = request.POST.get("key")
        family.save()
        return HttpResponseRedirect("/")
       #else:
           # return HttpResponse("not enough members in family")
#@login_requir
def tryq(request):
    current_user = request.user
    m=current_user.username
    return HttpResponseRedirect(reverse('archive', args=(m,)))
def user_dashboard(request, list_id):
    try:
        user_list = Person.get(pk=list_id)
    except models.List.DoesNotExist:
        raise Http404
    return TemplateResponse(request, 'dashboard/view.html', {'user_list': user_list})
@csrf_exempt 
def swagger(request):
    if request.method == "POST":
        #qfamily = Family()
        json_data=json.loads(request.body.decode("utf-8"))
        #print (json_data)
        fname = json_data['fname']
        password= json_data['password']
        count= json_data['count']
        budget=json_data['budget']
        Family.objects.create(fname = fname,password = password, count = count,budget = budget)
        #print(count)
        for i in range (int(count)+1):
            person=json_data['Users'][i]
           # print(person)
            name=person['name']
            spending=person['spending']
            age=person['birth data']
            #family_id=json_data['id']
            family_id= Family.objects.get(fname=fname)
            Person.objects.create(name = name, spending = spending, age = age, family_id = family_id.id)
        #qfamily = Family()
        #qfamily.fname = request.POST.get("name")
        #qfamily.count = request.POST.get("spending")
        #qfamily.save()
       
    return HttpResponseRedirect("/")



def PersonView(request,id=1):
     family = Family.objects.get(id=1)
     people = family.people.all()
     return render(request,'all_questions.html' )
def all_questions(request,q):
    family = get_object_or_404(Family,id=q)
    people = Person.objects.filter(family_id__in=q)
    print(q)
    return render(request,'all_questions.html', {'family': family,'people':people})
    #questions = Family.objects.annotate(number_of_answers=Count('people'))
    #return render(request, 'all_questions.html', {
            #'questions':questions})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        form=AuthenticationForm()
        return render(request, 'dappx/login.html', {})
        