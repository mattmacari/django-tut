from django.shortcuts import render

from vanilla import ListView, CreateView

from . import models


class PieceListView(ListView):
    model = models.Piece
