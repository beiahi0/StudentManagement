from django.shortcuts import render, HttpResponse, redirect
from django import forms
from management import models
from management.utils.bootstrap import BootStrapModelForm


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"}),
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(
            render_value=True,
            attrs={"class": "border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"}
        ),
        required=True
    )

    class Meta:
        model = models.User
        fields = ["username", 'password']


#
#     # code = forms.CharField(
#     #     label="验证码",
#     #     widget=forms.TextInput,
#     #     required=True
#     # )
#     #
#     # def clean_password(self):
#     #     pwd = self.cleaned_data.get("password")
#     #     return md5(pwd)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"}),
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(
            render_value=True,
            attrs={"class": "border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"}
        ),
        required=True
    )
    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(
            render_value=True,
            attrs={"class": "border rounded-lg px-3 py-2 mt-1 mb-5 text-sm w-full"}
        ),
    )

    class Meta:
        model = models.User
        fields = ["username", 'password', 'confirm_password']
        # exclude = ['id']

    def clean_confirm_password(self):
        # 自定义验证规则
        print(self.cleaned_data)
        # confirm = md5(self.cleaned_data.get("confirm_password"))
        confirm = self.cleaned_data.get("confirm_password")
        pwd = self.cleaned_data.get("password")

        if confirm != pwd:
            raise forms.ValidationError("两次密码不一致")
        # 为什么要return
        return confirm


#
#     # code = forms.CharField(
#     #     label="验证码",
#     #     widget=forms.TextInput,
#     #     required=True
#     # )
#     #
#     # def clean_password(self):
#     #     pwd = self.cleaned_data.get("password")
#     #     return md5(pwd)


class SdeptModelForm(BootStrapModelForm):
    class Meta:
        model = models.Sdept
        fields = "__all__"

    # 验证：方式2
    # def clean_mobile(self):
    #
    #     txt_mobile = self.cleaned_data["mobile"]
    #
    #     exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
    #     if exists:
    #         raise ValidationError("手机号已存在")
    #
    #     # 验证通过，用户输入的值返回
    #     return txt_mobile


class CourseModelForm(BootStrapModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"

    def clean_cpno(self):
        print(self.cleaned_data)
        # cno = self.cleaned_data.get("cno")
        cpno = self.cleaned_data.get("cpno")
        return cpno


class StudentModelForm(BootStrapModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"

    # def clean_cpno(self):
    # print(self.cleaned_data)
    # # cno = self.cleaned_data.get("cno")
    # cpno = self.cleaned_data.get("cpno")
    # return cpno


class ScModelForm(BootStrapModelForm):
    class Meta:
        model = models.Sc
        fields = "__all__"
        exclude = ['id']

    # def clean_cpno(self):
    # print(self.cleaned_data)
    # # cno = self.cleaned_data.get("cno")
    # cpno = self.cleaned_data.get("cpno")
    # return cpno
