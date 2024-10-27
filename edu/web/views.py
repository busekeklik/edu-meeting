from datetime import datetime

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

def upcoming_meetings(request):
    meetings = Meetings.objects.filter(date__gte=datetime.now()).order_by('date')[:5]  # Yaklaşan 5 toplantıyı al
    return render(request, 'upcoming-meetings.html', {'meetings': meetings})

def course_categories(request):
    categories = Courses.objects.values_list('category', flat=True).distinct()
    return render(request, 'course-categories.html', {'categories': categories})

def index(request):
    upcoming_meetings = Meetings.objects.filter(date__gte=datetime.now()).order_by('date')[:5]
    popular_courses = Courses.objects.all().order_by('-popularity')[:10]
    return render(request, 'mainpage/index.html', {
        'upcoming_meetings': upcoming_meetings,
        'popular_courses': popular_courses
    })

def meetings(request):
    # This might list all meetings
    all_meetings = Meetings.objects.all()
    return render(request, 'mainpage/meetings.html', {'meetings': all_meetings})


def meeting_details(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, 'mainpage/meeting-details.html', {'meeting': meeting})
