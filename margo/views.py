from django.shortcuts import render, redirect
from .models import Articles, Answer
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def margo_home(request):
    margo = Articles.objects.all()
    return render(request, 'margo/margo_home.html', {'margo': margo})


class MargoDetailView(DetailView):
    model = Articles
    template_name = 'margo/details_view.html'
    context_object_name = 'article'

class MargoUpdateView(UpdateView):
    model = Articles
    template_name = 'margo/margo-update.html'
    success_url = '/margo'
    form_class = ArticlesForm

class MargoDeleteView(DeleteView):
    model = Articles
    success_url = '/margo'
    template_name = 'margo/margo-delete.html'

    form_class = ArticlesForm



def MargoReviewView(request, pk):
    film = Articles.objects.get(pk=pk)
    answers = Answer.objects.filter(article=film)
    context = {'answers': answers}

    return render(request, 'margo/review.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('margo_home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'margo/create.html', data)