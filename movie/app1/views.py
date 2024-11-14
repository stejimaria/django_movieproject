from django.shortcuts import render,redirect
from app1.models import Movie
from app1.forms import MovieForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


# def home(request):
#     k=Movie.objects.all()
#     return render(request,'home.html',{'movie':k})

class Home(ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = "movie"

    # get_query_set

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(title__icontains="P")
    #     return queryset
    #
    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(title="ARM")
    #     return queryset

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(title__startswith="P")
    #     return queryset

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     queryset = qs.filter(year__gt=2021)
    #     return queryset

    #get_context_data

    # def get_context_data(self):
    #     context=super().get_context_data()
    #     context['name']="Steji"
    #     context['age']=21
    #     return context

extra_context = {'name':'Steji','age':21}
class Addmovie(CreateView):
    model = Movie
    fields = ['title','description','year','language','image']
    template_name = 'add.html'
    success_url = reverse_lazy('app1:home')




# def addmovies1(request):                           #builtinform
#     if(request.method=="POST"):
#         form=MovieForm(request.POST,request.FILES)              #create a form object using values that are passed that are passed through request.POST
#         if form.is_valid():                         #is_valid() builtin function to check the values of form fields
#             form.save()                           #save the form in db table
#             return redirect('home')               #redirect to home page
#     form=MovieForm()                       #empty form object is created
#     context={'form':form}
#     return render(request,'add1.html',context)


# def addmovie(request):
#     if(request.method=="POST"):
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         l=request.POST['l']
#         i=request.FILES['i']
#
#         m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
#         m.save()
#         return home(request)
#     return render(request,'add.html')

# def viewdetail(request,i):
#     k=Movie.objects.get(id=i)
#     return render(request, 'detail.html', {'movie': k})


class Detail(DetailView):
    model = Movie
    template_name = "detail.html"
    context_object_name = "movie"

# def edit(request,i):
#     k=Movie.objects.get(id=i)
#     if (request.method == "POST"):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         if request.FILES.get('i')==None:
#             k.save()
#         else:
#             k.image=request.FILES['i']
#         k.save()
#         return redirect('app1:home')

    # return render(request, 'edit.html',{'movie': k})


class Edit(UpdateView):
    model = Movie
    fields = ['title', 'description', 'year', 'language', 'image']
    template_name = 'edit.html'
    success_url = reverse_lazy('app1:home')

# def delete(request,i):
#     k=Movie.objects.get(id=i)
#     k.delete()
#     return redirect('app1:home')


class Delete(DeleteView):
    template_name = "delete.html"
    model = Movie
    success_url = reverse_lazy('app1:home')






