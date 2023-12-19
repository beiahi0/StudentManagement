from django.shortcuts import render, redirect

from management import models
from management.utils.form import ScModelForm


def sc_list(request):
    search_data = request.GET.get("q", "")
    # print(search_data, type(search_data))

    data_dict = {}
    # if search_data:
    #     data_dict = {"sno__contains": search_data}

    queryset = models.Sc.objects.filter(**data_dict)

    # queryset = models.Sc.objects.all()
    for i in queryset:
        print(i)

    context = {
        "queryset": queryset,
        # "search_data": search_data,
    }
    return render(request, 'sc_list.html', context)


def sc_add(request):
    if request.method == "GET":
        form = ScModelForm()
        context = {"form": form}
        return render(request, 'sc_add.html', context)

    form = ScModelForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect("/sc/list")
    context = {
        "form": form
    }
    print("Sc add not valid")
    return render(request, 'sc_add.html', context)


def sc_edit(request, nid):
    obj = models.Sc.objects.filter(id=nid).first()
    if request.method == "GET":
        form = ScModelForm(instance=obj)
        context = {"form": form}
        return render(request, 'course_edit.html', context)

    form = ScModelForm(data=request.POST, instance=obj)
    # form.instance.cpno = models.Course.objects.get(cpno=nid).cpno
    if form.is_valid():
        print("sc_edit valid")
        form.save()
        return redirect("/sc/list")
    print(form.errors)
    return render(request, 'sc_edit.html', {"form": form})


def sc_delete(request, nid):
    models.Sc.objects.filter(id=nid).delete()
    print(nid)
    return redirect('/sc/list')
