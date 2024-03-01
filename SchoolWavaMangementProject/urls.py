"""
URL configuration for SchoolWavaMangementProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Aunthentification import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),

    path('mup', views.mupdatePassword, name='mupdatePassword'),
    path('fupdatePassword',views.fupdatePassword,name='fupdatePassword'),
    path('supdatePassword', views.supdatePassword, name='supdatePassword'),
    path('forgotPassword',views.forgotPassword,name='forgotPassword'),
    path('managementLog',views.managementLog,name='managementLog'),
    path('addFaculty', views.addFaculty, name='addFaculty'),
    path('editFaculty', views.editFaculty, name='editFaculty'),
    path('deleteFaculty', views.deleteFaculty, name='deleteFaculty'),
    path('facultyLog',views.facultyLog,name='facultyLog'),
    path('addStudent',views.addStudent,name='addStudent'),
    path('editStudent',views.editStudent,name='editStudent'),
    path('deleteStudent',views.deleteStudent,name='deleteStudent'),
    path('showResult',views.showResult,name='showResult'),
    path('updateQuestion',views.updateQuestion,name='updateQuestion'),
    path('studentLogin', views.studentLogin, name='studentLogin'),
    path('updateAnswer',views.updateAnswer,name='updateAnswer'),
    path('studentSub',views.studentEachSubejctDetails,name='studentEachSubejctDetails'),



]
