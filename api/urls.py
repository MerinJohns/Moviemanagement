from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("actors",views.ActorViewSet,basename="actors")

router.register("films",views.MovieViewSet,basename="films")

router.register("albums",views.AlbumViewSet,basename="albums")

router.register("tracks",views.TrackViewSetView,basename="tracks")


urlpatterns = [

    path("movies/",views.MovieListCreateView.as_view()),

    path("movies/<int:pk>/",views.MovieRetrieveUpdateDestroyView.as_view()),

    path("movies/languages/",views.LanguagesView.as_view()),

    path("movies/genres/",views.GenreView.as_view()),

]+router.urls