from csv import reader
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    # your code here
    data=open('fruits.csv')
    read=reader(data)
    s=''
    money=3
    for i in read:
        if i[1]!='price' and money<float(i[1]):
            money=float(i[1])
            s=i[0]
    return  s
data=str()
print(get_expensive_fruit(data))