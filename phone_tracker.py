from time import time
from numpy import number
import phonenumbers
from phonenumbers import geocoder,timezone,carrier
#from ifscApi.getDetails import FetchData

number= input("Enter your phone number")
#ifsc=input("Enter your ifsc code")

#data=FetchData().getdata(ifsc)

phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")

print(phone,'\n',car,'\n',reg,'\n',time,'\n')#,data)

