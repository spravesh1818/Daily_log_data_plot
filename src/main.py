import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt

data:DataFrame=pd.read_excel("/Users/praveshchapagain/Downloads/daily_logs.xlsx",sheet_name="Data",usecols="A:AG")
data['datetime']=data['English']+" "+data['Hrs']
data['datetime'] = pd.to_datetime(data['datetime'], format="%Y-%m-%d %H:%M:%S")

data.plot(x='datetime',y="MW +",)
plt.show()

