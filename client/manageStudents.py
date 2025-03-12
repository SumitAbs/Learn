from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
# from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Students


def manageStudents(request):
    
    # students = [
    #     {'name': 'John Doe', 'age': 15, 'grade': '10th'},
    #     {'name': 'Jane Smith', 'age': 14, 'grade': '9th'},
    #     {'name': 'Emily Johnson', 'age': 16, 'grade': '11th'}
    # ]
    students = Students.objects.all()
    
    # for student in students:
    #     print(student)
        
        
    return render(request, 'client/ManageStudents/list.html', {'students': students} )  # This is the manage_students path

def addStudent(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        
        if Students.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect('manageStudents')
        
        Student = Students.objects.create(
            name=name, age=age, email=email,
            grade=grade
        )
        if Student:
            messages.success(request, "Student added successfully")
            return redirect('manageStudents')

    return render(request, 'client/ManageStudents/addStudent.html')  # This is the add_student path

def editStudent(request, id):
    fetch_student = Students.objects.get(id=id)
    
    if request.method == 'POST':
        student_id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        grade = request.POST.get('grade')
        
        if email != fetch_student.email and Students.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return redirect('editStudent', id=id)
        
        student = Students.objects.get(id=student_id)
        student.name = name
        student.email = email
        student.age = age
        student.grade = grade
        student.save()
        messages.success(request, "Student updated successfully")
        return redirect('manageStudents')
    
    return render(request, 'client/ManageStudents/editStudent.html', {'student': fetch_student})

def deleteStudent(request, id):
    student = Students.objects.get(id=id)
    student.delete()
    messages.success(request, "Student deleted successfully")
    return redirect('manageStudents')