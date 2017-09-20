from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list-pieces', view=views.PieceListView.as_view(), name='list_pieces')
]
