import pandas as pd 
ms=pd.read_csv('main.csv')
k=[]
for i,j in ms.iterrows():
    if('US' not in j["COUNTRY"]):
        k.append(i)
ms.drop(ms.index[k], inplace=True)
ms.to_csv('filteredCountry.csv',index=False)
d={}
for i,j in ms.iterrows():
    if(j["SKU"] in d):
        d[j['SKU']].append(j["PRICE"])
    else:
        d[j["SKU"]]=[j["PRICE"]]
lowestPrice=pd.DataFrame(columns=["SKU", "FIRST_MINIMUM_PRICE","SECOND_MINIMUM_PRICE"])
for i in d:
    if(len(d[i])>1):
        sorted(d[i])
        lowestPrice.loc[len(lowestPrice.index)] = [i,d[i][0],d[i][1]]
lowestPrice.to_csv('lowestPrice.csv',index=False)
    
