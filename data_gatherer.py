
def data_gatherer(make,model,years):
    from scraper3 import final_data
    data=[]


    counties=["Carlow","Cavan","Clare","Cork","Dublin","Galway","Kerry","Kildare","Kilkenny",
          "Laois","Leitrim","Limerick","Longford","Louth","Mayo","Meath","Monaghan",
          "Offaly","Roscommon","Sligo","Tipperary","Waterford","Westmeath",
          "Wexford","Wicklow"]
    sources=["private","trade"]
    fuelTypes=["Diesel","Petrol"]
    transmissions=["Manual","Automatic"]
    years=[str(x) for x in years]
  


    make=make
    model=model
    for e in transmissions:
        for c in fuelTypes:
            for d in sources:
                for b in years:
                    for a in counties:
                            
                        area=a
                        year=b
                        fuelType=c
                        source=d
                        transmission=e
                        make=make
                        model=model
                        data.append(final_data(make,model,year,area,source,fuelType,transmission))
    data=[x for x in data if type(x)==list]
    g1=[x for x in data if len(x)>1 ]
    e1=[x for x in data if len(x)==1]
    e2=[]
    for i in range(len(e1)):
        e2.append(e1[i][0])
    expanded=[]
    for i in range(len(g1)):
        for j in range(len(g1[i])):
            expanded.append(g1[i][j])

    data=expanded+e2

   
    data=[x for x in data if len(x)>0 and len(x[3])<7 and len(x[2])<9 and len(x)<=10 and len(x[8])<4]
    
    return data
            
  
    