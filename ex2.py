
import requests
from bs4 import BeautifulSoup
import csv
linke="https://market.isagha.com/prices"
gold_details=[]
def main_code():
    page=requests.get(linke)
    soup=BeautifulSoup(page.content,'html.parser')
    golds=soup.find_all('div',{'class':'col-sm-12'}) 
    for n, i in enumerate(golds,1) :
        gauge=i.find('span').text
        sell_value=i.find_all('div',{'class':'value'})[0].text    
        buy_value=i.find_all('div',{'class':'value'})[1].text    
        status_value=i.find_all('div',{'class':'value'})[2].text    
        status=i.find_all('div',{'class':'state'})[2].text
        #print(n,gauge,sell_value,buy_value,status,status_value)
        #print('#'*30)
        gold_details.append({
           'العيار':gauge,
           'سعر البيع' :sell_value,
           'سعر الشراء' :buy_value,
           'الحالة' :status,
           'السعر' :status_value
        })

def printing():
#this function to print the file as csv formating 
    header=gold_details[0].keys()
    path="C:\\Users\\alber\Desktop\\gold_price.csv"
    with open(path,'w',encoding='utf-8',newline='') as file:
          writer=csv.DictWriter(file,header)
          writer.writeheader()
          writer.writerows(gold_details)
          print("file printed successfully")
  
        
main_code()
printing()
