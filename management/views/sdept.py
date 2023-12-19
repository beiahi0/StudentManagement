from django.shortcuts import render, redirect, HttpResponse
from management import models
from management.utils.form import SdeptModelForm


def sdept_list(request):
    search_data = request.GET.get("q", "")
    data_dict = {}
    if search_data:
        data_dict = {"sdeptId__contains": search_data}

    queryset = models.Sdept.objects.filter(**data_dict)

    # page_object = Pageination(request, queryset)
    context = {
        "queryset": queryset,
        "search_data": search_data,
        # "page_string": page_object.html()
    }
    return render(request, 'sdept_list.html', context)


def sdept_delete(request, nid):
    models.Sdept.objects.filter(sdeptId=nid).delete()
    return redirect('/sdept/list/')


def sdept_edit(request, nid):
    row_object = models.Sdept.objects.filter(sdeptId=nid).first()
    form = SdeptModelForm(instance=row_object)
    if request.method == "GET":
        print("get")
        context = {
            "form": form,
        }
        # print(form.sdeptId, form.sdeptName)
        return render(request, 'sdept_edit.html', {"form": form})

    form = SdeptModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        print("valie")
        form.save()
        return redirect("/sdept/list")
    print("not valid")
    return render(request, 'sdept_edit.html', {"form": form})


def sdept_add(request):
    if request.method == "GET":
        form = SdeptModelForm()
        context = {"form": form}
        return render(request, 'sdept_add.html', context)

    form = SdeptModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/sdept/list")
    context = {
        "form": form
    }
    return render(request, 'sdept_add.html', context)
