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
        print(link)
        self.driver.get(link)

    def get_product_data(self):
        pass
    

    
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

        site_nav_links = self.site_pages_links(xpath_category='//ul[@class="hnf-header__nav__main"]' ,item_cat_tag='li')
        print("--- IKEA available navigation pages links---")

        site_nav_list =[]
        
        for nav_link in site_nav_links:
        
            nav_tag = nav_link.find_element(By.TAG_NAME, 'a')
            nav_link = nav_tag.get_attribute('href')
            site_nav_list.append(nav_link)
            
        return site_nav_list

    
    # Display the availes Ikea products links
    def display_Ikea_products_links(self):
    
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
        self.select_product(dialog_x_path)


      # after launching the page scroll down and select top category to visit  
    #def display_ikea_top_category(self):
       # '''
       # Display IKEA top category products links

        #'''
        #products_site_link = self.site_pages_links(xpath_category='//*[@id="6f52285c-c220-11ec-a3dd-0948e2821b2e"]/div/div/div/div/div[1]/div' ,item_cat_tag='.//div')
       # print("---IKEA Category list----")
       # menu_product_list =[]
        
        #for site_link in products_site_link:
        
           # a_tag = site_link.find_element(By.TAG_NAME, 'a')
           # link = a_tag.get_attribute('href')
           # menu_product_list.append(link)
            

       # return menu_product_list

class Ikea_Furniture(IkeaScrapper):

    def navigate_Ikea_furniture_page(self):
        self.accept_cookies()
        self.visit_product_page(prod_xpath='//*[@data-pub-id="6f52285d-c220-11ec-a3dd-0948e2821b2e"]')
        self.close_dialog_windows()

    def display_furniture_categories(self):
        furniture_types_links = self.site_pages_links(xpath_category='//nav[@role="navigation"]', item_cat_tag='./a')
        print("List 0f furnitures categories:")
        furnitures_list = []
        for furn_cat in furniture_types_links:

            a_tag = furn_cat.find_element(By.TAG_NAME, 'a')
            link = a_tag.get_attribute('href')
            furnitures_list.append(link)
            
        return furnitures_list

    def get_furniture_data(self):
        pass


    '''
    def navigate_Ikea_garden_page(self):
        self.visit_product_page(prod_xpath='//*[@data-pub-id="90651450-d113-11ec-91f8-9f2328d7da79"]')
        self.close_dialog_windows()


    def navigate_Ikea_home_organisation_page(self):
       
        self.visit_product_page(prod_xpath='//*[@data-pub-id="6f52285e-c220-11ec-a3dd-0948e2821b2e"]')
        self.close_dialog_windows()
 
    def navigate_decoration_page(self):
        self.visit_product_page(prod_xpath='//*[@data-pub-id="6f52285f-c220-11ec-a3dd-0948e2821b2e"]')
        self.close_dialog_windows()

    def navigate_Ikea_cook_and_table_ware_page(self):
        
        self.visit_product_page(prod_xpath='//*[@data-pub-id="6f522860-c220-11ec-a3dd-0948e2821b2e"]')
        self.close_dialog_windows()

    def navigate_Ikea_storage_and_org_page(self):
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f522861-c220-11ec-a3dd-0948e2821b2e"]')
            self.close_dialog_windows()

    def navigate_Ikea_kichen_page(self):
            self.visit_product_page(prod_xpath='//*[@data-pub-id="6f522862-c220-11ec-a3dd-0948e2821b2e"]')
            self.close_dialog_windows()

    # select the item design
    def select_items_model(self, model_xpath:str):
        pass

    def get_items_data(self):
        pass
    '''





    
    


        

    

        



        





    






