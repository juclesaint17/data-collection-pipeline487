# Data-collection-pipeline487
## Project description


The Aim of this project is to build a software application that will extract information from a given website and store it in a database by using python programming language.To extract information for the website we use Selenium and webdriver.

### Milestone 1:
---
- In this first milestone,GitHub repos is created to track changes to the application codes.
- The repos created is cloned to the Linux Dedian 11 OS,by using the git command line argument:
 > "gh repo clone juclesaint17/data-collection-pipeline487"

- To avoid any packages conflit with our computer system, we create a virtual environment with Conda to isolate our project fromthe internal system. After the cloning, the directory is created to the computer file system and we access the folder with the linux command line terminal:
> "cd ~/name of directory".


### Milestone 2:
---
After setting up the repos to GitHub,the next step is the selection of the webpage category that will be build to collect data from. For this project Ecommerce website catagory is selected to develop  the application that will scrappe the data and store it to the database for processing. Ikea Ecommerce website will be used to test the functionnality of the application.

### Milestone 3:
---
- VS Code an integrated development environment is used to develop computer programs and websites and,it is used to our project to develop our pipeline program. From the folder created in the machine file system, we launch VS code inside the directory to create prototype that will allow us to retrieve every single page for the website.
We create a class file name "Scrapper".
Scrapper class contains many methods that will allow us to navigate to different pages in the website and collect data from each pages.
1. class Scrapper
> class Scrapper:

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
            
- For this piece of code to run and collect the data needed, some libraries were imported to the file as shows bellow:
>  import selenium
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


- Each function or method in the Scrapper class has different role, for example:
>  def  accept_cookies(self, xpath: str = '//button[@id="onetrust-accept-btn-handler"]'):

        '''
        Click automatically the "Accept cookies button inthe website"

        Params
        ----------
        xpath: str
           The path of the Accept cookies button
        '''
        self.select_product(xpath)

This method click automatically on the accept cookies dialog box when the page is loadedand displayed.
Another method like:
>def search_product(self, product_name: str, xpath: str):
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
click and send keys with a given product name inside the webpage search box and return the product information available on the website.

A powerfull method for this class Scrapper is:
> def select_product(self, xpath: str):
        '''
        Click on any link in the website

        Parameters
        ------------
        xpath: str
        The path of the link selected or clicked
        ''' 
        user_click = self.driver.find_element(By.XPATH, xpath)
        user_click.click()
This method finds a webpage by it xpath and click on it automatically, and most of others methods in the Scrapper class implement this function to perform some of their operations.

- Scrapper class for this project is the parent class, and others classes will inherit from it methods.

2. class IkeaScrapper:

This class is created to scrappe data from the Ikea Ecommerce website and inherit some methods from the Scrapper class and has it own methods to scrappe data from Ikea Ecommerce website.
The screenshot bellow show the IkeaScrapper class:
> class IkeaScrapper(Scrapper):
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

The IkeaScrapper class inherit methods from the parent parent class Scrapper.
for example the method:
 > def search_product_category(self):
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

This method perform a 'function call' from the parent class: accept_cookies() and search_product().
The IkeaScrapper method called :
 > def display_Ikea_nav_links(self):

        site_nav_links = self.site_pages_links(xpath_category='//ul[@class="hnf-header__nav__main"]' ,item_cat_tag='li')
        print("--- IKEA available navigation pages links---")

        site_nav_list =[]
        
        for nav_link in site_nav_links:
        
            nav_tag = nav_link.find_element(By.TAG_NAME, 'a')
            nav_link = nav_tag.get_attribute('href')
            site_nav_list.append(nav_link)
            
        return site_nav_list

This method select all available navigation pages links and store them in a list.

After implementing the code,we create a python file named main.py
>from utils.Scrapper import Scrapper
import time

if __name__== '__main__':

    target = Scrapper()
    target.accept_cookies()
    time.sleep(5)

This file is used to test the functionality of our project.
Inside the main.py file, we import the Scrapper class from the utils folder and it to a variable call target, and call the accept_cookies() ethod from the Scrapper class to test the functionality of each method inside the class.




    


    




