# Data-Mining
Generating data from donedeal.ie, using data mining, data cleansing and data manipulation techniques.

I used Python3 and the packages "requests" and "BeautifulSoup", to scrape data from ad's.
The data scraped from each ad is cleansed and manipulated in order to save the following data format to a CSV.

Index|     Description

0    |     Binary Variable, 1 if ad is a spotlight ad, 0 if not.
1    |     Binary Variable, 1 if Milage is measured in Km, 0 for Miles.
2    |     Milage (based on unit specified in index 1). 
3    |     Price.
4    |     County.
5    |     Binary Variable, 1 if ad is from dealership, 0 if not.
6    |     Year.
7    |     Binary Variable, 1 if car is manual, 0 if automatic.
8    |     Engine Size.
9    |     Binary Variable, 1 if ad is a greenlight ad, 0 if not.
10   |     Make
11   |     Model
