from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Blog, Category, Series
from .forms import BlogForm
# Create your views here.



###################### SERIES RELATED #####################
class SeriesCreate(LoginRequiredMixin, CreateView):
    model       =   Series
    fields      =   ['title']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class SeriesDetail(DetailView):
    model       =   Series


#categoryCount
def get_categoryCount():
    queryset = Blog.objects.values('category__name').annotate(Count('category'))
    return queryset

class BlogList(ListView):
    model       =   Blog
    paginate_by =   4
    ordering    =   '-date_stamp'
    form        =   BlogForm()

    def post(self, request, *args, **kwargs):
        form    =   BlogForm(request.POST)
        form.instance.author    =   request.user
        if form.is_valid():
            form.save()
            messages.success(request, f"Blog Created successfully")
            return redirect('blog_list')
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoryCount'] = get_categoryCount()
        context['form'] = self.form
        return context


class BlogCategory(ListView):
    template_name = "blog/blog_category.html"
    form        =   BlogForm()

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return  Blog.objects.filter(category=self.category)

    def post(self, request, *args, **kwargs):
        form    =   BlogForm(request.POST)
        form.instance.author    =   request.user
        if form.is_valid():
            form.save()
            messages.success(request, f"Blog Created successfully")
            return redirect(object.get_absolute_url())

    def get_context_data(self, **kwargs):
        context = super(BlogCategory, self).get_context_data(**kwargs)
        context['category_list']  = Category.objects.all()
        context['form'] = self.form
        return context



def blogDetail(request, pk):
    object  =   get_object_or_404(Blog, pk=pk)
    #categoryCount
    categoryCount = get_categoryCount()
    #Increament Views
    object.view += 1
    object.save()
    #Comments
    # parent_obj = None
    # initial_data = {
    #         "content_type": object.get_content_type,
    #         "object_id": object.id,
    #     }
    # form    =   CommentForm(request.POST or None, initial = initial_data)
    # if form.is_valid():
    #     c_type = form.cleaned_data.get('content_type')
    #     try:
    #         parent_id = int(request.POST.get("parent_id"))
    #     except:
    #         parent_id = None
    #     if parent_id:
    #         parent_qs = Comment.objects.filter(id=parent_id)
    #         if parent_qs.exists() and parent_qs.count() == 1:
    #             parent_obj = parent_qs.first()

       
    #     new_comment, created = Comment.objects.get_or_create(
    #         user         = request.user,
    #         content_type = ContentType.objects.get(model=c_type),
    #         object_id    = form.cleaned_data.get("object_id"),
    #         content      =  form.cleaned_data.get("content"),
    #         parent       =  parent_obj,
    #     )
    #     if new_comment.is_parent:
    #         return HttpResponseRedirect(new_comment.get_absolute_url())
    #     return redirect(new_comment.parent.get_absolute_url())
        
        

    context = {
        'categoryCount':categoryCount,
        'object':object,
    }
    return render(request, 'blog/blog_detail.html', context)



class BlogUpdate(UpdateView):
    model   =   Blog
    fields  =   ['title','content','category']

    def form_valid(self, form):
        form.instance.edited == True
        form.save()
        return super().form_valid(form)


def blogDelete(request, pk):
    blog    =   get_object_or_404(Blog, pk=pk)
    if blog.author == request.user or request.user.is_superuser:
        blog.delete()
        messages.success(request, f"Post Deleted")
        return redirect('blog_list')
    else:
        messages.warning(request, f"you don't have the permission for the operation!!!")
        return redirect(blog.get_absolute_url())

@login_required
def likeBlog(request, pk):
    obj = get_object_or_404(Blog, pk=pk)
    if obj.like.filter(id=request.user.id).exists():
        obj.like.remove(request.user.id)
        obj.author.points -= 1  # Reduce Authors Points by one if user dislikes the blog
    else:
        obj.like.add(request.user.id)
        obj.author.points += 1  # Increase Authors Points by one if user likes the blog
    return redirect(obj.get_absolute_url())

def disLikeBlog(request, pk):
    obj = get_object_or_404(Blog, pk=pk)
    print(obj.author.points)
    if obj.like.filter(id=request.user.id).exists():
        obj.like.remove(request.user.id)
        obj.dislike.add(request.user.id)
    elif obj.dislike.filter(id=request.user.id).exists():
        obj.dislike.remove(request.user.id)
    else:
        obj.dislike.add(request.user.id)
    return redirect(obj.get_absolute_url())