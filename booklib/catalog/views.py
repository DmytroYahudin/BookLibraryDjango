from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DeleteView
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views import View
from django.db.models import F, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .models import Book, Comments
from .forms import CommentForm, BookForm, AuthorForm


class Index(ListView):
    template_name = "catalog/index.html"
    model = Book
    paginate_by = 6


class SearchBook(LoginRequiredMixin, ListView):
    login_url = '/user/login/'
    template_name = "catalog/search_results.html"
    model = Book
    paginate_by = 6

    def get_queryset(self):
        searched = str(self.request.GET['searched'])
        object_list = Book.objects.filter(Q(title__icontains=searched) |
                                          Q(author__first_name__icontains=searched) |
                                          Q(author__last_name__icontains=searched))
        return object_list


class BookView(LoginRequiredMixin, View):
    login_url = '/user/login/'
    form_class = CommentForm
    template_name = "catalog/book.html"

    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        context = {}
        try:
            comments = Comments.objects.filter(for_book=book_id)
            context['comments'] = comments.order_by('-date_added')
        except Comments.DoesNotExist:
            context['comments'] = None
        book.number_of_views = F('number_of_views') + 1
        book.save()
        context['book'] = book
        context['form'] = self.form_class()
        return render(request, self.template_name, context)

    def post(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        form = self.form_class(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.for_book = book
            comment.created_by = request.user
            comment.save()
            return HttpResponseRedirect(reverse('catalog:book', args=(book_id,)))


class NewBook(LoginRequiredMixin, View):
    login_url = '/user/login/'
    form_class = BookForm
    template_name = "catalog/add_book.html"

    def get(self, request):
        if self.request.user.is_superuser or self.request.user.moderator:
            form = self.form_class()
            context = {'form': form}
            return render(request, self.template_name, context)
        else:
            raise PermissionDenied

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            if any(request.FILES):
                new_book.image = request.FILES['image']
            new_book.save()
            return HttpResponseRedirect(reverse('catalog:index'))


class EditBook(LoginRequiredMixin, View):
    login_url = '/user/login/'
    template_name = 'catalog/edit_book.html'
    form_class = BookForm

    def get(self, request, book_id):
        if self.request.user.is_superuser or self.request.user.moderator:
            book = Book.objects.get(pk=book_id)
            form = self.form_class(instance=book)
            context = {'book': book, 'form': form}
            return render(request, self.template_name, context)
        else:
            raise PermissionDenied

    def post(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        book.date_added = datetime.now()
        form = self.form_class(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('catalog:book', args=(book_id,)))


class NewAuthor(LoginRequiredMixin, View):
    login_url = '/user/login/'
    form_class = AuthorForm
    template_name = "catalog/add_author.html"

    def get(self, request):
        if self.request.user.is_superuser or self.request.user.moderator:
            form = self.form_class()
            context = {'form': form}
            return render(request, self.template_name, context)
        else:
            raise PermissionDenied

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_author = form.save(commit=False)
            new_author.save()
            return HttpResponseRedirect(reverse('catalog:index'))


class DeleteBook(LoginRequiredMixin, DeleteView):
    login_url = '/user/login/'
    template_name = 'catalog/book_delete_confirmation.html'

    def get_object(self, queryset=None):
        if self.request.user.is_superuser or self.request.user.moderator:
            book_id = self.kwargs.get("book_id")
            return get_object_or_404(Book, pk=book_id)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('catalog:index')


class DeleteComment(LoginRequiredMixin, DeleteView):
    login_url = '/user/login/'
    template_name = 'catalog/comment_delete_confirmation.html'

    def get_object(self, queryset=None):
        if self.request.user.is_superuser or self.request.user.moderator:
            comment_id = self.kwargs.get("comment_id")
            return get_object_or_404(Comments, pk=comment_id)
        else:
            raise PermissionDenied

    def get_success_url(self):
        book_id = Comments.objects.get(pk=self.kwargs.get("comment_id")).for_book.pk
        return reverse('catalog:book', args=(book_id,))
