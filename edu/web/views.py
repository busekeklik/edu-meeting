from django.shortcuts import render, get_object_or_404
from .models import Meetings
from .models import Teachers
from .models import Students
from .models import Courses

# Create your views here.
def mainpage(request):
    return render(request,'mainpage/index.html')

def meeting_list(request):
    meetings = Meetings.objects.all()
    return render(request, 'meetings/meeting_list.html', {'meetings': meetings})

def meeting_detail(request, id):
    meeting = get_object_or_404(Meetings, id=id)
    return render(request, 'meetings/meeting_detail.html', {'meeting': meeting})

def teacher_list(request):
    teachers = Teachers.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, id):
    teacher = get_object_or_404(Teachers, id=id)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})

def student_list(request):
    students = Students.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, id):
    student = get_object_or_404(Students, id=id)
    return render(request, 'students/student_detail.html', {'student': student})

def course_list(request):
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Courses, id=id)
    return render(request, 'courses/course_detail.html', {'course': course})
