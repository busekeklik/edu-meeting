from datetime import datetime

from django.shortcuts import render, get_object_or_404
from .models import Meetings
from .models import Courses

# Create your views here.
def mainpage(request):
    return render(request,'mainpage/index.html')

def upcoming_meetings(request):
    meetings = Meetings.objects.filter(date__gte=datetime.now()).order_by('date')[:5]  # Yaklaşan 5 toplantıyı al
    return render(request, 'upcoming-meetings.html', {'meetings': meetings})

def course_categories(request):
    categories = Courses.objects.values_list('category', flat=True).distinct()
    return render(request, 'course-categories.html', {'categories': categories})


import logging

# Create a logger instance
logger = logging.getLogger(__name__)

def index(request):
    context = {
        'successful_students': 200,
        'total_teachers': 50,
        'total_students': 800,
        'total_courses': 120,
    }
    print(context)  # This will print the context to the console
    return render(request, 'mainpage/index.html', context)

def meetings(request):
    # This might list all meetings
    all_meetings = Meetings.objects.all()
    return render(request, 'mainpage/meetings.html', {'meetings': all_meetings})

def meeting_details(request, id):
    meeting = get_object_or_404(Meetings, pk=id)
    return render(request, 'mainpage/meeting-details.html', {'meeting': meeting})

def course_list(request):
    # List all courses
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, id):
    # Detailed view for a specific course
    course = get_object_or_404(Courses, id=id)
    return render(request, 'courses/course_detail.html', {'course': course})

def course_categories(request):
    # Fetch distinct course categories
    categories = Courses.objects.values_list('category', flat=True).distinct()
    return render(request, 'course-categories.html', {'categories': categories})