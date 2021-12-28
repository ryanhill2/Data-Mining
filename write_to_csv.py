from datetime import datetime
from data_gatherer import data_gatherer
start_time=datetime.now()

make="Volkswagen"
model="Golf"
years=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]

data=data_gatherer(make,model,years) 
file=open("data_golf.csv","w")
for line in data:
    file.write(','.join(line) +','+make+','+model+ '\n')
file.close()

end_time=datetime.now()

print("Runtime:{}".format(end_time-start_time))
