from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger, Logout, UpdateAdminStatus
from .views.video import ExternaVideo, VideoSubView, VideoStarView, StarDelete, VideoSubDelete


urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manger', AdminManger.as_view(), name='admin_Manger'),
    path('admin/manger/update/status', UpdateAdminStatus.as_view(), name='admin_update_status'),
    path('video/externa', ExternaVideo.as_view(), name='externa_video'),
    path('video/videosub/<int:video_id>', VideoSubView.as_view(), name='video_sub'),
    path('video/star', VideoStarView.as_view(), name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>', StarDelete.as_view(), name='star_delete'),
    path('vdeio/sub/delete/<int:videosub_id>/<int:video_id>', VideoSubDelete.as_view(), name='sub_delete')
]
