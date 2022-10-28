import json
from lib2to3.pgen2 import driver
from webbrowser import get
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from typing import List
import time
import pandas as pd
import numpy as np
import requests
import urllib.request
import os
import sys
from uuid import uuid4
from datetime import datetime



class Scrapper:

    def __init__(self, url: str = 'https://www.ikea.co.uk/'):
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)



    def select_product(self, xpath: str):
        '''
        Click on any link in the website

        Parameters
        ------------
        xpath: str
        The path of the link selected or clicked
        ''' 
        user_click = self.driver.find_element(By.XPATH, xpath)
        user_click.click()


    def search_product(self, product_name: str, xpath: str):
        '''
        Search product by usibg the webpage search box

        Parameters
        -------------
        product_name: the name of product to search
        xpath: the xpath of the search box
        '''
        search_product = self.driver.find_element(By.XPATH, xpath)
        search_product.click()
        time.sleep(1)
        search_product.send_keys(product_name)
        search_product.send_keys(Keys.RETURN)



    def accept_cookies(self, xpath: str = '//button[@id="onetrust-accept-btn-handler"]'):
        '''
        Click automatically the "Accept cookies button inthe website"

        Params
        ----------
        xpath: str
           The path of the Accept cookies button
        '''
        self.select_product(xpath)
    
    def visit_product_page(self, prod_xpath:str ):
        '''
        Visit a webpage link

        Params
        -------------
        prod_xpath: str
        the href link to visit the webpage link
        '''
    
        products= self.driver.find_element(By.XPATH, prod_xpath)
        a_tag = products.find_element(By.TAG_NAME, 'a')
        link = a_tag.get_attribute('href')
        print("The visiting webpage link is: ",link)
        self.driver.get(link)



    def collect_product_data(self):
        '''
        Collect product data in the webpage
        '''

        pass
    
    def download_product_images(self,product_img_url, product_path):
        '''
        Function to download images in a webpage and save it to a local machine
        Parameters:
        ---------------
        product_img_url: The url of the product image
        product_path: The destination folder to save the image

        '''

        product_img = self.requests.get(product_img_url).content
        with open(product_path, 'wb') as retriever:

            retriever.write(product_img)


    def create_dir(self,dir_path: str,folder_name):
        '''
        Create a directory in a given file path

        Parameters:
        dir_path: directory path to create the folder
        folder_name: the name of the folder to be created
        '''
        file_name = os.path.join(dir_path, folder_name)
        os.mkdir(file_name)


    def save_file(self,product_code,product_data):
        
        '''
        Within the directory of the created directory,create a new folder and save data.
        Parameters:

        file_path: the current directory path

        product_file: directory to be created,it can be a list or dict index
        product_data: data to save
        '''
        self.product_code = product_code
        self.product_data = product_data
        path = '/home/juc-lesaint/Desktop/data-collection-pipeline487/raw_data'
        
        if not os.path.exists(product_code):
            os.chdir(path)
            time.sleep(1)
            os.mkdir(product_code)
        with open(f"{product_code}/data.json", "w") as outfile:
            json.dump(product_data, outfile, indent=4)






    
    def site_pages_links(self, xpath_category: str, item_cat_tag: str) -> list:
        '''
        Display a list of available webpages links of the site.

        Parameters:
        --------------
        xpath_category:str
        The path of website subpages
        item_cat_tag:str
        the href link of the product site
        '''
        
        containers = self.driver.find_element(By.XPATH, xpath_category)
        #print(str(containers))
    
        item_category = containers.find_elements(By.XPATH, item_cat_tag)
        
        return item_category
            

    
        

