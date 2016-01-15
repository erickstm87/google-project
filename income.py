#!/usr/bin/python
#this code is my displacement algorithm
#Note: on the csv files the bash command 'grep -c "echo" FILE.csv"' will give me the count of true/false (echo) in the file 
import random
import csv
import math
class google_employee:  #object==google_employee

    def job_Select(type):
        foo = ['jd', 'sd', 'markman', 'softman']
        y = random.choice(foo)#randomly select the employees job title        
        return y
    def methodIncome(self):#based on this job selection they will be given an annual salary based on a random selection of the ranges below
        x = self.job_Select()
        if x=="jd": 
            x = random.randint(83680,139145) #jd=junior developer 
        elif x=="sd":
            x = random.randint(130036,198659) #sd=senior developer 
        elif x=="markman":
            x = random.randint(111502,161784) #markman=marketing manager
        elif x=="softman":
            x = random.randint(93389,176169) #softman=software manager
        return x
    def purchasing_income(self):#this is the home buyers/boring family heads of household
        p = True
        disposable = self.methodIncome()*4    #I took a really general rule of thumb that states one can 			afford a house 4 or even 5 times their gross annual income from http://www.mymoneyblog.com/4-different-rules-of-thumb-for-how-much-house-you-can-afford.html
        zz = random.choice(open('fixed1.csv').readlines()) #this is to pair the employees to housing availabilities
        if zz.isspace(): #this protects from an obnoxious error that comes up when the last line in csv file is selected
            return False  #this took ridiculously long to figure out        
        j = int(zz) #values pulled from the csv file need to be converted from string to int        
        new_housing = j+356708 #this is to adjust for the low housing property values that Boulder appraises 			at. I took the median values from both middle tier and top tier of all the zipcodes, found the median 			of these values, and am flatly adding the difference to the boulder values. New median values are 			taken from zillow            
        if (new_housing>=disposable): #if the house is too expensive they won't buy
            p = False
            print j,(','),p,(','),new_housing
        else: 
            p = True
            print j,(','),p,(','),new_housing
        #return j,disposable
    def rental_rates(self): #this is the renter half function, probably all miserable singles . . .
        p = True
        r_values = random.choice(open('fixed1.csv').readlines())  #pull from the rental values I 		sifted through craigslist for              
        if r_values.isspace(): #this protects from an obnoxious error that comes up when the last line in csv 			file is selected
            return False  #this took ridiculously long to figure out
        s = int(r_values)  #again convert my strings from csv to ints                         
        ss = s+356708        
        #http://www.investopedia.com/terms/p/price-to-rent-ratio.asp gives a formula for calculating the 			"price to rent" ratio. Since Boulder is a renters market with a rental vacancy around 2% I have 		manually set the 
        #price-to-rent ratio at 22 which the website considers to be "very good". I based this decision by 			pulling a few houses from Zillow and running this calculation manually 
        #the formula itself is price-to-rent = housing_price/(monthly_rent*12) so 22 = s/(monthly_rent*12)
        rent = ss/120 #rent = monthly_rent
        monthly_spendable = (self.methodIncome()/12)*.3 #the monthly portion of their incomes they can spend 			on housing 30% was the figure I pulled from the Housing market analysis
        if rent > monthly_spendable: #if the rent is too damn high
            p = False
            print s,(','),p,(','),rent
        else: #if they can 
            p = True
            print s,(','),p,(','),rent
        #return s,il
def main():
    i = 0   
    for i in range(0,600):#for this split I'm going to do half as home buyers and half as renter, this is the home buyer
        google_object=google_employee()
        (google_object.purchasing_income())
    for i in range(0,600): #this is the rental half
        google_object=google_employee()
        (google_object.rental_rates()) #note:after examining rental rates on craigslist I really wouldn't be surprised if they could afford all renting units
main()
