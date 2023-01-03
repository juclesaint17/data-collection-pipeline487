# Data-collection-pipeline487
## Project description


The Aim of this project is to build a software application that will extract informations from a website and store them into a file locally by using python programming language.To extract informations for the website we will use Selenium and webdriver.

### Milestone 1:
---
- In this first milestone,GitHub repos is created to track changes to the application codes.
- The repos created is cloned to the Linux Dedian 11 OS,by using the git command line argument:
 > "gh repo clone juclesaint17/data-collection-pipeline487"

- To avoid any packages conflit with our computer system, we create a virtual environment with Conda to isolate our project fromthe internal system. After the cloning, the directory is created to the computer file system and we access the folder with the linux command line terminal:
> "cd ~/name of directory".


### Milestone 2:
---
After setting up the repos to GitHub,the next step is the selection of the webpage category that will be use to collect data from. For this project, Ecommerce website catagory is selected to develop  the application that will scrappe the data and store them into a local file for processing. Ikea Ecommerce website will be used to test the functionnality of the application.

### Milestone 3:
---
- VS Code an integrated development environment is used to develop computer programs and websites and,it is used to our project to develop our pipeline program. From the folder created in the machine file system, we launch VS code inside the directory to create prototype that will allow us to retrieve every single page for the website.
We create a class file named "Scrapper".
Scrapper class contains many methods that will allow us to navigate to different pages in the website and collect data from each page.
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
This method finds a webpage by xpath and click on it automatically, and most of others methods in the Scrapper class implement this function to perform some of their operations.

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

This method select all available navigations pages links and store them in a list.

After implementing the code,we create a python file named main.py
>from utils.Scrapper import Scrapper
import time

if __name__== '__main__':

    target = Scrapper()
    target.accept_cookies()
    time.sleep(5)

This file is used to test the functionality of our project.
Inside the main.py file, we import the Scrapper class from the utils folder and assign it to a variable call target, and call the accept_cookies() method from the Scrapper class to test the functionality of each method inside the class.

## Milestone 4:
In this milestone we create and define functions to retrieve products data and images from a single details page.As each page of Ikea website contains multiple webpages links for each product,we define a function to loop over all the links of the page and collect data and images for all the products available for the page.
The function below download images from the pages and store them in a file.


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
        print(image_path)
        return image_path

To collect data from the pages we define the function as shows below to loop through all webpages links, collect data and save them in a dictionary locally.


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




## Milestone 5:
After implementing classes and methods to run the software,we create a test_scraper python file to test the functionality of public methods created.
> testing public methods screenshots

     

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

In the test_scraper file we defined necessary tests methods to test the functionality of the methods of the scrapper class.
##Milestone 6:

After testing public functions of the project,an additional flag 'headless mode' was add to the webdrivers options to allow runnimg  the project without user graphical interface within the Docker container.After successfull implementation of the headless flag,we created a dockerfile to build the image of the scrapper project locally, test the image functionality and push the Docker image to Docker Hub.

##Milestone 7:
In this milestone we set up a CI/CD pipeline for the scrapper Docker image created in milestone 6.
First we set up GitHub secrets that contains credentials to push the scrapper image to a Docker Hub account and we create specific Git Hub actions to push the image to the main branch of the repository,and push the image to the Dockerhub account.
The screenshot below shows the Dockerfile created and the Git Hub actions implemented for the project.
> IkeaScrapper Dockerfile


 
    FROM python:latest

    RUN apt -f install -y

    RUN apt-get install -y wget

    RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

    RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
    RUN apt-get -y update
    RUN apt-get install -y google-chrome-stable

    RUN apt-get -y update


    RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

    RUN apt-get install -yqq unzip

    RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


    WORKDIR  /home/juc-lesaint/Desktop/data-collection-pipeline487/

    
    COPY . .

    #RUN pip install -r requirements.txt
    RUN  pip install -e .


    ENTRYPOINT ["python3", "main.py"]

-----------------------
> IkeaScrapper Actions file

    name: Ikea Scrapper ci

    on:
    push:
        branches:
        - "main"
    pull_request:
        branches:
        - "main"

    jobs:
    build:
        runs-on: ubuntu-latest
        steps:
        -
            name: Checkout
            uses: actions/checkout@v3
        -
            name: Login to Docker Hub
            uses: docker/login-action@v2
            with:
            username: ${{ secrets.DOCKER_HUB_JUCLART }}
            password: ${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}
        -
            name: Set up Docker Buildx
            uses: docker/setup-buildx-action@v2
        -
            name: Build and push
            uses: docker/build-push-action@v3
            with:
            context: .
            file: ./Dockerfile
            push: true
            tags: ${{ secrets.DOCKER_HUB_JUCLART }}/ikeascrapper:latest


                







    


    




