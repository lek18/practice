import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# Enter Data
path = "/Users/luisek/OneDrive/Documents/Applications/Microsoft/Feb2020/SSE DS Case Study - Take Home/"
yahoo_file = "yahoo_finance.csv"
comp_file = "us_company.csv"

yahoo_df = pd.read_csv(path+yahoo_file,header=0,sep=",")
#remove any nan
yahoo_df = yahoo_df.dropna()
company_df = pd.read_csv(path+comp_file,header=0,sep=",")

# Data Cleaning
#Let's aggregate over "Company domain or its webpage
# Make company email domain lower caps and remove any https, or "" or "\"
def cleanUrl(str):
    str = str.lower()
    list_of_beginings = ["https://","https://www.","https://www2.","https://www3.","http://","http://www.","http://www2.","http://www3."]
    right_string_available = list(filter(lambda x:len(re.findall(x,str))>0,list_of_beginings))
    right_string = right_string_available[len(right_string_available)-1]
    str = str.replace(right_string,"").split(".") [0]
    return str+".com"

def cleanMarketCap(string):
    # replace the dollar sign
    string = string.replace("$","")

    million_check = re.search("M",string)
    billion_check = re.search("B",string)
    if million_check is not None:
        string = string.replace("M","")
        value = float(string) * 1e6
    elif billion_check is not None:
        string = string.replace("B", "")
        value = float(string) * 1e9
    else:
        value = float(string)

    return value


#apply function to both dataframes
company_df['CompanyEmailDomain'] = company_df.apply(lambda x:x['CompanyEmailDomain'].lower(),axis=1)
yahoo_df['Domain'] = yahoo_df.apply(lambda x:cleanUrl(x['Domain']),axis=1)
yahoo_df['MarketCap'] = yahoo_df.apply(lambda x:cleanMarketCap(x['MarketCap']),axis=1)

#Make employee numbers integers as opposed to string
yahoo_df['Num_Employees'] = yahoo_df.apply(lambda x:int(re.sub('[^0-9]+','',str(x['Num_Employees']))),axis=1)


## Lets aggregate over company emaild domain from both sides of the tables
company_df_web_pg = company_df[["LOCALSALES","USSALES","EMPTOTAL","CompanyEmailDomain"]].\
    groupby(['CompanyEmailDomain'],as_index=False).sum()

yahoo_df_web_pg = yahoo_df[["Num_Employees","Domain"]].\
    groupby(['Domain'],as_index=False).sum()

# Question 1
# Let visualize company emptotal - both histograms and box plots
fig, ax = plt.subplots(2, 1)
ax[0].hist(company_df_web_pg['EMPTOTAL'],bins=50)
ax[1].boxplot(company_df_web_pg['EMPTOTAL'],vert=False)
ax[0].title.set_text('Histogram of EMPTOTAl - all data used')
ax[1].title.set_text('Boxplot of EMPTOTAl - all data used')

third_quartile = np.quantile(company_df_web_pg['EMPTOTAL'],0.75)
second_quartile = np.quantile(company_df_web_pg['EMPTOTAL'],0.25)
iqr = 1.5*(third_quartile-second_quartile)
max_val = iqr + third_quartile

company_df_web_pg['none_outlier'] = np.where(company_df_web_pg['EMPTOTAL']>=max_val,max_val,company_df_web_pg['EMPTOTAL'])
fig, ax = plt.subplots(1, 1)
ax.hist(company_df_web_pg['none_outlier'],bins=50)
ax.title.set_text('Histogram of EMPTOTAl - chopped at outlier')

# Question 2 - is the EMPTOTAL column accurate? looks like its not unless a lot of companies have only <1000 employee lol

# Couple of examples that are not
company_df_web_pg[company_df_web_pg['CompanyEmailDomain']=="apple.com"]
yahoo_df_web_pg[yahoo_df_web_pg['Domain']=="apple.com"]

company_df_web_pg[company_df_web_pg['CompanyEmailDomain']=="amazon.com"]
yahoo_df_web_pg[yahoo_df_web_pg['Domain']=="amazon.com"]

#Lets merge these two tables on basis of Domain == CompanyEmail Domain. Assume Yahoo has the correct values!

full_df = pd.merge(yahoo_df_web_pg, company_df_web_pg, how="left", right_on=['CompanyEmailDomain'], left_on=['Domain'])
full_df.shape[0] == yahoo_df_web_pg.shape[0]


#Check with companies are accurate!
a1 = full_df.sort_values(['EMPTOTAL'], ascending=False)
# Stringent condition - very few cases
top10_stringent = full_df[(~full_df['CompanyEmailDomain'].isna()) & (full_df['Num_Employees'] == full_df['EMPTOTAL'])].sort_values(['Num_Employees'], ascending=False)
# Let say that we can go ahead with 5% deviation error
top10_deviate5pct = full_df[(~full_df['CompanyEmailDomain'].isna()) & (abs((full_df['Num_Employees'] - full_df['EMPTOTAL'])/full_df['Num_Employees'])<=0.05)]
top10_deviate5pct['deviation'] = abs((full_df['Num_Employees'] - full_df['EMPTOTAL'])/full_df['Num_Employees'])
# Sort asc it by the ones that are devaiting more
top10_deviate5pct['max_rank'] = top10_deviate5pct['deviation'].rank(method='max')
top10_deviate5pct = top10_deviate5pct.sort_values(['deviation'], ascending=True)
top10_deviate5pct.to_csv(path+"top10_deviate5pct.csv",index=False)


#Top below - well lets just change top10_deviate5pct a bit
bottom10_stringent = full_df[(~full_df['CompanyEmailDomain'].isna()) & (abs((full_df['Num_Employees'] - full_df['EMPTOTAL'])/full_df['Num_Employees'])>0.05)]
bottom10_stringent['deviation'] = abs((bottom10_stringent['Num_Employees'] - bottom10_stringent['EMPTOTAL'])/full_df['Num_Employees'])
# Sort asc it by the ones that are devaiting more
bottom10_stringent['max_rank'] = bottom10_stringent['deviation'].rank(method='max')
bottom10_stringent = bottom10_stringent.sort_values(['deviation'], ascending=False)
bottom10_stringent.to_csv(path+"bottom10_stringent.csv",index=False)


## Question 3 additional interesting visaulization

#1. Want to have a look at MarketCap vs Num_Employees, LOCALSALES, USSALES ,EMPTOTAL  on all data that are within 5% deviation - i.e num of employes ~= emptotal
import seaborn as sns
corr = top10_deviate5pct[["Num_Employees", "LOCALSALES", "USSALES" ,"EMPTOTAL"]].corr()
ax = sns.heatmap(
    corr,
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)

a4_dimension = (11.7, 8.27)
fig, ax = plt.subplots(figsize=a4_dimension)
ax=sns.pairplot(company_df_web_pg[[ "LOCALSALES", "USSALES" ,"EMPTOTAL"]])

## Lets try a tree map on category
import squarify
#tree map of Market cap
df1 = yahoo_df[['Sector','MarketCap']].groupby(['Sector'],as_index=False).sum()
squarify.plot(sizes=df1['MarketCap'], label=df['Sector'], alpha=.8 )
plt.title("Tree map of total MarketCap By Sector")
plt.axis('off')
plt.show()

#tree map of count distinct of Domain
df2 = yahoo_df[['Sector','Domain']].drop_duplicates().groupby(['Sector'],as_index=False).count()
squarify.plot(sizes=df2['Domain'], label=df2['Sector'], alpha=.8 )
plt.title("Tree map of Distinct count Domain By Sector")
plt.axis('off')
plt.show()
