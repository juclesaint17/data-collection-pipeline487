from utils.Scrapper import IkeaScrapper, Scrapper,Ikea_Furniture
import time

if __name__== '__main__':

    #target = Scrapper()
    #target.accept_cookies()

    

    #target2 = Ikea_Furniture()
    #target2.ikea_living.navigate_Ikea_living_rooms_page()
    
    #time.sleep(1)
    target = Ikea_Furniture()
    path_dir= '/home/juc-lesaint/Desktop/data-collection-pipeline487/'
    folder ="raw_data"
    target.create_dir(path_dir,folder)
    time.sleep(1)
    target.ikea_living.navigate_Ikea_living_rooms_page()
    time.sleep(1)
    target.ikea_living.display_living_room_products()
    
