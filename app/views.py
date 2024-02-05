from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
from app.models import *
def equijoins(request): 
    EMPOBJECTS=Employee.objects.select_related('deptno').all()
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(hiredate__year=2024)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno=10)
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__dname='Accounting')
    EMPOBJECTS=Employee.objects.select_related('deptno').filter(deptno__dlocation='Dallas')
    EMPOBJECTS=Employee.objects.select_related('deptno').order_by('sal')
    EMPOBJECTS=Employee.objects.select_related('deptno').order_by('-sal')
    EMPOBJECTS=Employee.objects.select_related('deptno').order_by(Length('ename'))
    EMPOBJECTS=Employee.objects.select_related('deptno').order_by(Length('ename').desc())
    EMPOBJECTS=Employee.objects.select_related('deptno').all()[2:5:]

    
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def selfjoins(request):
    EMPOBJECTS=Employee.objects.select_related('mgr').all()
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(sal__gte=2000)
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(sal__lte=3000)
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(mgr__isnull=True)
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(mgr__isnull=False)
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(comm__isnull=False)
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(comm__isnull=True)
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(deptno=30)
    EMPOBJECTS=Employee.objects.select_related('mgr').filter(deptno__dname='Research')
    EMPOBJECTS=Employee.objects.select_related('mgr').order_by('hiredate')
    EMPOBJECTS=Employee.objects.select_related('mgr').order_by('-hiredate')
    EMPOBJECTS=Employee.objects.select_related('mgr').order_by(Length('ename'))
    EMPOBJECTS=Employee.objects.select_related('mgr').order_by(Length('ename').desc())
    EMPOBJECTS=Employee.objects.select_related('mgr').all()[1:5:]

    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'selfjoins.html',d)    

def emp_mgr_dept(request):
    emd=Employee.objects.select_related('deptno','mgr').all()
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname='Sales')
    emd=Employee.objects.select_related('deptno','mgr').filter(Q(mgr__ename='Blake') | Q(deptno__dname='Accounting'))
    emd=Employee.objects.select_related('deptno','mgr').filter(ename='Scott')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename='King',mgr__ename='Scott')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename='King',deptno__dname='Accounting')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename__startswith='A')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename__endswith='k')
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dlocation='Dallas')
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname__startswith='R')
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname__endswith='s')
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__ename__startswith='S')
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__ename__endswith='h')
    emd=Employee.objects.select_related('deptno','mgr').order_by('ename')
    emd=Employee.objects.select_related('deptno','mgr').order_by('-ename')
    emd=Employee.objects.select_related('deptno','mgr').order_by(Length('ename'))
    emd=Employee.objects.select_related('deptno','mgr').order_by(Length('ename').desc())
    emd=Employee.objects.select_related('deptno','mgr').order_by('mgr__ename')
    emd=Employee.objects.select_related('deptno','mgr').order_by('-mgr__ename')
    emd=Employee.objects.select_related('deptno','mgr').order_by(Length('mgr__ename'))
    emd=Employee.objects.select_related('deptno','mgr').order_by(Length('mgr__ename').desc())
    emd=Employee.objects.select_related('deptno','mgr').order_by('deptno__dname')
    emd=Employee.objects.select_related('deptno','mgr').order_by('-deptno__dname')
    emd=Employee.objects.select_related('deptno','mgr').order_by(Length('deptno__dname'))
    emd=Employee.objects.select_related('deptno','mgr').order_by(Length('deptno__dname').desc())
    emd=Employee.objects.select_related('deptno','mgr').exclude(ename__in=('Smith','King','Allen'))
    emd=Employee.objects.select_related('deptno','mgr').exclude(mgr__ename='Scott')
    emd=Employee.objects.select_related('deptno','mgr').exclude(mgr__ename__in=('Scott','King','Allen'))
    emd=Employee.objects.select_related('deptno','mgr').exclude(deptno__dname='Research')
    emd=Employee.objects.select_related('deptno','mgr').exclude(deptno__dname__in=('Research','Sales','Operations'))
    emd=Employee.objects.select_related('deptno','mgr').filter(ename__contains='Smith')
    emd=Employee.objects.select_related('deptno','mgr').filter(deptno__dname__contains='Accounting')
    emd=Employee.objects.select_related('deptno','mgr').filter(mgr__ename__contains='King')
    emd=Employee.objects.select_related('deptno','mgr').filter(ename__contains='Smith',deptno__dname__contains='Research')
    emd=Employee.objects.select_related('deptno','mgr').filter(Q(mgr__ename__contains='King') | Q(deptno__dname__contains='Sales'))
    


    
    
    
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)

def emp_salgrade(request):
    #EO=Employee.objects.all()
    #SO=SalGrade.objects.all()

    # Retrieving the data of employess who belongs to grade 4
    SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]
    EO=Employee.objects.filter(sal__range=(SO[0].lowsal,SO[0].highsal))
    #Retrieving the data of employess who belongs to grade 3,4
    SO=SalGrade.objects.filter(grade__in=(3,4))

    EO=Employee.objects.none()
    for sgo in SO:
        EO=EO|Employee.objects.filter(sal__range=(sgo.lowsal,sgo.highsal))
        EO=EO|Employee.objects.filter(sal__range=(sgo.lowsal,sgo.highsal),ename='Blake')
    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)