class IkeaScrapper(Scrapper):

    # A method to search available product in the Ikea site
    def search_product_category(self):
        '''
        Search for product by using the search box

        Parameters:
        --------------
        product: str
        The product name to search
        search_bar_path: str
        the xpath of the search box

        '''
        self.accept_cookies()
        time.sleep(1)
        self.search_product(product_name= str, xpath='//input[@type="search"]')
        #self.select_product('//a[@data-index="0"]')

     # Display the navigation items link of IKea   
    def display_Ikea_nav_links(self):
        '''
        Display Ikea navigations links and store the links in a list
        parameters:
        -------------
        xpath_category:
        
        '''

        site_nav_links = self.site_pages_links(xpath_category='//ul[@class="hnf-header__nav__main"]' ,item_cat_tag='li')
        print("--- IKEA available navigation pages links---")

        site_nav_list =[]
        
        for nav_link in site_nav_links:
        
            nav_tag = nav_link.find_element(By.TAG_NAME, 'a')
            nav_link = nav_tag.get_attribute('href')
            site_nav_list.append(nav_link)
            
        return site_nav_list

    
    # Display the available Ikea products links
    def display_Ikea_products_links(self):
        '''
        Display Ikea products links pages
        '''
    
        products_site_link = self.site_pages_links(xpath_category='//ul[@data-tracking-label="products"]' ,item_cat_tag='li')
        print("---IKEA products list----")
        menu_product_list =[]
        
        for site_link in products_site_link:
        
            a_tag = site_link.find_element(By.TAG_NAME, 'a')
            link = a_tag.get_attribute('href')
            menu_product_list.append(link)
            
        return menu_product_list
        

    def close_dialog_windows(self, dialog_x_path: str ='/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/button/span'):
        '''

        Close the dialog box windows asking to enter area postcode

        Parameter:
        ---------------
        dialog_x_path: str
        The path of the dialog box windows
        '''
    
    

    def collect_data(self, item_path:str, data_path:str):
        '''
        Collect data from each IKEA pages and diplays the result in a formatted Dataframe tables.
        Function return null if there in no data to collect from a page

        Parameters:
        product_lists: List of all pages containing data
        data_path: The path of available data to scrappe

        '''
        products_dict = {
            'Date scrapped':[],
            'Product Code':[],
            'Product Brand': [],
            'Product Description': [],
            'Product Price(£)': [],
            'Product Images links': []
            }
        #product_frame = pd.DataFrame()

        for item in item_path:

            self.id_lists = item.find_elements(By.XPATH, data_path)
            
        for product_ref in self.id_lists:

            date = datetime.now()
            date_collected = date.strftime("%Y-%m-%d %H:%M:%S")
            products_dict['Date scrapped'].append(date_collected)

            product_code = product_ref.get_attribute("data-product-number")
            products_dict['Product Code'].append(product_code)      
                #print(product_code)
            product_name = product_ref.get_attribute("data-product-name")
            products_dict['Product Brand'].append(product_name)
                #print(product_name)
            product_price = product_ref.get_attribute("data-price")
            products_dict['Product Price(str(£))'].append(product_price)
                #print(product_price)

            product_description = product_ref.find_element(By.TAG_NAME, "a")
            description = product_description.get_attribute("aria-label")
            products_dict['Product Description'].append(description)

            product_image = product_ref.find_element(By.TAG_NAME, "img")
            image = product_image.get_attribute("src")    
            products_dict['Product Images links'].append(image)

        # creating the dictionary for each product by extractiong data from the main dictionary
        for index_code in range(len(products_dict['Product Code'])):
            product_data = {

                'Date scrapped': products_dict['Date scrapped'][index_code],
                'Product Code':  products_dict['Product Code'][index_code],
                'Product Brand': products_dict['Product Brand'][index_code],
                'Product Description': products_dict['Product Description'][index_code],
                'Product Price(£)': products_dict['Product Price(£)'][index_code],
                'Product Images links': products_dict['Product Images links'][index_code]
            }
        
           # product_frame = product_frame.append(product_data, ignore_index=True)

            # creating and saving files with given path
            product_frame = pd.DataFrame.from_dict(product_data,orient="index")

            product_file = str(product_data['Product Code'])             
            self.save_file(product_file,product_data)
            
            
        
        print("\t================================PRODUCTS DATA============================================")
        print(product_frame)
        #print(product_data)
        
        return product_frame
    

    

    def collect_images(self, image_path:str, image_source:str):
        '''
        Collecting image from Ikea webpages

        Parameters:
        image_path: the path of images sources
        image_source: the source link of the image

        '''
        images_list = []

        for products_imgs in image_path:
            self.images = products_imgs.find_elements(By.XPATH, image_source)
            
        for image_src in self.images:
            images_list.append(image_src.get_attribute('src'))
        
        print("=============PRODUCTS IMAGES URLS===========================")
        print(images_list)

        return images_list


     
