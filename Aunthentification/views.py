from django.contrib import messages
from django.shortcuts import render

from Aunthentification.models import *
from Aunthentification.tempararyRequired import *


# Create your views here.
def index(request):
    return render(request, 'index.html')
def managementLog(request):
    if request.method =="POST":
        email=request.POST['tbEmail']
        password=request.POST['tbPass']
        management_user=management.objects.filter(email=email,password=password)
        if management_user.exists():
            mm=management.objects.get(email=email,password=password)
            mid=mm.id
            facultyAll = faculty.objects.all()
            return render(request, 'managementHome.html', context={'facultyT': facultyAll,'mid':mid})
        else:
            messages.error(request,'Invalid Details Please Enter Details Carefully')
            return render(request,'managementLogin.html')
    return render(request, 'managementLogin.html')
def mupdatePassword(request):
    if request.method=='POST':
        mid=request.POST['mId']
        mid=int(mid)
        mp1=request.POST['tbPass1']
        mp2 = request.POST['tbPass2']
        if mp1==mp2:
            mup=management.objects.get(id=mid)
            mup.password=mp1
            mup.save()
            facultyAll = faculty.objects.all()
            sus="password Updates Succesfully"
            return render(request, 'managementHome.html', context={'facultyT': facultyAll, 'mid': mid,'sus':sus})

    mid=request.GET['mid']
    mid=int(mid)
    return render(request,'mupdatepassword.html',context={'mid':mid})

def forgotPassword(request):
    if request.method=="POST":
        email=request.POST['tbEmail']
        pass1=request.POST['tbPass1']
        pass2=request.POST['tbPass2']
        if pass1==pass2:
            mfp = management.objects.filter(email=email)
            ffp=faculty.objects.filter(email=email)
            spf7=class7.objects.filter(email=email)
            spf8=class8.objects.filter(email=email)
            spf9=class9.objects.filter(email=email)
            spf10=class10.objects.filter(email=email)
            if mfp.exists():
                mfp=management.objects.get(email=email)
                mfp.password=pass1
                mfp.save()
                sus='Password Reset Succesfully Done'
                return render(request,'managementLogin.html',context={'sus':sus})
            elif ffp.exists():
                ffp=faculty.objects.get(email=email)
                ffp.password=pass1
                ffp.save()
                sus='Password Reset Succesfully Done'
                return render(request,'facultyLogin.html',context={'sus':sus})
            elif spf7.exists():
                spf7=class7.objects.get(email=email)
                spf7.password=pass1
                spf7.save()
                sus='Password Reset Succesfully Done'
                return render(request,'studentLogin.html',context={'sus':sus})
            elif spf8.exists():
                spf8 = class8.objects.get(email=email)
                spf8.password = pass1
                spf8.save()
                sus = 'Password Reset Succesfully Done'
                return render(request, 'studentLogin.html', context={'sus': sus})
            elif spf9.exists():
                spf9 = class9.objects.get(email=email)
                spf9.password = pass1
                spf9.save()
                sus = 'Password Reset Succesfully Done'
                return render(request, 'studentLogin.html', context={'sus': sus})
            elif spf10.exists():
                spf10 = class10.objects.get(email=email)
                spf10.password = pass1
                spf10.save()
                sus = 'Password Reset Succesfully Done'
                return render(request, 'studentLogin.html', context={'sus': sus})

    return render(request,'forgotpassword.html')
def addFaculty(request):
    if request.method=="POST":
        name=request.POST['tbName']
        email=request.POST['tbEmail']
        mobile=request.POST['tbTel']
        password=request.POST['tbPass']

        facultyReg =faculty(name=name,email=email,mobile=mobile,password=password)
        facultyReg.save()
        facultyAll=faculty.objects.all()
        return render(request,'managementHome.html',context={'facultyT':facultyAll})

    return render(request,'facultyRegistration.html')

