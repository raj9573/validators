from django.shortcuts import render

# Create your views here.

def register(request):

    if request.method == 'POST':
        # print(type(request.POST))
        # print(request.POST)
        name = request.POST['name']
        age = request.POST['age']

        print(name,age)

    return render(request,'index.html')


from app.forms import userForm

def my_form(request):

    uf = userForm()

    if request.method ==  'POST':

        UFD = userForm(request.POST)

        # print(UFD)

        if UFD.is_valid():
            name = UFD.cleaned_data['name']
            age = UFD.cleaned_data['age']
            print("this is the my_form data ")
            print(name,age)
            print("this is the end of my form data ")
            UFD.save()


    return render(request,'my_form.html',{'uf':uf})

