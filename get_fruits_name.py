from csv import reader
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    data=open('fruits.csv')
    read=reader(data)
    lst=[]
    for i in read:
        if i[0]!="name":
            lst.append(i[0])
    return lst
data=str()
print(get_frutis_name(data))

    