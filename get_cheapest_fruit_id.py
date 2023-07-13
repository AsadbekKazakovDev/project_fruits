from csv import reader
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    data=open('fruits.csv')
    read=reader(data) 
    money=351
    for i in read:
        if i[1]!='price' and money>float(i[1]):
            money=float(i[1])
    return int(money)
data=str()
print(get_cheapest_fruit_id(data))
    