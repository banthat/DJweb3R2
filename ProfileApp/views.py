from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse("<H1>Hello World, This is my First Web </H1>"
                        "<H2>I Love Girls' Generation, It's My Life</H2>")

def firstPage(request):
    return render(request, 'FirstPage.html')

def secondpage(request):
    return render(request, 'SecondPage.html')

def thirdpage(request):
    return render(request, 'thirdpage.html')

def hnypage(request):
    return render(request, 'hnypage.html')

def home(request):
    return render(request, 'home.html')

def myData(request):
    name = "Mr. Banthat"
    surname = "Upara"
    gender = "Male"
    education = "ปรัญญาตรี ปีที่ 3"
    status = "Student"
    work = "RMUTI"
    return render(request, 'myData.html',
                  {'name': name, 'surname': surname, 'gender': gender,
                   'education': education, 'status': status, 'work': work})

    # context = {'name': name, 'surname': surname, 'gender': gender,
    #            'education': education, 'status': status, 'work': work}
    # return render(request, 'myData.html', context)
