from django.shortcuts import render, redirect, HttpResponse
from management import models
from management.utils.form import SdeptModelForm, CourseModelForm

from management import models


def course_list(request):
    search_data = request.GET.get("q", "")
    data_dict = {}
    if search_data:
        data_dict = {"cno__contains": search_data}

    queryset = models.Course.objects.filter(**data_dict)
    # for i in queryset:
    #     print(i)

    context = {
        "queryset": queryset,
        "search_data": search_data,
        # "page_string": page_object.html()
    }
    return render(request, 'course_list.html', context)


def course_add(request):
    if request.method == "GET":
        form = CourseModelForm()
        context = {"form": form}
        return render(request, 'course_add.html', context)

    form = CourseModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect("/course/list")
    context = {
        "form": form
    }
    print("course add not valid")
    return render(request, 'course_add.html', context)


def course_delete(request, nid):
    models.Course.objects.filter(cno=nid).delete()
    # obj = models.Course.objects.filter(cno=nid).first()
    # obj.delete()
    # print(nid, type(nid))
    # print(obj.cno, type(obj.cno))
    return redirect("/course/list")


def course_edit(request, nid):
    obj = models.Course.objects.filter(cno=nid).first()
    if request.method == "GET":
        form = CourseModelForm(instance=obj)
        context = {"form": form}
        return render(request, 'course_edit.html', context)
    form = CourseModelForm(data=request.POST, instance=obj)
    # form.instance.cpno = models.Course.objects.get(cpno=nid).cpno
    if form.is_valid():
        print("course_edit valid")
        form.save()
        return redirect("/course/list")
    print(form.errors)
    return render(request, 'course_edit.html', {"form": form})
