# This is a sample Python script.
import pandas as pd
import pyodbc as py
df=pd.read_csv(r'C:\Users\Ezra\Desktop\Data1\movies_data_01.csv')
df.head()
df=df.dropna(subset='YEAR')
df=df.fillna(0)
df['GENRE'].str.strip()
df['ONE-LINE'].str.strip()
df['STARS'].str.strip()
df.GENRE=df.GENRE.replace('\n', ' ', regex=True)
df.STARS=df.STARS.replace('\n', '', regex=True)
df.YEAR = df.YEAR.astype('string')
df.YEAR=df.YEAR.replace('â€“','-',regex=True)
df['ONE-LINE']=df['ONE-LINE'].replace('\n-', '', regex=True)
df = df.rename(columns={'ONE-LINE': 'ONELINE'})
# print(year)
df.owner_company = df.owner_company.replace('\t', ' ', regex=True)
df.STARS = df.STARS.astype('string')

# df["Directors"]= n[0]
# df["Actors"] = n[1]

# df["Directors"]= n[0]

has_colon = df['STARS'].str.contains('\|')
df[['Directors', 'Actors']] = df.loc[has_colon, 'STARS'].str.split('\|',n=1, expand=True)
df['Actors']= df['STARS'].apply(lambda x: x.split('|')[1] if x.find('|')!=-1 else x)
print(df['Directors'][:20])
print(df['Actors'][:20])

# boolean_finding = df['STARS'].str.contains('Directors').any()
# print(boolean_finding)
# if df['STARS'].str.contains('Directors').any():
#       print(df['STARS'])

# df['name'] = df['STARS'].str.split('\|').str.get(0)
# print(df['name'])
# df2=df.query('STARS == Director')['STARS']

# print(out)

df['extraction_date'] = pd.to_datetime(df['Extract_date']).dt.date
df['extraction_time'] = pd.to_datetime(df['Extract_date']).dt.time


df['YEAR'] = df['YEAR'].str.replace(r'[()]',"",regex=True)
new = df["YEAR"].str.split("-", n = 1, expand = True)
df["Start_Year"]= new[0]
df["End_Year"] = new[1]
df['Start_Year'] = pd.to_numeric(df['Start_Year'],errors='coerce')
# .astype('Int64')

df['End_Year'] = pd.to_numeric(df['End_Year'],errors='coerce')
df['End_Year']=df['End_Year'].fillna(0)
df['Start_Year']=df['Start_Year'].fillna(1)
def conditions(s):
    if (s['End_Year']==0):
        return 'Present'
    elif (s['Start_Year']==1):
        return 'Movie'
    else:
        val=s['End_Year']-s['Start_Year']
        return val
df['Lasted'] = df.apply(conditions, axis=1)

