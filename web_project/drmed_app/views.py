from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from httpx import options

# Create your views here.

elder_info = {
    "name": '', 
    "surname": '', 
    "birthday": '', 
    "HN": '', 
    "hospital_name": '', 
    "hospital_phone": '', 
    "care_name": '', 
    "care_surname": '', 
    "relation": '', 
    "care_phone": '', 
}
disease_info = {
    "disease_else": '',
    "disease_name": [],
}
physical_info = {
    "physical_name": [],
}
mem = {
    "options" : '',
}

# index test
def home(request):
    #return HttpResponse("<h2>hello world</h2>")
    elder_info["name"] =''
    elder_info["surname"] =''
    elder_info["birthday"] =''
    elder_info["HN"] = ''
    elder_info["hospital_name"] = ''
    elder_info["hospital_phone"] = ''
    elder_info["care_name"] = ''
    elder_info["care_surname"] = ''
    elder_info["relation"] = ''
    elder_info["care_phone"] = ''
    disease_info["disease_else"] = ''
    disease_info["disease_name"] = []
    physical_info["physical_name"] = []
    return render(request, 'layout.html' )

def add_new(request):
    elder_info["name"] =''
    elder_info["surname"] =''
    elder_info["birthday"] =''
    elder_info["HN"] = ''
    elder_info["hospital_name"] = ''
    elder_info["hospital_phone"] = ''
    elder_info["care_name"] = ''
    elder_info["care_surname"] = ''
    elder_info["relation"] = ''
    elder_info["care_phone"] = ''
    disease_info["disease_else"] = ''
    disease_info["disease_name"] = []
    physical_info["physical_name"] = []
    return render(request, 'elder_regis.html', elder_info)

def elder_register(request):
    return render(request, 'elder_regis.html', elder_info)

def elder_register2(request):
    if "next" in request.POST :
        elder_info["name"] = request.POST['elder_name']
        elder_info["surname"] = request.POST['elder_surname']
        elder_info["birthday"] = request.POST['birthday']
        elder_info["HN"] = request.POST['elder_hNumber']
        elder_info["hospital_name"] = request.POST['elder_hName']
        elder_info["hospital_phone"] = request.POST['elder_hPhone']
        elder_info["care_name"] = request.POST['care_name']
        elder_info["care_surname"] = request.POST['care_surname']
        elder_info["relation"] = request.POST['relation']
        elder_info["care_phone"] = request.POST['care_phone']
        return render(request, 'elder_regis2.html',disease_info)
    elif "cancel" in request.POST :
        elder_info["name"] =''
        elder_info["surname"] =''
        elder_info["birthday"] =''
        elder_info["HN"] = ''
        elder_info["hospital_name"] = ''
        elder_info["hospital_phone"] = ''
        elder_info["care_name"] = ''
        elder_info["care_surname"] = ''
        elder_info["relation"] = ''
        elder_info["care_phone"] = ''
        return render(request, 'layout.html')
    else:
        return render(request, 'elder_regis2.html',disease_info)

def elder_register3(request):
    if "back2" in request.POST :
        return render(request, 'elder_regis2.html',disease_info)
    elif "next2" in request.POST :
        disease_info["disease_else"] = request.POST['disease_else']
        disease_info["disease_name"] = []
        list_box = ['disease1','disease2','disease3','disease4','disease5','disease_else']
        for name in list_box :
            di = request.POST.get(name)
            if di :
                disease_info["disease_name"].append(request.POST[name])
        return render(request, 'elder_regis3.html',physical_info)
    elif "cancel2" in request.POST :
        disease_info["disease_else"] = ''
        disease_info["disease_name"] = []
        return render(request, 'layout.html')
    else:
        return render(request, 'elder_regis3.html',physical_info)
    

def elder_register4(request):
    if "back3" in request.POST :
        return render(request, 'elder_regis3.html',physical_info)
    elif "next3" in request.POST :
        physical_info["physical_name"] = []
        list_box1 = ['physical1','physical2','physical3','physical4']
        for phy in list_box1 :
            physic_di = request.POST.get(phy)
            if physic_di :
                physical_info["physical_name"].append(request.POST[phy])
        return render(request, 'elder_regis4.html',mem)
    elif "cancel3" in request.POST :
        physical_info["physical_name"] = []
        return render(request, 'layout.html')
    else:
        return render(request, 'elder_regis4.html',mem)


def elder_register5(request):
    if "back4" in request.POST :
        return render(request, 'elder_regis4.html',mem)
    elif "next4" in request.POST :
        mem['options'] = request.POST['options']
        return render(request, 'elder_regis5.html')
    elif "cancel4" in request.POST :
        mem["options"] = ''
        return render(request, 'layout.html')
    else:
        return render(request, 'elder_regis5.html')

