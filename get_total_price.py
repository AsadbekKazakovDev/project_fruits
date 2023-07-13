import csv
from pprint import pprint
def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    data = open("fruits.csv")
    read= csv.reader(data)
    s=0
    for t in read:
        if t[1]!="price":
            s+=float(t[1])
    return s
data = str()
pprint(get_total_price(data))
    
    

    