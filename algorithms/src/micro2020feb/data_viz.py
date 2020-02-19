import pandas as pd
import matplotlib.pyplot as plt
import re


path = "/Users/luisek/OneDrive/Documents/Applications/Microsoft/Feb2020/SSE DS Case Study - Take Home/"
yahoo_file = "yahoo_finance.csv"
comp_file = "us_company.csv"

yahoo_df = pd.read_csv(path+yahoo_file,header=0,sep=",")
#remove any nan
yahoo_df = yahoo_df.dropna()
company_df = pd.read_csv(path+comp_file,header=0,sep=",")

# Some data cleaning stuff
#Let's aggregate over "Company domain or its webpage
# Make company email domain lower caps and remove any https, or "" or "\"
def cleanUrl(str):
    str = str.lower()
    list_of_beginings = ["https://","https://www.","https://www2.","https://www3.","http://","http://www.","http://www2.","http://www3."]
    right_string_available = list(filter(lambda x:len(re.findall(x,str))>0,list_of_beginings))
    right_string = right_string_available[len(right_string_available)-1]
    str = str.replace(right_string,"").split(".") [0]
    return str+".com"

#apply function to both dataframes
company_df['CompanyEmailDomain'] = company_df.apply(lambda x:x['CompanyEmailDomain'].lower(),axis=1)
yahoo_df['Domain'] = yahoo_df.apply(lambda x:cleanUrl(x['Domain']),axis=1)

#Make employee numbers integers as opposed to string
yahoo_df['Num_Employees'] = yahoo_df.apply(lambda x:int(re.sub('[^0-9]+','',str(x['Num_Employees']))),axis=1)


## Lets aggregate over company emaild domain from both sides of the tables
company_df_web_pg = company_df[["LOCALSALES","USSALES","EMPTOTAL","CompanyEmailDomain"]].\
    groupby(['CompanyEmailDomain'],as_index=False).count()

yahoo_df_web_pg = yahoo_df[["MarketCap","Num_Employees","Domain"]].\
    groupby(['Domain'],as_index=False).count()