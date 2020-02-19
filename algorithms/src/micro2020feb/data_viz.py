import pandas as pd
import matplotlib.pyplot as plt
import re


path = "/Users/luisek/OneDrive/Documents/Applications/Microsoft/Feb2020/SSE DS Case Study - Take Home/"
yahoo_file = "yahoo_finance.csv"
comp_file = "us_company.csv"

yahoo_df = pd.read_csv(path+yahoo_file,header=0,sep=",")
#remove any nan
company_df = pd.read_csv(path+comp_file,header=0,sep=",")

# Some data cleaning stuff
#Let's aggregate over "Company domain or its webpage
# Make company email domain lower caps and remove any https, or "" or "\"
def removePunction(str):
    str = str.lower()
    #str = re.sub('[^A-Za-z0-9]+', '', str)

    return str.replace("http://","").replace("/","").replace("www.","")

#apply function to both dataframes
company_df['CompanyEmailDomain'] = company_df.apply(lambda x:removePunction(x['CompanyEmailDomain']),axis=1)
yahoo_df['Domain'] = yahoo_df.apply(lambda x:removePunction(x['Domain']),axis=1)


## Lets aggregate over company emaild domain from both sides of the tables
company_df_web_pg = company_df[["LOCALSALES","USSALES","EMPTOTAL","CompanyEmailDomain"]].\
    groupby(['CompanyEmailDomain'],as_index=False).count()

yahoo_df = company_df[["LOCALSALES","USSALES","EMPTOTAL","CompanyEmailDomain"]].\
    groupby(['Domain'],as_index=False).count()