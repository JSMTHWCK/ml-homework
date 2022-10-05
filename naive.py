def find_quant(data,column,value):
    #example, would return as find_quant(data,1,"No")
    tscam = 0
    for i in data:
        if i[column] == value:
            tscam += 1
    return tscam
def find_in(data,column,value,boolval):
    a = 0
    for i in data:
        if boolval == i[0]:
            if i[column] == value:
                a += 1
    return a

def opposite(value):
    if value == "Yes":
        return "No"
    if value == "No":
        return "Yes"

def is_spam(data,point):
    tscam = find_quant(data,0,"Yes")
    fscam = len(data) - tscam

    pa_scam = find_in(data,1,point[1],"Yes")/tscam
    pb_scam = find_in(data,2, point[2],"Yes")/tscam

    pa_nscam = find_in(data,1,point[1],"No")/fscam
    pb_nscam = find_in(data,2,point[2],"No")/fscam
    t = pa_scam * pb_scam * tscam/len(data)
    f = pa_nscam * pb_nscam * fscam/len(data)

    if t > f:
        return "Yes"
    else:
        return "No"






data = [["No","No","No"],
        ["Yes","Yes","Yes"],
        ["Yes","Yes","Yes"],
        ["No","No","No"],
        ["No","No","Yes"],
        ["Yes","Yes","Yes"],
        ["No","Yes","No"],
        ["No","No","Yes"],
        ["Yes","Yes","No"],
        ["No","No","Yes"]
        ]

print(is_spam(data,["?","No","No"]))
print(is_spam(data,["?","Yes","Yes"]))
print(is_spam(data,["?","Yes","No"]))
print(is_spam(data,["?","No","Yes"]))