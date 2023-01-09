from django.urls import path

from my_portfolio.portfolio.views import index_view, download_resume

urlpatterns = (
    path('', index_view, name='index page'),
    path('download/', download_resume, name='download resume'),
)