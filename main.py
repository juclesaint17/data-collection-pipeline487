from utils.Scrapper import IkeaScrapper, Scrapper,Ikea_Furniture
import time

if __name__== '__main__':

   #target = Scrapper()
   #target.accept_cookies()

    

   #target2 = Ikea_Furniture()
    #target2.ikea_living.navigate_Ikea_living_rooms_page()
    
   
   target = IkeaScrapper()
   time.sleep(1)
   target.display_Ikea_nav_links()
   #target.display_Ikea_products_links()
   time.sleep(1)


   target2 =Ikea_Furniture()
   target2.display_ikea_top_categories()

   path_dir= '/home/juc-lesaint/Desktop/data-collection-pipeline487/'
   folder ="raw_data1"
    
   target2.create_directory(path_dir,folder)     
   time.sleep(1)
   target2.ikea_living.collect_ikea_rooms_product_data()




   #target2.ikea_living.display_and_collect_ikea_room_products_data(living_room_links,item_cat_tag)




    
    
    
