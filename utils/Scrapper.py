import json
import selenium
import time
import requests
import urllib.request
import os
import sys
import pandas as pd
import numpy as np
from lib2to3.pgen2 import driver
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from typing import List
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

    def get_webpages_links(self,page_xpath):
    
        '''
        Store webpages links in a list and display the links

        Parameters:
        -------------------------------
        page_xpage: Variable representing the call of the sites_pages_links

        '''
        
        links_list = []
        for link_tag in page_xpath:
            navigation_tag = link_tag.find_element(By.TAG_NAME, 'a')
            navigation_link = navigation_tag.get_attribute('href')
            links_list.append(navigation_link)
        print(links_list)
        return links_list
    

    def display_images(self, image_path:str, image_source:str):
        '''
        Collecting images links for each page and display the links

        Parameters:
        ------------------------------------------
        image_path: the path of images sources
        image_source: the source link of the image

        '''
        images_list = []

        for products_imgs in image_path:
            self.images = products_imgs.find_elements(By.XPATH, image_source)
            
        for image_src in self.images:
            images = image_src.get_attribute('src')
            images_list.append(images)
        
        print("=============PRODUCTS IMAGES URLS===========================")
        print("")
        print("\tThe total number of images links is: {}".format(len(images_list)))
        print(images_list)

        return images_list


    def download_product_images(self,product_img_url, image_path):
        '''
        Function to download images in a webpage and save it to a local machine
        Parameters:
        ---------------
        product_img_url: The url of the product image

        product_path: The destination folder to save the image

        '''
        product_img = requests.get(product_img_url).content
        
        with open(image_path, 'wb') as retriever:

            retriever.write(product_img)


    def create_directory(self,dir_path: str,folder_name):
        '''
        Create a directory in a given file path

        Parameters:

        dir_path: directory path to create the folder

        folder_name: the name of the folder to be created
        '''
        file_name = os.path.join(dir_path, folder_name)
        if not os.path.exists(file_name):

            os.mkdir(file_name)
            print("FOLDER DREATED")
        else:
            print("FOLDER ALREADY EXISTS")
        

    def save_file(
        self, 
        product_code,
        product_data_dict, 
        parent_dir, 
        product_image_link,
        count
    ):
        
        '''
        Within the parent directory,create a new folder and save data and download products images

        Parameters:
        ------------------------

        product_code: the directory to store product with their unique ID.

        product_data_dict: the product data to be store in json file format.

        parent_dir: the path where the folder will be created.

        product_image_link: the product image to be store in product_code subfolder

        count: define the number of images uploaded into the images folder
        '''

        # created the date variable and assign it as image code name
        date = datetime.now()
        date_collected = date.strftime("%Y-%m-%d %H:%M:%S")
        
        if not os.path.exists(product_code):
            
            os.chdir(parent_dir)
            time.sleep(1)
            os.makedirs(f"{product_code}/images")
    
        with open(f"{product_code}/data.json", "w") as outfile:
            
            json.dump(product_data_dict, outfile, indent=4)
            
            self.download_product_images(product_image_link, f"{product_code}/images/{date_collected}_{product_code}_{count}.jpg")
            


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
        
        item_category = containers.find_elements(By.XPATH, item_cat_tag)
        
        return item_category
            

    
        

