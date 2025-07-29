from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import AdminLoginForm, StudentForm
from rest_framework.decorators import api_view
from rest_framework.response import Response


def login_view(request):
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'students/login.html', {'form': form})

# Add this logout function
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    students = Student.objects.filter(
        department=request.user.department
    ).order_by('-id')[:5]  # Just get the 5 most recent
    
    return render(request, 'students/dashboard.html', {
        'students': students,
        'department': request.user.get_department_display(),
        'total_count': students.count()  # Simple count without time filtering
    })

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, admin=request.user)
        if form.is_valid():
            student = form.save(commit=False)
            student.department = request.user.department
            student.created_by = request.user
            student.save()
            return redirect('dashboard')
    else:
        form = StudentForm(admin=request.user)
    return render(request, 'students/add_student.html', {'form': form})

@login_required
def search_students(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(department=request.user.department)
    
    if query:
        students = students.filter(name__icontains=query) | students.filter(student_id__icontains=query)
    
    return render(request, 'students/search.html', {
        'students': students,
        'query': query,
        'department': request.user.get_department_display(),
    })

@api_view(['GET'])
def student_api(request):
    students = Student.objects.all()
    data = [{'id': s.id, 'name': s.name} for s in students]  # Example
    return Response(data)