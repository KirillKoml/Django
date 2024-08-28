from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blogs

class BlogsListView(ListView):
    model = Blogs

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogsDetailView(DetailView):
    model = Blogs


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save(update_fields=['number_of_views'])

        if self.object.number_of_views >= 100:
            self.send_mail()
        return self.object

class BlogsCreateView(CreateView):
    model = Blogs
    fields = ('heading', 'content', 'preview')
    success_url = reverse_lazy('blog:blog_list')

class BlogsUpdateView(UpdateView):
    model = Blogs
    fields = ('heading', 'content', 'preview')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])




# Класс-контроллер для удаления записи
class BlogsDeleteView(DeleteView):
    model = Blogs
    success_url = reverse_lazy('blog:blog_list')