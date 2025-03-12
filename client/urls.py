from django.urls import path
from . import views, manageStudents
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', login_required(views.index), name='index'), # This is the root path
    path('', views.index, name='index'), # This is the root path
    path('about/', views.about, name='about'), # This is the about path
    path('contact/', views.contact, name='contact'), # This is the contact path
    path('login/', views.set_login, name='set_login'), # This is the login path
    path('signup/', views.signup, name='signup'), # This is the signup path
    path('logout/', views.logout, name='logout'), # This is the logout path
    path('profile/', views.profile, name='profile'), # This is the profile path
    path('forgot-password/', views.forgot_password, name='forgot-password'), # This is the forgot_password path
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset-password'), # This is the reset_password path

    path('cdashboard/', login_required(views.cdashboard), name='cdashboard'), # This is the Home path
    
    # Manage Students
    path('manage-students/', login_required(manageStudents.manageStudents), name='manageStudents'), # This is the manage_students path 
    path('add-student/', login_required(manageStudents.addStudent), name='addStudent'), # This is the add_student path
    path('edit-student/<int:id>/', login_required(manageStudents.editStudent), name='editStudent'), # This is the edit_student path
    path('delete-student/<int:id>/', login_required(manageStudents.deleteStudent), name='deleteStudent'), # This is the delete_student path
]
