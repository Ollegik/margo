
from django.urls import path
from . import views

urlpatterns = [
    path('', views.margo_home, name='margo_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.MargoDetailView.as_view(), name='margo-detail'),
    path('<int:pk>/update', views.MargoUpdateView.as_view(), name='margo-update'),
    path('<int:pk>/delete', views.MargoDeleteView.as_view(), name='margo-delete'),
    path('review/<int:pk>', views.MargoReviewView, name='margo-review')
]