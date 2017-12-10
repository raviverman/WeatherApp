import requests as web
import re 


city = input("Enter your city : ")
url = "https://www.weather-forecast.com/locations/"+city+"/forecasts/latest"
proxies = {}
# proxies={"https":"https://edcguest:edcguest@172.31.52.52:3128"}
rawdata = web.get(url, proxies).content
data = rawdata.decode("utf-8")
try:
    start = re.search('<span class="phrase">', data).end()
    end = start + re.search('</span>',data[start:]).start()
    print("Weather at " + city + " is " + data[start:end].replace("&deg;"," deg ") )
except:
    print("Error in collecting data.")