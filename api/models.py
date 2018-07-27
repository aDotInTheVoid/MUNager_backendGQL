"""api/models.py: django models for the UCSMUN MUNager api"""

# Copyright (C) 2018  Nixon Enraght-Moony

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from django.db import models

# Create your models here.


class CardPage(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return "Cardpage: {}".format(self.name)


class Card(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(
        help_text="The main text body to display on the card")
    media = models.URLField(
        help_text="The absolute url to the image for the card")
    page = models.ForeignKey(CardPage, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
