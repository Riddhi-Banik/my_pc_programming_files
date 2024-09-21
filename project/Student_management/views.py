from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def Student_form_fill(request):
    recent = False
    msg = {'is_success' : '',
           'dupe' : False,}
    if request.method == "POST":
        form = StudentForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll = form.cleaned_data['roll']
            section = form.cleaned_data['section']
            gpa = form.cleaned_data['gpa']
            photo = form.cleaned_data['photo']
            print(form.cleaned_data)
            _db = Student.objects.all()
            _res = [s for s in _db.values() if s['roll'] == roll and s['name'] == name and s['section'] == section] # manage duplicates
            print(_res, len(_res))
            _data = Student(name = name,
                            roll = roll,
                            section = section,
                            gpa = gpa,
                            photo = photo)
            if len(_res) == 0: # no duplicates
                _data.save()
                recent = form.instance
                print('Success')
                msg['is_success'] = True
            else:
                msg['dupe'] = True
    else:
        msg = {'is_success' : False}
    
    
    form = StudentForm(label_suffix= ':')
    print(msg)
    if recent:
        print(f"Recent : {recent}")
        return render(request, 'Student/FormFill.html', 
        {'form' : form, 'msg' : msg, 'obj' : recent})
    return render(request, 'Student/FormFill.html', 
    {'form' : form, 'msg' : msg,})


def Viewing(request):
    _db = Student.objects.all()
    return render(request, 'Student/Viewing.html', {'db' : _db})