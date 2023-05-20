from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import CommentsForm
from .models import Comments

class CommentAddView(FormView):
    template_name = 'index.html'
    form_class = CommentsForm
    success_url = reverse_lazy('comment_add')

    def form_valid(self, form):
        comment = Comments()
        comment.name = form.cleaned_data['name']
        comment.email = form.cleaned_data['email']
        comment.text = form.cleaned_data['text']
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.all().order_by('-id')
        return context



def comments_add(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = Comments()
            comment.name = form.cleaned_data['name']
            comment.email = form.cleaned_data['email']
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('comments_add')
    else:
        form = CommentsForm()
    comments = Comments.objects.all().order_by('-id')
    return render(request, 'index.html', {'form': form, 'comments': comments})
