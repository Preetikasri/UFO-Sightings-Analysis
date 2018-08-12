import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

df = pd.read_csv('../data/scrubbed.csv', encoding='utf-8')

df = df.dropna()
df = df[df['country'] == 'us']
df['date posted'] = pd.to_datetime(df['date posted'])

def get_date(s):
    d = s.split(' ')[0]
    d = pd.to_datetime(d)
    return d

def get_hour(s):
    h = s.split(' ')[-1].split(':')[0]
    return h

def get_time(s):
    t = s.split(' ')[-1]
    return t

df['date_pd'] = df['datetime'].apply(get_date)
df['time_pd'] = df['datetime'].apply(get_time)

df = df[df['date_pd'] > pd.Timestamp('01-01-1984')]

#assert df.shape[0] == 59681

#### Heat maps ####
pvt_tbl = pd.pivot_table(df3, index=['shape', 'Month_sighting'], values= 'index', aggfunc=len)
pvt_tbl.unstack().head()
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

fig, ax = plt.subplots(figsize= (14,10))

sns_plot_mon_shape = sns.heatmap(pvt_tbl.unstack().T, cmap= "RdPu", linewidths=.5, yticklabels=month_list, linecolor="grey")
plt.title("How the Shape of the Sightings varies across the months")
#fig.suptitle("How the Shape of the Sightings varies across the months", fontsize = 12)
plt.show()

fig = sns_plot_mon_shape.get_figure()
fig.savefig("../images/Mon_shape_htmp")



