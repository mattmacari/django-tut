from django.db import models


class Piece(models.Model):

    class Meta:
        managed = True

    piece_id = models.AutoField(primary_key=True)
    piece_name = models.CharField(max_length=100)

    def __str__(self):
        return self.piece_name