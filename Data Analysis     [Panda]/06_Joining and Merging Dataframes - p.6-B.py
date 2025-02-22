import pandas as pd

##Adat generalasa
df1 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

##df2 = pd.DataFrame({'HPI':[80,85,88,85],
##                    'Int_rate':[2, 3, 2, 2],
##                    'US_GDP_Thousands':[50, 55, 65, 55]},
##                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#left and right joiner [df1 df3]
merged = pd.merge(df1, df3, on= 'Year', how='left')
merged = pd.merge(df1, df3, on= 'Year', how='right')
#outer -> union of the keys , minden kulcs bent lesz
merged = pd.merge(df1, df3, on= 'Year', how='outer')
#metszet 
merged = pd.merge(df1, df3, on= 'Year', how='inner')
merged.set_index('Year', inplace=True)

print(merged)
#merge -> index nem szamit igazan
#join -> amikor az index szamit
#concat , pending -> nem igazan, teljes cucc-ot csinalhatunk
