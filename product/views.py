from django.shortcuts import render
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from user_account.models import Role
# Create your views here.

@method_decorator(login_required(login_url='account:login'),name="dispatch")
class HomeView(View):
    def get(self,request):
        user_roles = self.request.user.roles.all()
        stu_role = Role.objects.get(id = Role.STUDENT)
        teacher_role = Role.objects.get(id = Role.TEACHER)
        secratary_role = Role.objects.get(id = Role.SECRETARY)
        if stu_role in user_roles:
            return render(request,'product/student.html')
        
        if teacher_role in user_roles:
            return render(request,'product/teacher.html')
        
        if secratary_role in user_roles:
            return render(request,'product/secretary.html')
        return render(request,'product/index.html')

        