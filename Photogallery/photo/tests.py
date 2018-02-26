from django.test import TestCase
from . models import Gallery,Category,Image


#create your tests here
 class LocationTestClass(TestCase):
    def setUp(self):
         self.test_place(place="kirinyaga")

    def test_instance(self):
        self.assertTrue(isinstance(self.test_place,Location))

    def test_saving_place(self):
        self.test_place.save_places()
        place = Location.objects.all()
        self.assertTrue(len(place) > 0)     

