from utils.Scrapper import Scrapper, IkeaScrapper,Ikea_Furniture
import unittest
import os.path
from os import path

class ScrapperTestCase(unittest.TestCase):

    def setUp(self):
        self.ikea_scrapper = Scrapper()
        

    
    def test_folder_creation(self):
        print("CHECKING FOLDER CREATION")
        path = '/home/juc-lesaint/Desktop/data-collection-pipeline487/'
        folder = 'test_folder'
        #scrapper_dir = Scrapper()
        directory_check = self.ikea_scrapper.create_directory(path,folder)
        expected_value = '/home/juc-lesaint/Desktop/data-collection-pipeline487/test_folder'
        self.assertEqual(expected_value,directory_check)

    def test_ikea_search_product(self):
        print("CHECKING THE SEARCH BOX")
        check_search_box = self.ikea_scrapper.search_product('Furniture',xpath='//input[@type="search"]')
        expected_value = 'Furniture'
        self.assertEqual(expected_value,check_search_box)

    def test_visit_product_page(self):
        check_page = self.ikea_scrapper.visit_product_page(prod_xpath='//*[@data-pub-id="6f52285d-c220-11ec-a3dd-0948e2821b2e"]')
        expected_value = 'https://www.ikea.com/gb/en/rooms/living-room/'
        self.assertEqual(expected_value,check_page)

    def test_sites_pages(self):
        site_page = self.ikea_scrapper.site_pages_links(xpath_category='//ul[@class="hnf-header__nav__main"]' ,item_cat_tag='li')
        expected_value = [1,2,3,4]
        print(len(site_page))
        self.assertEqual(len(expected_value),len(site_page))


    def test_get_webpages_links(self):
        print(" CHECKING AVAILABLE LINKS")
        sites_subpages =self.ikea_scrapper.site_pages_links(xpath_category='//ul[@class="hnf-header__nav__main"]' ,item_cat_tag='li')
        available_links = self.ikea_scrapper.get_webpages_links(sites_subpages)
        expect_value = [1,2,3,4]
        print(len(available_links))
        self.assertEqual(len(expect_value), len(available_links))
     
    def test_download_images(self):
       check_download = self.ikea_scrapper.download_product_images(product_img_url='https://www.ikea.com/gb/en/images/products/friheten-corner-sofa-bed-with-storage-skiftebo-dark-grey__0175610_pe328883_s5.jpg?f=xxs',
       image_path='test_folder/img.jpg')
       expected_result = 'test_folder/img.jpg'
       print("File exists"+ expected_result)
       self.assertEqual(expected_result,check_download)

       


        

    
    #unittest.main(argv=[''], verbosity=6, exit=False)


