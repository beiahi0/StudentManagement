from django.shortcuts import render, redirect, HttpResponse
from management import models
from management.utils.form import SdeptModelForm, StudentModelForm


def student_list(request):
    # queryset = models.Student.objects.all()

    search_data = request.GET.get("q", "")
    data_dict = {}
    if search_data:
        data_dict = {"sno__contains": search_data}

    queryset = models.Student.objects.filter(**data_dict)

    # page_object = Pageination(request, queryset)
    context = {
        "queryset": queryset,
        "search_data": search_data,
        # "page_string": page_object.html()
    }
    return render(request, 'student_list.html', context)


def student_add(request):
    if request.method == "GET":
        form = StudentModelForm()
        context = {"form": form}
        return render(request, 'student_add.html', context)

    form = StudentModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect("/student/list")
    context = {
        "form": form
    }
    print("student add not valid")
    return render(request, 'student_add.html', context)


def student_delete(request, nid):
    models.Student.objects.filter(sno=nid).delete()
    return redirect('/student/list')


def student_edit(request, nid):
    print(nid)
    obj = models.Student.objects.filter(sno=nid).first()
    if request.method == "GET":
        form = StudentModelForm(instance=obj)
        context = {"form": form}
        return render(request, 'student_edit.html', context)
    form = StudentModelForm(data=request.POST, instance=obj)
    # form.instance.cpno = models.Course.objects.get(cpno=nid).cpno
    if form.is_valid():
        print("student_edit valid")
        form.save()
        return redirect("/student/list")
    print(form.errors)
    return render(request, 'student_edit.html', {"form": form})
