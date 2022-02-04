# from sqlite3 import connect
# from wsgiref.util import request_uri
import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser=argparse.ArgumentParser()
parser.add_argument("--page_num_max",help="enter the number of pages to parse",type=int)
parser.add_argument("--dbname",help="enter the number of pages to parse",type=int)
# parser.add_argument("--dbname",help="enter the name of db",type=str())
args=parser.parse_args()


oyo_url="https://www.oyorooms.com/search?location=Nagpur%2C%20Maharashtra%2C%20India&city=Nagpur&searchType=city&coupon=&checkin=03%2F02%2F2022&checkout=04%2F02%2F2022&roomConfig%5B%5D=2&showSearchElements=false&country=india&guests=2&rooms=1&filters%5Bcity_id%5D=43"

page_num_MAX=args.page_num_max
scrapped_info_list=[]
connect.connect(args.dbname)

for page_num in range(1,page_num_MAX):
    # url=oyo_url+str(page_num)
    # print("GET request for:"+url)
    req=requests.get(oyo_url+str(page_num))
    content=req.content

# print(content)
    soup=BeautifulSoup(content,"html.parser")

    all_hotels=soup.find_all("div",{"class":"hotelCardListting",})
    # scrapped_info_list={}

for hotel in all_hotels:
    hotel_dict={}
    hotel_dict["name"]= hotel_name=hotel.find("h3",{"calss":"ListingHotelDescription_hotelName"}).text
    hotel_dict["address"]= hotel_address=hotel.find("span",{"itemprop":"streetAddress"}).text
    hotel_dict["price"]= hotel_price=hotel.find("span",{"class":"ListingPrice_finalPrice"}).text
    
    try:
         hotel_dict["rating"] =hotel_rating=hotel.find("span",{"class":"hotelRating_ratingSummary"}).text
    except AttributeError:
        # hotel_dict["rating"]=None
        pass

    parent_amenities_element=hotel.find("div",{"c;ass":"amenityWrapper"})
    
    amenities_list=[]

    for  amenity in parent_amenities_element.finda_ll("div",{"c;ass":"amenityWrapper_amenity"}):
        amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

    hotel_dict["amenities"]=', '.join(amenities_list[:-1])

    scrapped_info_list.append(hotel_dict)
    connect.insert_list_table(args.dbname, tuple(hotel_dict.values()))

    # print(hotel_name,hotel_address, hotel_price, hotel_rating,amenities_list)

dataFrame=pandas.DataFrame(scrapped_info_list)
print("creating csv file..")
# dataFrame.to_csv("oyo.csv")
connect.get_hotel_info(args.dbname)





