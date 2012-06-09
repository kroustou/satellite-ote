#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


SEMESTER_CHOICES = (
    (1, '4o'),
    (2, '6o'),
    (3, '8o'),
    (4, u'Επι πτυχείο')
)

DIRECTION_CHOICES = (
    (1, 'Διαδυκτιακά και υπολογιστικά συστήματα'),
    (2, 'Τεχνολογία λογισμικού και εφυή συστήματα'),
    (3, 'Πληροφοριακά συστήματα'),
)


# Create your models here.
class Participation(models.Model):
    last_name = models.CharField(u'Επώνυμο', max_length=255)
    first_name = models.CharField(u'Όνομα', max_length=255)
    fathers_name = models.CharField(u'Όνομα πατρός', max_length=255)
    id_number = models.CharField(u'Αριθμός μητρώου', max_length=8)
    home_phone = models.CharField(u'Σταθερό τηλέφωνο', max_length=15)
    mobile_phone = models.CharField(u'Κινήτο τηλέφωνο', max_length=15)
    email = models.EmailField()
    semester = models.IntegerField(u'Εξάμηνο', choices=SEMESTER_CHOICES)
    direction = models.IntegerField(u'Κατεύθυνση', choices=DIRECTION_CHOICES)
