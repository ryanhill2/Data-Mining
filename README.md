# Data-Mining
Generating data from donedeal.ie, using data mining, data cleansing and data manipulation techniques.

I used Python3 and the packages "requests" and "BeautifulSoup", to scrape data from ad's.
The data scraped from each ad is cleansed and manipulated in order to save the following data format to a CSV.

Steps to run application

1 Check file data_golf.csv is empty

2 Run the write_to_csv.py file through the cli using "python write_to_csv.py" or using an IDE

Index|     Description

0    |     Binary Variable, 1 if ad is a spotlight ad, 0 if not.

1    |     Binary Variable, 1 if Milage is measured in Km, 0 for Miles.


3    |     Price.

4    |     County.

5    |     Binary Variable, 1 if ad is from dealership, 0 if not.

6    |     Year.

7    |     Binary Variable, 1 if car is manual, 0 if automatic.

8    |     Engine Size.

9    |     Binary Variable, 1 if ad is a greenlight ad, 0 if not.

10   |     Make.

11   |     Model.


This program gathers between 70 and 80% of data for a specific range of years and a chosen make and model of car. The remaining uncollected portion is due to variation in ads that can be unpredicatable and this program works only with ads where the price is given in euro.

There are three files in this upload:

Scraper3:
Contains function "final_data" which generates data from ad's according to specific conditions entered as arguments to the function.

Data_Gatherer:
Contains the function "data_gatherer" which iterates the "final_data" function from scraper3 through all possible inputs, for a certain range of years and a certain make and model.

Write_to_csv:
Calls the "data_gatherer" function from data_gatherer, here the inputs of a range of years, make and model are passed into the function and the resulting data is added to a CSV.
