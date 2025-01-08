from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'author' : 'Apps', 'age' : 17, 'list' : [1,2,3,4,5], 'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'Taka' : 1000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'Taka' : 2000
        },
        {
            'id' : 3,
            'name' : 'HTML',
            'Taka' : 3000
        },
    ]}
    return render(request,'home.html',context)