class IkeaScrapper(Scrapper):
    '''
    Class IkeaScrapper,a class that will inherit methods from the Scrapper class

    '''

    # A method to search available product in the Ikea site
    def search_product_category(self):
        '''
        Search for product by using the search box

        Parameters:
        --------------
        search_product: method inherited from the scrapper class that takes two arguments:
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
        sites_pages_links: method inherited from Srapper class and takes two args:

        xpath_category: the web page path
        item_cat_tag: the subpath of the navigation links
        
        '''

        site_nav_links = self.site_pages_links(xpath_category='//ul[@class="hnf-header__nav__main"]' ,item_cat_tag='li')
        print(" ")
        print("\t------------ IKEA available navigation pages links----------------------")
        self.get_webpages_links(site_nav_links)

        
    # Display the available Ikea products links
    def display_Ikea_products_links(self):
        '''
        Display Ikea products links pages
        '''
    
        products_site_link = self.site_pages_links(xpath_category='//ul[@data-tracking-label="products"]' ,item_cat_tag='li')
        print("")
        print("\t----------------IKEA products list---------------------------------------")
        self.get_webpages_links(products_site_link)
        
        

    def close_dialog_windows(self, dialog_x_path: str ='/html/body/div[5]/div/div[1]/div/div/div[2]/div[2]/button/span'):
        '''

        Close the dialog box windows asking to enter area postcode

        Parameter:
        ---------------
        dialog_x_path: str
        The path of the dialog box windows
        '''
        self.select_product(dialog_x_path)
    
    

    def collect_data(self, item_path:str, data_path:str):
        '''
        Collect data from each IKEA pages and diplays the result in a formatted Dataframe tables.
        Function return null if there in no data to collect from a page

        Parameters:
        product_lists: List of all pages containing data
        data_path: The path of available data to scrappe

        '''        
        products_dict = {
            'Time scrapped':[],
            'Product Code':[],
            'Product Brand': [],
            'Product Description': [],
            'Product Price(£)': [],
            'Product Images':[]
            }


        for item in item_path:
            product_data = item.find_elements(By.XPATH,  data_path)

        for data in product_data:

            date = datetime.now()
            date_collected = date.strftime("%Y-%m-%d %H:%M:%S")
            products_dict['Time scrapped'].append(date_collected)

            product_code = data.get_attribute("data-product-number")
            products_dict['Product Code'].append(product_code)      
                    
            product_name = data.get_attribute("data-product-name")
            products_dict['Product Brand'].append(product_name)
                    
            product_price = data.get_attribute("data-price")
            products_dict['Product Price(£)'].append(product_price)
                    
            product_description = data.find_element(By.TAG_NAME, "a")
            description = product_description.get_attribute("aria-label")               
            products_dict['Product Description'].append(description)
            
            product_image = data.find_element(By.TAG_NAME, "img")
            image = product_image.get_attribute("src")
            products_dict['Product Images'].append(image)

        product_frame = pd.DataFrame()
        count = 0

        for product_index in range(len(products_dict['Product Code'])):
            product_dict ={
                "Time collected":products_dict['Time scrapped'][product_index],
                "Product ID": products_dict['Product Code'][product_index],
                "product Brand": products_dict['Product Brand'][product_index],
                "Product Description": products_dict['Product Description'][product_index],
                "Product Price": products_dict['Product Price(£)'][product_index],
                "Product Image Link": products_dict['Product Images'][product_index]

            }
            count+=1
           
            product_frame = product_frame.append(product_dict, ignore_index=True) 
            product_file_data = str(product_dict['Product ID'])
            
            product_file_image = product_dict["Product Image Link"]

            path = '/home/juc-lesaint/Desktop/data-collection-pipeline487/raw_data1'
            
            self.save_file(product_file_data,product_dict,path,product_file_image,count)
        
        print("------------------------------------------------------------------------------------------------------------------")
        print("-----------\tTOTAL NUMBER OF IMAGES COLLECTED FROM THE PAGE: {} IMAGE(S)".format(count))

        print("\t================================PRODUCTS DATA====================================================================")
        print(product_frame)
        #print(product_dict)

        return product_frame  
            
        
    


     
class Ikea_Furniture(IkeaScrapper):
    

    def __init__(self):
        
        self.ikea_living = self.Ikea_Living_Room_Cat()
        super(Ikea_Furniture,self).__init__(url= 'https:www.ikea.co.uk')

   
    def display_ikea_top_categories(self):
        '''
        Displays the top categories links of IKEA

        '''
        
        self.accept_cookies()
        time.sleep(1)
        furniture_types_links = self.site_pages_links(xpath_category='//div[@id="pub__carousel__6f52285c-c220-11ec-a3dd-0948e2821b2e"]', item_cat_tag='./div')
        print("List 0f furnitures categories:")
        self.get_webpages_links(furniture_types_links)

       

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
            print("--------------------------------------\tAll LIVING ROOM PRODUCTS LINKS---------------------------------------------------------------------------------------------")
            print("")
            print(product_lists)

            for link in product_lists:
              
                self.driver.get(link)
                count+=1
                print("----------------------------------------------------PRODUCT NUMBER:{} ----------------------------------------------------------------------------".format(count))
                print("")
                print("======================================== PRODUCT URL LINK ======================================================================================================")
                #time.sleep(1)
                print("\t",link)
                print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
                try:

                    self.collect_living_room_product_data()                    
                    time.sleep(1)
                except Exception as e:
                    print(e)
                    print("No Data to Collect for this Link")
                    pass
            
        # collect IKEA living room products datas
        def collect_living_room_product_data(self):
            '''
            Displays Ikea Living room products data like item price, item description and the product rating

            Parameters:
            
            '''
            product_list = self.site_pages_links(xpath_category='//div[@class="plp-product-list__products"]', item_cat_tag='./div')
            data_xpath = '//div[@class="pip-product-compact"]'
            self.collect_data(product_list,data_xpath)



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
    





    
    


        

    

        



        





    






