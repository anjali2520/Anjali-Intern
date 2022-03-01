import dataclasses
import pandas as pd
import ast
class Customer():
    def __init__(self):
        self.CustomerName = input("Customer Name :-") 
        self.StoreName = input("Store Name :-")
        #read .csv file
        self.data = pd.read_csv("Store_list.csv") 
        
    def payment(self):
        index = list(self.data["Name"]).index(self.StoreName) # to find index value of store
        Grocery = ast.data[dataclasses["Name"] == self.StoreName]["Grocery"] # to fetch grocery items
        Grocery = ast.literal_eval(Grocery[index])  #Convert into Dict
        Price = sum(Grocery.values()) # total price of all grocery items price

        print(f" Customer Name :- {self.CustomerName} \n Store Name :- {self.StoreName} \n Grocery Name :- {Grocery} \n Total Price :- Rs {Price}") 

    def buy(self):
        try:            
            if (list(self.data["Name"]).index(self.StoreName)) != 0: #checking whether that store is available or not
                self.payment()
        except:

            raise Exception("Store Doesn't Exists")
a = Customer() #creating an object of a class
a.buy()
 