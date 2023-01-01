from utils.Scrapper import IkeaScrapper, Scrapper,Ikea_Furniture
import time

if __name__== '__main__':


   
   target2 =Ikea_Furniture()

   path_dir= '/home/juc-lesaint/Desktop/data-collection-pipeline487/'
   folder ="raw_data1"
    
   target2.create_directory(path_dir,folder)     
   time.sleep(1)

   target2.ikea_living.collect_ikea_rooms_data()








    
    
    
