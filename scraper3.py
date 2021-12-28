import requests
from bs4 import BeautifulSoup

data=[]
make="Ford"
model="Focus"
year="2011"
area="Clare"
source="trade"
fuelType="Diesel"
transmission="Manual"
verification="any"


def scraper(make,model,year,area,source,fuelType,transmission,verification):
    data=[]
    req = requests.get("https://www.donedeal.ie/cars/"+make+"/"+model+"/"+year+\
                   "?area="+area+"&source="+source+"&fuelType="+fuelType+\
                    "&transmission="+transmission+\
                        "&verifications="+verification)
        
    
    req = requests.get("https://www.donedeal.ie/cars/"+make+"/"+model+"/"+year+\
                   "?area="+area+"&source="+source+"&fuelType="+fuelType+\
                    "&transmission="+transmission+\
                        "&verifications="+verification)

    soup = BeautifulSoup(req.content,"html.parser")
    
    raw=soup.get_text()
    raw=raw.split("correctly")
    raw=raw[1].split("Filter")[0]
    raw=raw.split("\n")

    raw2=[]

    for i in range(len(raw)):
        if len(raw[i])>0:
            raw2.append(raw[i])
            raw2=raw2[0].split("Price")
        
    

    
    for i in range(len(raw2)-1):
        try:
            if raw2[i+1][2]==",":
                price=raw2[i+1][0:6]
                raw2[i]=raw2[i]+price
                raw2[i+1]=raw2[i+1][6:]
            else:
                price=raw2[i+1][0:7]
                raw2[i]=raw2[i]+price
                raw2[i+1]=raw2[i+1][7:]
        except IndexError:
            continue
            
       
    
    for i in range(len(raw2)):
        try:
            if raw2[i][-4]!=",":
                raw2.remove(raw2[i])
            
            raw2.remove(raw2[-1])
        except IndexError:
            continue
       
    
    
    d=raw2[:]
    engine_size=raw2[:]
    for i in range(len(raw2)):
        if "Spotlight" in raw2[i]:
            if "km" in raw2[i]:
                raw2[i]=raw2[i].split(fuelType)
                raw2[i]=raw2[i][1]
                raw2[i]=raw2[i].split("km")
                raw2[i]=raw2[i][0]
                raw2[i]=raw2[i].strip()
                d[i]=d[i].split("€")
                d[i]=d[i][1].strip(",")
                engine_size[i]=engine_size[i][::-1].split(year[::-1],1)
                engine_size[i]=engine_size[i][0][-3:][::-1]
                data.append(["1","1",raw2[i],d[i]])
                
            elif "mi" in raw2[i]:
                raw2[i]=raw2[i].split(fuelType)
                raw2[i]=raw2[i][1]
                raw2[i]=raw2[i].split("mi")
                raw2[i]=raw2[i][0]
                raw2[i]=raw2[i].strip()
                d[i]=d[i].split("€")
                d[i]=d[i][1].strip(",")
                engine_size[i]=engine_size[i][::-1].split(year[::-1],1)
                engine_size[i]=engine_size[i][0][-3:][::-1]
                data.append(["1","0",raw2[i],d[i]])
        else:
            if "km" in raw2[i]:
                try:
                    raw2[i]=raw2[i].split(fuelType)
                    raw2[i]=raw2[i][1]
                    raw2[i]=raw2[i].split("km")
                    raw2[i]=raw2[i][0]
                    raw2[i]=raw2[i].strip(",")
                    d[i]=d[i].split("€")
                    d[i]=d[i][1].strip()
                    engine_size[i]=engine_size[i][::-1].split(year[::-1],1)
                    engine_size[i]=engine_size[i][0][-3:][::-1]
                    data.append(["0","1",raw2[i],d[i]])
                except IndexError:
                    continue
                
                
            elif "mi" in raw2[i]:
                try:
                    raw2[i]=raw2[i].split(fuelType)
                    raw2[i]=raw2[i][1]
                    raw2[i]=raw2[i].split("mi")
                    raw2[i]=raw2[i][0]
                    raw2[i]=raw2[i].strip()
                    d[i]=d[i].split("€")
                    d[i]=d[i][1].strip(",")
                    engine_size[i]=engine_size[i][::-1].split(year[::-1],1)
                    engine_size[i]=engine_size[i][0][-3:][::-1]
                    data.append(["0","0",raw2[i],d[i]])
                except IndexError:
                    continue
               
    
    if source=="private":
        dealership="0"
    elif source=="trade":
        dealership="1"
    if transmission =="Manual":
        trans="1"
    elif transmission == "Automatic":
        trans="0"
    
    
    

    for i in range(len(data)):
        data[i]=data[i]+[area]+[dealership]+[year]+[trans]+[engine_size[i]]
        data[i][2]=data[i][2].replace(",","")
        data[i][3]=data[i][3].replace(",","")
        
    return data

##greenlight checked data##
def final_data(make,model,year,area,source,fuelType,transmission):
    not_greenlight=scraper(make,model,year,area,source,fuelType,transmission,"any")
    greenlight=scraper(make,model,year,area,source,fuelType,transmission,"greenlightVerified")

    not_greenlight=[x for x in not_greenlight if x not in greenlight]

    for i in range(len(not_greenlight)):
        not_greenlight[i].append("0")
    for i in range(len(greenlight)):
        greenlight[i].append("1")

    data=not_greenlight+greenlight

    return data
    
    
   
            
        
                
        
    
    
    