def editFaculty(request):
    if request.method=="POST":
        id=request.POST['tbId']
        name=request.POST['tbName']
        email=request.POST['tbEmail']
        mobile=request.POST['tbTel']

        oneFacultyDetails=getOneFacultyDetails(id)
        oneFacultyDetails.name=name
        oneFacultyDetails.email=email
        oneFacultyDetails.mobile=mobile
        oneFacultyDetails.save()

        facultyAll = faculty.objects.all()
        return render(request, 'managementHome.html', context={'facultyT': facultyAll})

    id=request.GET['id']
    oneFaculty=getOneFacultyDetails(id)
    return render(request,'facultyRegistration.html',context={'fuser':oneFaculty})
def getOneFacultyDetails(id):
    return faculty.objects.get(id=id)

def deleteFaculty(request):
    id=request.GET['id']
    deleteFac=getOneFacultyDetails(id)
    deleteFac.delete()
    facultyAll = faculty.objects.all()
    return render(request, 'managementHome.html', context={'facultyT': facultyAll})


def facultyLog(request):
    if request.method=="POST":
        email=request.POST['tbEmail']
        password=request.POST['tbPass']

        isfaculty=faculty.objects.filter(email=email,password=password)
        if isfaculty.exists():
            instance = faculty.objects.get(email=email)
            fid=instance.id
            classD,nameofclass,subject=classDetails(fid)
            studentAll=studentDetails(fid)
            return render(request, 'facultyHome.html', context={'studentT': studentAll,'fid':fid,'studentAl1':classD,'nOfClass':nameofclass,'subject':subject})
        else:
            messages.error(request,'invalid details Pleas enter details carrefully')
            return render(request, 'facultyLogin.html')

    return render(request, 'facultyLogin.html')
def fupdatePassword(request):
    if request.method=="POST":
        fid=request.POST['fId']
        pass1=request.POST['tbPass1']
        pass2=request.POST['tbPass2']
        fid=int(fid)
        if pass1==pass2:
            up=faculty.objects.get(id=fid)
            up.password=pass1
            up.save()
        classD, nameofclass, subject = classDetails(fid)
        studentAll = studentDetails(fid)
        sus='Password Updated Successfully'
        return render(request, 'facultyHome.html',
                      context={'studentT': studentAll, 'fid': fid, 'studentAl1': classD, 'nOfClass': nameofclass,
                               'subject': subject,'sus':sus})

    fid =request.GET['fid']
    fid=int(fid)
    fuser=faculty.objects.get(id=fid)
    return render(request,'fupdatepassword.html',context={'fid':fid})

def addStudent(request):
    if request.method=='POST':
        fid=request.POST['fId']
        fid=int(fid)
        name=request.POST['tbName']
        email=request.POST['tbEmail']
        mobile=request.POST['tbTel']
        password=request.POST['tbPass']
        classD,nameofclass,subject = classDetails(fid)
        studentAll = addStudentDetails(fid, name, email, mobile, password)
        return render(request, 'facultyHome.html', context={'studentT': studentAll, 'fid': fid, 'studentAl1': classD,'nOfClass':nameofclass,'subject':subject})


    faid = request.GET['faId']
    return render(request,'studentRegistration.html',context={'fid':faid})

def editStudent(request):
    if request.method=="POST":
        fid1=request.POST['fId']
        fid=int(fid1)
        id=request.POST['tbId']
        name=request.POST['tbName']
        email=request.POST['tbEmail']
        mobile=request.POST['tbTel']
        classD,nameofclass,subject = classDetails(fid)
        subjectsEditingDetails(fid,id,name,email)
        studentAll=studentEditindDetails(fid,id,name,email,mobile)
        return render(request, 'facultyHome.html', context={'studentT':studentAll,'fid':fid,'studentAl1':classD,'nOfClass':nameofclass,'subject':subject})


    id=request.GET['id']
    fid = request.GET['fid']
    oneStudentDetails=getOneStudentDetails(fid,id)
    return render(request,'studentRegistration.html',context={'suser':oneStudentDetails,'fid':fid})