class Ikea_Furniture(IkeaScrapper):

    def __init__(self):
        self.ikea_living = self.Ikea_Living_Room_Cat()

   
    def display_ikea_top_categories(self):
        
        self.accept_cookies()
        time.sleep(1)
        furniture_types_links = self.site_pages_links(xpath_category='//div[@id="pub__carousel__6f52285c-c220-11ec-a3dd-0948e2821b2e"]', item_cat_tag='./div')
        print("List 0f furnitures categories:")
        furnitures_list = []
        for furn_cat in furniture_types_links:

            a_tag = furn_cat.find_element(By.TAG_NAME, 'a')
            link = a_tag.get_attribute('href')
            furnitures_list.append(link)
            
        return furnitures_list


    class Ikea_Living_Room_Cat(IkeaScrapper):

        def navigate_Ikea_living_rooms_page(self):

            '''
            Nagivate to Ikea living room page.
            Params:
            ------------------
            prod_xpath: The xpath of Ikea living room page
            '''

            self.accept_cookies()
            time.sleep(1)
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f52285d-c220-11ec-a3dd-0948e2821b2e"]')
                            
        #self.close_dialog_windows()
            
            
        def display_living_room_products(self):
            '''
            Display Ikea all living room products categories pages
            Parameters:
            xpath_category: the xpath of all living room products
            item_cat_tag: product href

            '''   
            
            living_room_prod = self.site_pages_links(xpath_category='//*[@id="5a386581-e41e-11ec-aa30-f1ff1fc0055d"]/div/div/div[1]/nav',item_cat_tag='a')  

            count =0
            product_lists= []
            for product in living_room_prod:

                product_link = product.get_attribute('href')
                product_lists.append(product_link)
            print("--------------------------------------\tAll LIVING ROOM PRODUCTS LINKS----------------------------------------------------------")
            print("")
            print(product_lists)

            for link in product_lists:
              
                self.driver.get(link)
                count+=1
                print("-------------------------PRODUCT NUMBER:{} -------------".format(count))
                print("")
                print("======================================== PRODUCT URL LINK ===========================================================================")
                #time.sleep(1)
                print("\t",link)
                try:

                    self.display_and_collect_living_room_product_data()

                    
                    
                    time.sleep(1)
                except:
                    print("No data to collect for this link")
                    pass
                #break
                               
        # collect IKEA living room products datas
        def display_and_collect_living_room_product_data(self):
            '''
            Displays Ikea Living room products data like item price, item description and the product rating

            Parameters:
            
            '''

            product_list = self.site_pages_links(xpath_category='//div[@class="plp-product-list__products"]', item_cat_tag='./div')

            data_xpath = '//div[@class="pip-product-compact"]'
            self.collect_data(product_list,data_xpath)

            time.sleep(1)

            images_data = '//img[@class="pip-image"]'
            self.collect_images(product_list,images_data)




       
        #extract product images.   
        def extract_living_room_images(self):
            '''
            Collect Ikea living room products images
            

            
            self.create_dir("Living_room_images")

            item_path = self.site_pages_links(xpath_category='//div[@class="plp-product-list__products"]',item_cat_tag='./div')
            images_sources = []

            for products_imgs in item_path:
                images = products_imgs.find_elements(By.XPATH, '//img[@class="pip-image"]')            
            for image_src in images:
                images_sources.append(image_src.get_attribute('src'))
            print("-------- LIST OF PRODUCTS IMAGES URLS----")    
            print(images_sources)

            for image in range(len(images_sources)):

                self.download_product_images(images_sources[image], "Living_room_images/pics{}.jpg".format(image))
            print("Products images save successfully.")

             '''
            pass


    class Ikea_Garden_Cat:

        def navigate_Ikea_garden_page(self):
            self.accept_cookies()
            self.visit_product_page(prod_xpath='//*[@data-pub-id="90651450-d113-11ec-91f8-9f2328d7da79"]')
            self.close_dialog_windows()
        
        def display_Ikea_garden_products(self):
            '''
            Display Ikea all garden products categories pages
            Parameters:
            xpath_category: the xpath of all garden products
            item_cat_tag: product href

            '''   
            garden_products_prod = self.site_pages_links(xpath_category='',item_cat_tag='a')     
    
            product_lists= []
            for product in garden_products_prod:

                product_link = product.get_attribute('href')
                product_lists.append(product_link)
            print("All garden products categories")
            print(product_lists)

            for link in product_lists:
                self.driver.get(link)
                time.sleep(3)

        



    class Ikea_Home_Organisation:

        def navigate_Ikea_home_organisation_page(self):
            self.accept_cookies()
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f52285e-c220-11ec-a3dd-0948e2821b2e"]')
            self.close_dialog_windows()

        def display_home_organisation_products(self):
            '''
            Display Ikea all home organisations products categories pages
            Parameters:
            xpath_category: the xpath of all  products
            item_cat_tag: product href

            '''   
            home_organisation_prod = self.site_pages_links(xpath_category='',item_cat_tag='a')     
    
            product_lists= []
            for product in home_organisation_prod:

                product_link = product.get_attribute('href')
                product_lists.append(product_link)
            print("All home organisation categories")
            print(product_lists)

            for link in product_lists:
                self.driver.get(link)
                time.sleep(3)
 
    class Ikea_Decoration:

        def navigate_decoration_page(self):
            self.accept_cookies()
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f52285f-c220-11ec-a3dd-0948e2821b2e"]')
            self.close_dialog_windows()

        def display_Ikea_decoration_products(self):
            '''
            Display Ikea all decoration products categories pages
            Parameters:
            xpath_category: the xpath of all living room products
            item_cat_tag: product href

            '''   
            decorations_products = self.site_pages_links(xpath_category='',item_cat_tag='a')     
    
            product_lists= []
            for product in decorations_products:

                product_link = product.get_attribute('href')
                product_lists.append(product_link)
            print("All decorations pages categories")
            print(product_lists)

            for link in product_lists:
                self.driver.get(link)
                time.sleep(3)

    class Ikea_Cook_Table_Ware:
        def navigate_Ikea_cook_and_table_ware_page(self):
            self.accept_cookies()       
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f522860-c220-11ec-a3dd-0948e2821b2e"]')
            self.close_dialog_windows()

        def display_cook_table_products(self):
            '''
            Display Ikea all living room products categories pages
            Parameters:
            xpath_category: the xpath of all living room products
            item_cat_tag: product href

            '''   
            cook_tables_products = self.site_pages_links(xpath_category='',item_cat_tag='a')  
    
            product_lists= []
            for product in cook_tables_products:

                product_link = product.get_attribute('href')
                product_lists.append(product_link)
            print("All cook tables products")
            print(product_lists)

            for link in product_lists:
                self.driver.get(link)
                time.sleep(3)


    class Ikea_Storage_and_Organisation:

        def navigate_Ikea_storage_and_org_page(self):
            self.accept_cookies()
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f522861-c220-11ec-a3dd-0948e2821b2e"]')
            self.close_dialog_windows()

        def display_storage_and_organisation_products(self):
            '''
            Display Ikea all living room products categories pages
            Parameters:
            xpath_category: the xpath of all living room products
            item_cat_tag: product href

            '''   
            storage_organisation_prod = self.site_pages_links(xpath_category='',item_cat_tag='a')   
    
            product_lists= []
            for product in storage_organisation_prod:

                product_link = product.get_attribute('href')
                product_lists.append(product_link)
            print("Storage and organisations categories")
            print(product_lists)

            for link in product_lists:
                self.driver.get(link)
                time.sleep(3)    
    
    class Ikea_Kichen:


        def navigate_Ikea_kichen_page(self):
            self.accept_cookies() 
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f522862-c220-11ec-a3dd-0948e2821b2e"]')
            self.close_dialog_windows()

        def display_Ikea_kitchen_products(self):
            '''
            Display Ikea all living room products categories pages
            Parameters:
            xpath_category: the xpath of all living room products
            item_cat_tag: product href

            '''   
            kitchen_products = self.site_pages_links(xpath_category='',item_cat_tag='a')     
    
            product_lists= []
            for product in kitchen_products:

                product_link = product.get_attribute('href')
                product_lists.append(product_link)
            print("All kitchen categories")
            print(product_lists)

            for link in product_lists:
                self.driver.get(link)
                time.sleep(3)

    # select the item design
    def select_items_model(self, model_xpath:str):
        pass

    def get_items_data(self):
        pass
    





    
    


        

    

        



        





    






