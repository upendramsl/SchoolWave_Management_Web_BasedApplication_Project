from Aunthentification.models import *


def C77():

    dict={
        'c8':class8.objects.all(),
        'c9':class9.objects.all(),
        'c10':class10.objects.all()
    }
    return dict
def C8():

    dict={
        "c77":class7.objects.all(),
        'c9':class9.objects.all(),
        'c10':class10.objects.all()
    }
    return dict
def C9():

    dict={
        "c7":class7.objects.all(),
        'c8':class8.objects.all(),
        'c10':class10.objects.all()
    }
    return dict
def C10():

    dict={
        "c7": class7.objects.all(),
        'c8': class8.objects.all(),
        'c9': class9.objects.all(),
    }
    return dict


def classDetails(id):
    if id==1:
        c7=class7.objects.all()
        return c7,'c7',"Mathe Matics"
    elif id==11:
        c8=class8.objects.all()
        return c8,'c8','Telugu'
    elif id==13:
        c9=class9.objects.all()
        return c9,'c9','science'
    elif id==14:
        c10=class10.objects.all()
        return c10,'c10','social'
def studentDetails(id):
    if id == 1:
        studentAll = C77()
    elif id == 11:
        studentAll = C8()
    elif id == 13:
        studentAll = C9()
    elif id == 14:
        studentAll = C10()
    return studentAll

def addStudentDetails(fid, name, email, mobile, password):
    if fid == 1:
        StudentReg = class7(name=name, email=email, mobile=mobile, password=password)
        class7Maths(name=name,email=email).save()
        class7Telugu(name=name,email=email).save()
        class7science(name=name,email=email).save()
        class7Social(name=name,email=email).save()
        StudentReg.save()
        studentAll = studentDetails(fid)
        return studentAll
    elif fid == 11:
        StudentReg = class8(name=name, email=email, mobile=mobile, password=password)
        StudentReg.save()
        class8Maths(name=name, email=email).save()
        class8Telugu(name=name, email=email).save()
        class8science(name=name, email=email).save()
        class8Social(name=name, email=email).save()
        studentAll = studentDetails(fid)
        return studentAll

    elif fid == 13:
        StudentReg = class9(name=name, email=email, mobile=mobile, password=password)
        StudentReg.save()
        class9Maths(name=name,email=email).save()
        class9Telugu(name=name,email=email).save()
        class9science(name=name,email=email).save()
        class9Social(name=name,email=email).save()
        studentAll = studentDetails(fid)
        return studentAll

    elif fid == 14:
        StudentReg = class10(name=name, email=email, mobile=mobile, password=password)
        StudentReg.save()
        class10Maths(name=name, email=email).save()
        class10Telugu(name=name, email=email).save()
        class10science(name=name, email=email).save()
        class10Social(name=name, email=email).save()
        studentAll = studentDetails(fid)
        return studentAll


def studentEditindDetails(fid,id ,name,email,mobile):

    if fid == 1:
        oneStudentDetails = class7.objects.get(id=id)
        oneStudentDetails.name = name
        oneStudentDetails.email = email
        oneStudentDetails.mobile = mobile
        oneStudentDetails.save()
        studentAll = studentDetails(fid)
        return studentAll
    elif fid == 11:
        oneStudentDetails = class8.objects.get(id=id)
        oneStudentDetails.name = name
        oneStudentDetails.email = email
        oneStudentDetails.mobile = mobile
        oneStudentDetails.save()
        studentAll = studentDetails(fid)
        return studentAll
    elif fid == 13:
        oneStudentDetails = class9.objects.get(id=id)
        oneStudentDetails.name = name
        oneStudentDetails.email = email
        oneStudentDetails.mobile = mobile
        oneStudentDetails.save()
        studentAll = studentDetails(fid)
        return studentAll
    elif fid == 14:
        oneStudentDetails = class10.objects.get(id=id)
        oneStudentDetails.name = name
        oneStudentDetails.email = email
        oneStudentDetails.mobile = mobile
        oneStudentDetails.save()
        studentAll = studentDetails(fid)
        return studentAll

def subjectsEditingDetails(fid,id,name,email):
    if fid==1:
        c7maths = class7Maths.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class7Telugu.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class7science.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class7Social.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
    elif fid==11:
        c8maths = class8Maths.objects.get(id=id)
        c8maths.name = name
        c8maths.email = email
        c8maths.save()
        c8maths = class8Telugu.objects.get(id=id)
        c8maths.name = name
        c8maths.email = email
        c8maths.save()
        c7maths = class8science.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class8Social.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
    elif fid==13:
        c7maths = class9Maths.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class9Telugu.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class9science.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class9Social.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
    elif fid==14:
        c7maths = class10Maths.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class10Telugu.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class10science.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()
        c7maths = class10Social.objects.get(id=id)
        c7maths.name = name
        c7maths.email = email
        c7maths.save()

