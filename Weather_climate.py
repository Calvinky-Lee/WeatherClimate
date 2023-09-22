convertDict = {"ON":"Ontario","BC":"British Colombia","SK":"Saskatchewan","NL":"Newfoundland and Labador","PE":"Prince Edward Island",\
                "NS":"Nova Scotia","NB":"New Brunswick","QC":"Quebec","MB":"Manitoba","AB":"Alberta","NT":"Northwest Territorys","NU":"Nunavut",\
               "YT":"Yukon"}
provinceDict = {"Ontario":[],"British Colombia":[],"Saskatchewan":[],"Newfoundland and Labador":[],"Prince Edward Island":[],\
                "Nova Scotia":[],"New Brunswick":[],"Quebec":[],"Manitoba":[],"Alberta":[],"Northwest Territorys":[],"Nunavut":[],\
               "Yukon":[]}
with open("climateData.csv") as file_in:
    for i in range(32):
        file_in.readline()

    for data in file_in:

        data = data.replace('"','').strip().split(",")
        prov = convertDict[data[3]]
        provinceDict[prov] +=[data[0]]


print(provinceDict)
