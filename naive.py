def find_quant(data,column,value):
    #example, would return as find_quant(data,1,"No")
    tscam = 0
    for i in data:
        if i[column] == value:
            tscam += 1
        return tscam
            

def is_spam(data,point):
    tscam = find_quant(data,0,"Yes")
    fscam = len(data) - tscam
    


data = ["No","No","No"
        "Yes","Yes","Yes"
        "Yes","Yes","Yes"
        "No","No","No"
        "No","No","Yes"
        "Yes","Yes","Yes"
        "No","Yes","No"
        "No","No","Yes"
        "Yes","Yes","No"
        "No","No","Yes"
        ]