def updateQuestions(fid,id,cName,remarks,nq):
    if fid==1:
        if cName=='c7':
            uQ=class7Maths.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c8':
            uQ=class8Maths.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c9':
            uQ=class9Maths.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c10':
            uQ=class10Maths.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
    elif fid==11:
        if cName=='c7':
            uQ=class7Telugu.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c8':
            uQ=class8Telugu.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c9':
            uQ=class9Telugu.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c10':
            uQ=class10Telugu.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
    elif fid==13:
        if cName=='c7':
            uQ=class7science.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c8':
            uQ=class8science.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c9':
            uQ=class9science.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c10':
            uQ=class10science.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
    elif fid==14:
        if cName=='c7':
            uQ=class7Social.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c8':
            uQ=class8Social.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c9':
            uQ=class9Social.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
        elif cName=='c10':
            uQ=class10Social.objects.get(id=id)
            uQ.remarks=remarks
            uQ.nq=nq
            uQ.save()
    return "SuccessFully Updated question"
def getOneStudentDetails(fid,id):
    fid=int(fid)
    if fid==1:
        c7=class7.objects.get(id=id)
        return c7
    elif fid==11:
        c8=class8.objects.get(id=id)
        return c8
    elif fid==13:
        c9=class9.objects.get(id=id)
        return c9
    elif fid==14:
        c10=class10.objects.get(id=id)
        return c10

def deleteStudentDetails(fid,id):
    if fid==1:
        class7.objects.get(id=id).delete()
        studentAll = studentDetails(fid)
        return studentAll
    elif fid==11:
        class8.objects.get(id=id).delete()
        studentAll = studentDetails(fid)
        return studentAll
    elif fid==13:
        class9.objects.get(id=id).delete()
        studentAll = studentDetails(fid)
        return studentAll
    elif fid==14:
        class10.objects.get(id=id).delete()
        studentAll = studentDetails(fid)
        return studentAll

def getStudentResults(fid,cName,id):
    if fid==1:
        if cName=='c7':
            student_result=class7Maths.objects.get(id=id)
            return student_result,'Mathematics'
        elif cName=='c8':
            student_result=class8Maths.objects.get(id=id)
            return student_result,'Mathematics'
        elif cName=='c9':
            student_result=class9Maths.objects.get(id=id)
            return student_result,'Mathematics'
        elif cName=='c10':
            student_result=class10Maths.objects.get(id=id)
            return student_result,'Mathematics'

    elif fid == 11:
        if cName == 'c7':
            student_result = class7Telugu.objects.get(id=id)
            return student_result,'Telugu'
        elif cName == 'c8':
            student_result = class8Telugu.objects.get(id=id)
            return student_result,'Telugu'
        elif cName == 'c9':
            student_result = class9Telugu.objects.get(id=id)
            return student_result,'Telugu'
        elif cName == 'c10':
            student_result = class10Telugu.objects.get(id=id)
            return student_result,'Telugu'

    elif fid == 13:
        if cName == 'c7':
            student_result = class7science.objects.get(id=id)
            return student_result,'Science'
        elif cName == 'c8':
            student_result = class8science.objects.get(id=id)
            return student_result,"Science"
        elif cName == 'c9':
            student_result = class9science.objects.get(id=id)
            return student_result,"Science"
        elif cName == 'c7':
            student_result = class10science.objects.get(id=id)
            return student_result,"Science"
    elif fid == 14:
        if cName == 'c7':
            student_result = class7Social.objects.get(id=id)
            return student_result,'Social'
        elif cName == 'c8':
            student_result = class8Social.objects.get(id=id)
            return student_result,'Social'
        elif cName == 'c9':
            student_result = class9Social.objects.get(id=id)
            return student_result,'Social'
        elif cName == 'c7':
            student_result = class10Social.objects.get(id=id)
            return student_result,'Social'

def studentLogins(email,password):
    c7=class7.objects.filter(email=email, password=password)
    c8=class8.objects.filter(email=email, password=password)
    c9 = class9.objects.filter(email=email, password=password)
    c10 = class10.objects.filter(email=email, password=password)
    if c7.exists():
        c7 = class7.objects.get(email=email)
        sid=c7.id
        return sid,'c7'
    elif c8.exists():
        c8 = class8.objects.get(email=email)
        sid = c8.id
        return sid,'c8'
    elif c9.exists():
        studentId = class9.objects.get(email=email)
        sid = studentId.id
        return sid, 'c9'

    elif c10.exists():
        studentId = class10.objects.get(email=email)
        sid = studentId.id
        return sid, 'c10'
    else:
        return None,None
