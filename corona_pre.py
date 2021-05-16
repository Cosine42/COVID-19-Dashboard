import pandas as pd
dates=[]
from kaggle.api.kaggle_api_extended import KaggleApi
import kaggle
api = KaggleApi()
api.authenticate()
print("Downloading data...")
for title in ('confirmed', 'recovered', 'deaths'):
    api.dataset_download_file('sudalairajkumar/novel-corona-virus-2019-dataset'\
                                  ,'time_series_covid_19_'+title+'.csv')
 
def Process(country):
   
    def pro(title):
        global dates

        conf_data=pd.read_csv('time_series_covid_19_'+title+'.csv')
        #print(conf_data.head())
        
        conf_data = joinNames(conf_data)
         
        conf_data.drop('Province/State', axis=1, inplace=True)

        conf_data=conf_data[conf_data['Country/Region']==country]

      
        conf_data=conf_data.T.reset_index()

        a, b = conf_data.columns
        
     
        conf_data=conf_data[4:].rename(columns={a:'date', b:title})
        
        conf_series=conf_data[title]

        dates = conf_data['date']

        return conf_series

    #total confirmed
    conf_series=pro('confirmed')

    #death
    temp=pro('deaths')
    ded_series = temp.diff().fillna(temp)

    #recovered
    rec_series=pro('recovered')

    #new cases
    new_series = conf_series.diff().fillna(conf_series)

    #active cases
    active_series = conf_series - ded_series - rec_series
 
    return (dates, conf_series, rec_series, active_series, ded_series, new_series)

def joinNames(data):
    for lab, row in data.iterrows():
        if str(data.loc[lab, 'Province/State'])!='nan':
            data.loc[lab, 'Country/Region'] = data.loc[lab, 'Country/Region'] +"--"+\
                          data.loc[lab, 'Province/State']
    return data
 
def getCountries():
    conf_data=pd.read_csv('time_series_covid_19_confirmed.csv')
    
    conf_data = joinNames(conf_data)

    countries = conf_data['Country/Region']
    return list(countries.unique() )
 
