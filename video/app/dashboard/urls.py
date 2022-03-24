from django.urls import path
from .views.base import Index
from .views.auth import Login, AdminManger, Logout, UpdateAdminStatus, ClientManager
from .views.video import (ExternaVideo, ExternaZiVideo, VideoSubView,
                          VideoStarView, StarDelete,
                          VideoSubDelete, VideoUpdate,
                          VideoExternaUpdate, VideoExternaDelete
                          )
from .views.comments import Comments, CommentsDelete


urlpatterns = [
    path('', Index.as_view(), name='dashboard_index'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('admin/manger', AdminManger.as_view(), name='admin_Manger'),
    path('admin/manger/update/status', UpdateAdminStatus.as_view(), name='admin_update_status'),
    path('video/externa', ExternaVideo.as_view(), name='externa_video'),
    path('video/externa_zi', ExternaZiVideo.as_view(), name='externa_video_zi'),
    path('video/videosub/<int:video_id>', VideoSubView.as_view(), name='video_sub'),
    path('video/star', VideoStarView.as_view(), name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>', StarDelete.as_view(), name='star_delete'),
    path('vdeio/sub/delete/<int:videosub_id>/<int:video_id>', VideoSubDelete.as_view(), name='sub_delete'),
    path('video/update/<int:video_id>', VideoUpdate.as_view(), name='video_update'),
    path('video/externa/update/<int:video_id>', VideoExternaUpdate.as_view(), name='video_externa_status'),
    path('video/externa/delete/<int:video_id>', VideoExternaDelete.as_view(), name='video_externa_delete'),
    path('comments/status/<int:comment_id>/<int:video_id>', Comments.as_view(), name='video_comment_status'),
    path('comments/delete/<int:comment_id>/<int:video_id>', CommentsDelete.as_view(), name='video_comment_delete'),
    path('client/user', ClientManager.as_view(), name='dashboard_client_user')
]