def deleteStudent(request):
    id=request.GET['id']
    fid1 = request.GET['fid']
    fid=int(fid1)
    studentAll = deleteStudentDetails(fid,id)
    classD,nameofclass,subject = classDetails(fid)
    return render(request, 'facultyHome.html', context={'studentT': studentAll, 'fid': id, 'studentAl1': classD,'nOfClass':nameofclass,'subject':subject})

def showResult(request):
    id = request.GET['id']
    fid1 = request.GET['fid']
    fid = int(fid1)
    cName=request.GET['cName']
    studentAll,subject=getStudentResults(fid,cName,id)

    return render(request,'facultyShowResult.html',context={'item':studentAll,'subject':subject,'nameOfClass':cName,'fid':fid})

def updateQuestion(request):
    if request.method=='POST':
        fid=request.POST['faId']
        fid=int(fid)
        sid=request.POST['sId']
        cName=request.POST['sClass']
        remarks=request.POST['tbRadio']
        newQst=request.POST['tbNq']
        uQ=updateQuestions(fid,sid,cName,remarks,newQst)

        classD, nameofclass, subject = classDetails(fid)
        studentAll = studentDetails(fid)
        return render(request, 'facultyHome.html',
                      context={'studentT': studentAll, 'fid': fid, 'studentAl1': classD, 'nOfClass': nameofclass,
                               'subject': subject,'uq':uQ})

def studentLogin(request):
    if request.method=='POST':
        email=request.POST['tbEmail']
        password=request.POST['tbPass']
        sid,studentClassName=studentLogins(email,password)
        if sid!=None:
            subjectDetails = studentHomeDetails(studentClassName,sid)
            return render(request, 'studentHome.html',
                      context={'item': subjectDetails, 'nameOfClass': studentClassName, 'sid':sid})
        else:
            messages.error(request,'invalid details')
            return render(request,'studentLogin.html')
    return render(request, 'studentLogin.html')

def supdatePassword(request):
    if request.method=="POST":
        sid=request.POST['sId']
        cName=request.POST['cName']
        pass1=request.POST['tbPass1']
        pass2=request.POST['tbPass2']
        sid=int(sid)
        if pass1==pass2:
            if cName=='c7':
                up=class7.objects.get(id=sid)
                up.password=pass1
                up.save()
            elif cName=='c8':
                up=class8.objects.get(id=sid)
                up.password=pass1
                up.save()
            elif cName=='c9':
                up=class9.objects.get(id=sid)
                up.password=pass1
                up.save()
            elif cName=='c10':
                up=class10.objects.get(id=sid)
                up.password=pass1
                up.save
        subjectDetails = studentHomeDetails(cName, sid)
        sus='Password Updated Successfully'
        return render(request, 'studentHome.html',
                      context={'item': subjectDetails, 'nameOfClass': cName, 'sid': sid,'sus':sus})


    sid =request.GET['sid']
    sid=int(sid)
    cname=request.GET['cName']
    return render(request,'supdatepassword.html',context={'sid':sid,'cName':cname})


def studentEachSubejctDetails(request):
    id = request.GET['id']
    fid1 = request.GET['fid']
    fid = int(fid1)
    cName=request.GET['cName']
    studentAll=studentEachSubject(fid,cName,id)
    return render(request,'studentSubjectHome.html',context={'item':studentAll,'nameOfClass':cName,'fid':fid})

def updateAnswer(request):

    if request.method=="POST":
        sid = request.POST['sId']
        Cname=request.POST['sClass']
        subId = request.POST['subId']
        subId=int(subId)
        nq=request.POST['nqId']
        answer=request.POST['tbA']
        cname,sid=updateAnswers(Cname,sid,answer,subId,nq)
        uq="succesfully submited answer\n please go for next subjects"
        if cname !=None:
            subjectDetails = studentHomeDetails(cname, sid)
            return render(request, 'studentHome.html',
                          context={'item': subjectDetails, 'nameOfClass': cname, 'sid': sid,'uq':uq})