def updateAnswers(cname,sid,answer,subId,nq):
    if cname=='c7':
        if subId==1:
            updateMath=class7Maths.objects.get(id=sid)
            updateMath.answer=answer
            updateMath.pq=nq
            updateMath.save()
        elif subId==11:
            updateTelugu=class7Telugu.objects.get(id=sid)
            updateTelugu.answer=answer
            updateTelugu.pq=nq
            updateTelugu.save()
        elif subId==13:
            updateScience=class7science.objects.get(id=sid)
            updateScience.answer=answer
            updateScience.pq=nq
            updateScience.save()
        elif subId==14:
            updateSocial=class7Social.objects.get(id=sid)
            updateSocial.answer=answer
            updateSocial.pq=nq
            updateSocial.save()
        return cname,sid
    elif cname=='c8':
        if subId == 1:
            updateMath = class8Maths.objects.get(id=sid)
            updateMath.answer = answer
            updateMath.pq=nq
            updateMath.save()
        elif subId == 11:
            updateTelugu = class8Telugu.objects.get(id=sid)
            updateTelugu.answer = answer
            updateTelugu.pq=nq
            updateTelugu.save()
        elif subId ==13:
            updateScience = class8science.objects.get(id=sid)
            updateScience.answer = answer
            updateScience.pq=nq
            updateScience.save()
        elif subId ==14:
            updateSocial = class8Social.objects.get(id=sid)
            updateSocial.answer = answer
            updateSocial.pq=nq
            updateSocial.save()
        return cname, sid

    elif cname=='c9':
        if subId == 1:
            updateMath = class9Maths.objects.get(id=sid)
            updateMath.answer = answer
            updateMath.pq=nq
            updateMath.save()
        elif subId ==11:
            updateTelugu = class9Telugu.objects.get(id=sid)
            updateTelugu.answer = answer
            updateTelugu.pq=nq
            updateTelugu.save()
        elif subId ==13:
            updateScience = class9science.objects.get(id=sid)
            updateScience.answer = answer
            updateScience.pq=nq
            updateScience.save()
        elif subId ==14:
            updateSocial = class9Social.objects.get(id=sid)
            updateSocial.answer = answer
            updateSocial.pq=nq
            updateSocial.save()
        return cname, sid
    elif cname=='c10':
        if subId == 1:
            updateMath = class10Maths.objects.get(id=sid)
            updateMath.answer = answer
            updateMath.pq=nq
            updateMath.save()
        elif subId ==11:
            updateTelugu = class10Telugu.objects.get(id=sid)
            updateTelugu.answer = answer
            updateTelugu.pq=nq
            updateTelugu.save()
        elif subId ==13:
            updateScience = class10science.objects.get(id=sid)
            updateScience.answer = answer
            updateScience.pq=nq
            updateScience.save()
        elif subId == 14:
            updateSocial = class10Social.objects.get(id=sid)
            updateSocial.answer = answer
            updateSocial.pq=nq
            updateSocial.save()
        return cname, sid

def studentHomeDetails(cname,sid):
    if cname=='c7':
        return class7.objects.get(id=sid)
    elif cname=='c8':
        return class8.objects.get(id=sid)
    elif cname=='c9':
        return class9.objects.get(id=sid)
    elif cname=='c10':
        return class10.objects.get(id=sid)

def studentEachSubject(fid,cname,sid):
    if cname == 'c7':
        if fid==1:
            return class7Maths.objects.get(id=sid)
        elif fid==11:
            return class7Telugu.objects.get(id=sid)
        elif fid==13:
            return class7science.objects.get(id=sid)
        elif fid==14:
            return class7Social.objects.get(id=sid)
    elif cname == 'c8':
        if fid == 1:
            return class8Maths.objects.get(id=sid)
        elif fid == 11:
            return class8Telugu.objects.get(id=sid)
        elif fid == 13:
            return class8science.objects.get(id=sid)
        elif fid == 14:
            return class8Social.objects.get(id=sid)
    elif cname == 'c9':
        if fid == 1:
            return class9Maths.objects.get(id=sid)
        elif fid == 11:
            return class9Telugu.objects.get(id=sid)
        elif fid == 13:
            return class9science.objects.get(id=sid)
        elif fid == 14:
            return class9Social.objects.get(id=sid)
    elif cname == 'c10':
        if fid == 1:
            return class10Maths.objects.get(id=sid)
        elif fid == 11:
            return class10Telugu.objects.get(id=sid)
        elif fid == 13:
            return class10science.objects.get(id=sid)
        elif fid == 14:
            return class10Social.objects.get(id=sid)
