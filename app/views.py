from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.db.models import Q
from app.models import *

def insert_dept(request):
    dt=int(input('Enter dept no : '))
    dn=input('Enter dept name : ')
    dl=input('Enter Location : ')
    DO=Dept.objects.get_or_create(DEPTNO=dt,DNAME=dn,LOC=dl)[0]
    DO.save()

    return HttpResponse('create all the dept information successfully')

def display_dept(request):
    QDLO=Dept.objects.all()
    d={'QDLO':QDLO}
    return render(request,'display_dept.html',d)
        

def insert_emp(request):
    do=int(input('Enter dept : '))
    DO=Dept.objects.filter(DEPTNO=do)

    if DO:
        eno=int(input('Enter emp no : '))
        en=input('Enter emp name : ')
        j=input('Enter emp job : ')

        MTO=input('Enter mgr : ')

        if MTO:
            MEO=Emp.objects.get(Emp_no=int(MTO))
        else:
            MEO=None

        h=input('Enter hiredate : ')
        s=int(input('Enter emp salary : '))
        COMM=input('Enter commition : ')


        if COMM:
            COMM=int(COMM)
        else:
            COMM=None
        
        EO=Emp.objects.get_or_create(Emp_no=eno,ENAME=en,JOB=j,MGR=MEO,HIREDATE=h,SAL=s,COMM=COMM,DEPTNO=DO[0])[0]
        EO.save()
        
        return HttpResponse('Create emp table successfully')

    else:
        return HttpResponse('Given deptno is not there in dept table')
    
    
def innerEquijions(request):
    JDEO=Emp.objects.select_related('DEPTNO').all()
    JDEO=Emp.objects.select_related('DEPTNO').filter(JOB='SALESMAN')
    JDEO=Emp.objects.select_related('DEPTNO').filter(SAL__gt='1000')
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(SAL__gt='1000') & Q(ENAME__startswith='a'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(SAL__lt='1000'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(SAL__range=(1000,5000)) & Q(JOB='SALESMAN'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__contains='o') | Q(HIREDATE__gt='1987-01-01'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') | Q(HIREDATE__gt='1987-01-01'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') & Q(HIREDATE__gt='1987-01-01'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') | Q(HIREDATE__gte='1987-01-01'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') | Q(SAL__range=(1000,400)))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(JOB='salesman') & Q(ENAME__startswith='a') | Q(ENAME__contains='e') | Q(ENAME__startswith='j') & Q(ENAME__contains='e') | Q(HIREDATE__gt='1982-01-01'))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM__gt=0))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM=0))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM__gte=0))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(JOB='CLERK') | Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM__gt=0))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(JOB='MANAGER') | Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM__gt=0))
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(JOB='MANAGER') & Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM__gt=0))
    JDEO=Emp.objects.select_related('DEPTNO').all()
    JDEO=Emp.objects.select_related('DEPTNO').filter(MGR=7839)
    JDEO=Emp.objects.select_related('DEPTNO').filter(Q(MGR=7839) | Q(JOB='MANAGER') & Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM__gt=0))
    JDEO=Emp.objects.select_related('DEPTNO').filter(MGR=7698)





    d={'JDEO':JDEO}
    return render(request,'innerEquijions.html',d)

def insert_sal(request):
    gr=int(input('Enter grade : '))
    lo=int(input('Enter losal : '))
    ho=int(input('Enter hosal : '))

    SO=Salary.objects.get_or_create(GRADE=gr,LOSAL=lo,HISAL=ho)[0]
    SO.save()

    return HttpResponse('create successfully')


def selfjoin(request):
    EMJD=Emp.objects.select_related('MGR').all()

    #emp whose name starts with 'a'
    EMJD=Emp.objects.select_related('MGR').filter(ENAME__startswith='a')

    #emp whose name starts with 'e'
    EMJD=Emp.objects.select_related('MGR').filter(ENAME__contains='e')

    #emp whose comm is null
    EMJD=Emp.objects.select_related('MGR').filter(COMM__isnull=True)

    #emp whose hiredate year is greaterthan 1986
    EMJD=Emp.objects.select_related('MGR').filter(HIREDATE__year=1986)

    #emp whose hiredate year is greater than or equal to 1986
    EMJD=Emp.objects.select_related('MGR').filter(HIREDATE__year__gt=1986)

    #emp whose hiredate year is greater than or equal to 1986 and ename contains 'e'
    EMJD=Emp.objects.select_related('MGR').filter(Q(HIREDATE__year__gte=1986),Q(ENAME__contains='e'))

    #emp whose hiredate year is greater than or equal to 1986 or ename contains 'e'
    EMJD=Emp.objects.select_related('MGR').filter(Q(HIREDATE__year__gte=1986) | Q(ENAME__contains='e'))

    #emp whose manage name ends with 'e'
    EMJD=Emp.objects.select_related('MGR').filter(MGR__ENAME__endswith='e')

    #emp whose salay is greater than 1000 and job is manage
    EMJD=Emp.objects.select_related('MGR').filter(Q(SAL__gt=1000) & Q(JOB='MANAGER'))

    #emp whose salay is greater than or equal to  1000 and job is manage

    EMJD=Emp.objects.select_related('MGR').filter(Q(SAL__gte=1000) & Q(JOB='MANAGER'))

    #emp whose salay is less than 1000 or job is manage

    EMJD=Emp.objects.select_related('MGR').filter(Q(SAL__lt=1000) | Q(JOB='MANAGER'))

    #emp whose salay is less than or equal to 1000 or job is salesman

    EMJD=Emp.objects.select_related('MGR').filter(Q(SAL__lte=1000) | Q(JOB='SALSMAN'))

    #emp whose salay is less than 1000 or job is manage and deptno is 20
    EMJD=Emp.objects.select_related('MGR').filter(Q(SAL__lt=1000) | Q(JOB='MANAGER') &Q(DEPTNO=20))
    
    #emp whose comm is null  or job is manage
    EMJD=Emp.objects.select_related('MGR').filter(Q(COMM__isnull=False) | Q(JOB='MANAGER'))

    #emp whose comm is not null
    EMJD=Emp.objects.select_related('MGR').filter(Q(COMM__isnull=False) )

    #emp whose comm is not null and job is 'salesman'
    EMJD=Emp.objects.select_related('MGR').filter(Q(COMM__isnull=False) & Q(JOB='SALESMAN'))
    #emp whose mgr is '7839' or job is 'manager' and ename endswith 's' and sal is range b/w '1000' to '4000' or comm is greater than '0'
    EMDO=Emp.objects.select_related('MGR').filter(Q(MGR=7839) | Q(JOB='MANAGER') & Q(ENAME__endswith='s') & Q(SAL__range=(1000,400)) | Q(COMM__gt=0))


    d={'EMJD':EMJD}
    return render(request,'selfjoin.html',d)

