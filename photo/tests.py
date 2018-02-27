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

class CategoryTestClass(TestCase):
    def setUp(self):
        self.test = Category(category="Nature")

    def test_instance(self):
        self.asserTrue(isinstance(self.test, Gallery))

    def test_saving_category(self):
        self.test.save_category()
        images = Category.objects.all()
        self.assertTrue(len(images) > 0)

    def test_deleting_category(self):
        self.test = Category(category="foodie")
        self.test.save_category()
        self.test.delete_locations()
        place = Category.objects.all()
        self.assertTrue(len(places)

class GalleryTestClass(TestCase):
    def setUp(self):
      
        self.test_location = Location(location="Nakuru")
        self.test_location.save()
       
        self.test_category = Category(category="Nature")
        self.test_category.save()      

        
        self.test_image = Gallery(image="image",image_url="Imageurl",image_name="patelimg",description="image from nairobi",location=self.test_place)  
        self.test_image.save()
        self.test_image.category.add(self.test_category)


    def test_saving_image(self):
        self.test_image.save_image()
        images = Gallery.objects.all()
        self.assertTrue(len(images) > 0)