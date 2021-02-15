import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup
def realtime_rupee_value():
    url = ('https://in.finance.yahoo.com/quote/INR%3DX?p=INR%3DX') #Just put the url you want to extract data from
    r = requests.get(url) #r creates a request to get all inspection data from that url by using .get(url)

    #print(r.text) #If I print this,I will get the whole inspection content of that webpage

    web_content = BeautifulSoup(r.text,"lxml") #Now create a BeautifulSoup object, giving the whole inspection content as input and lxml as a parser library.
    #find() is used to find the content given as the parameter.
    web_content = web_content.find('div',{"class" : "My(6px) Pos(r) smartphone_Mt(6px)"} ) #Here I am parsing the rupee value from yahoofinance website.Just highlight the rupee value in webpage and click on inspect element by right clicking the mouse
    #div would be my header and we get some content which I wrote as key to class.If you need to extract multiple objects,just extend the dictionary further.

    #print(web_content) #Now printing that would give me the inspect content of that highlighted rupee value.From here I need to get the rupee value
    web_content = web_content.find("span").text #This value is under the span tag so I just found that here and asked to get me the text which is the value
    #print(web_content) #Hurray, I got the rupee value,72.5500 today
    
    if(web_content == []):
        web_content = '123456789' #Sometimes the website doesn't give us value during refreshing,so I assigned this garbage value to filter out later
    
    return web_content

def realtime_BSE_value():
    url = ('https://www.moneycontrol.com/india/stockpricequote/miscellaneous/bselimited/B08')
    r = requests.get(url)
    web_content = BeautifulSoup(r.text,"lxml") 
    #print(web_content)
    web_content = web_content.find('div',{"class" : "inprice1 nsecp"} ) 
    #print(web_content.text)
    web_content = web_content.text     
    if(web_content == []):
        web_content = '123456789' 
    
    return web_content

def realtime_Stock_value(stock_code):
    url = ('https://in.finance.yahoo.com/quote/' + stock_code + '?p=' + stock_code)
    #print(url)
    r = requests.get(url)
    web_content = BeautifulSoup(r.text,"lxml") 
    #print(web_content)
    web_content = web_content.find('div',{"class" : "D(ib) Mend(20px)"} ) 
    web_content = web_content.find("span").text
    #print(web_content)
         
    if(web_content == []):
        web_content = '123456789' 
    
    return web_content

NSE = ['MOTHERSUMI.NS','HEROMOTOCO.NS','BAJAJ-AUTO.NS','EICHERMOT.NS']

# print("Motherson Sumi Systems Limited: " + str(realtime_Stock_value('MOTHERSUMI.NS')))
# print("Hero MotoCorp Limited: "+ str(realtime_Stock_value('HEROMOTOCO.NS')))
# print("Bajaj Auto Limited: "+ str(realtime_Stock_value('BAJAJ-AUTO.NS')))
# print("Eicher Motors Limited: "+ str(realtime_Stock_value('EICHERMOT.NS')))
# print("USD Vs Rupee:" + str(realtime_rupee_value()))

for step in range(1,101):
    price = []
    cols = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock_code in NSE:
        price.append(realtime_Stock_value(stock_code))
    col = [time_stamp] 
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T 
    df.to_csv("/home/manju838/coding/env/pytorch_env/Live_Plotting/Realtime Motherson Sumi Systems Limited Stock Price.csv",header = False,mode = 'a')
    print(col)
    