from django.urls import path,include
# from watchlist_app.api.views import movie_list, movie_detail
from watchlist_app.api.views import GamePlatformVS,GamePlatform,ReviewCreate,ReviewDetail,ReviewList,WatchListAV,WatchDetailAV,GamePlatformAV,GamePlatformDetailAV
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('Game',GamePlatformVS,basename='gameplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(),name='game-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='game-detail'),

    path('',include(router.urls)),

    # path('stream/',StreamPlatformAV.as_view(),name='stream-list'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail'),

    # path('review/',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(),name='review-detail'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail')
]