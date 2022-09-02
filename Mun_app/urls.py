from django.urls import path
from . import views as Mun_app_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', Mun_app_views.IndexView.as_view(), name='index'),
    #path ('',Mun_app_views.Index, name="index" ),
    path ('about/',Mun_app_views.About, name="about"),
    path ('blog/',Mun_app_views.Blogf, name="blog"),
    path ('single/<int:id>/',Mun_app_views.Single, name="single"), #the order matter single/<int:id>/in the template and here.
    path ('about/previous_experience/',Mun_app_views.Previous_experience, name="previous_experience"),
    path ('highlights/',Mun_app_views.Previous_experience, name="highlight"),
    #path ('about/previous_experience/<int:pk>/',Mun_app_views.DetailView.as_view(), name="previous_experience"),
    path ('about/tv_series/',Mun_app_views.TvSeriesf, name="TvSeriesf"),
    path ('explore/',Mun_app_views.Exploref, name="explore"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




