from django.contrib import admin

from . import models

@admin.register(models.Piece)
class PieceModelAdmin(admin.ModelAdmin):
    pass