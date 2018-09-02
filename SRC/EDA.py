
## Script for exhaustive exploratory Data Analysis of the combined dataset

import pandas as pd 
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt 
from mpl_toolkits.basemap import Basemap

df = pd.read_csv('../data//full_final_UFO.csv')
df.head()

sns.countplot(y = df['Month_sighting'])
plt.title("How the sightings vary across month")
plt.show()

sns.countplot(y = df['dow_sighting'])
plt.title("How the sightings vary across month")
plt.show()

fig, ax = plt.subplots(figsize = (8,8))
sns.countplot(y = df['hour_sighting'])
plt.title("How the sightings vary across the hour of the day")
plt.show()

pvt_tbl = pd.pivot_table(df, index=['shape', 'Month_sighting'], values= 'index', aggfunc=len)
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
fig, ax = plt.subplots(figsize= (14,10))
sns_plot_mon_shape = sns.heatmap(pvt_tbl.unstack().T, cmap= "RdPu", linewidths=.5, yticklabels=month_list, linecolor="grey")
plt.title("How the Shape of the Sightings varies across the months")
#fig.suptitle("How the Shape of the Sightings varies across the months", fontsize = 12)
plt.show()

fig = sns_plot_mon_shape.get_figure()
fig.savefig("../images/Mon_shape_htmp")

pvt_tbl = pd.crosstab(df['shape'], df['dow_sighting'])
#pvt_tbl.head()
pvt_tbl = pvt_tbl[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
fig, ax = plt.subplots(figsize= (14,10))
yticks_lbl = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

sns_plot_mon_shape = sns.heatmap(pvt_tbl, cmap= "RdPu", linewidths=.5, linecolor="grey")
plt.title("How the Shape of the Sightings varies across the day of the week")
#fig.suptitle("How the Shape of the Sightings varies across the months", fontsize = 12)
plt.show()


def column_mean(x):
	m = x/sum(x)
	return m

pvt_tbl_perc = pvt_tbl.apply(column_mean, axis=0)
fig, ax = plt.subplots(figsize= (14,10))
yticks_lbl = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

sns_plot_mon_shape = sns.heatmap(pvt_tbl_perc, cmap= "RdPu", linewidths=.5, linecolor="grey", annot=True)
plt.title("How the Shape of the Sightings varies across the day of the week with percentage")
#fig.suptitle("How the Shape of the Sightings varies across the months", fontsize = 12)
plt.show()

fig2 = sns_plot_mon_shape.get_figure()
fig2.savefig("../images/Mon_shape_Perc_htmp")


df['date_real'] = df['date_pd'] 
df.set_index('date_pd', inplace=True)
df['date_real'] = pd.to_datetime(df['date_real'])
df['year'] = df['date_real'].map(lambda x: x.year)

fig, ax = plt.subplots(figsize = (12,8))
date_series = df['year'].value_counts()
date_series.sort_index(inplace=True)
date_series.plot()
plt.title("UFO Sightings varied across the years")
plt.show()


ca = df.loc[(df['state'] == 'ca'), 'year'].value_counts()
ca.sort_index(inplace=True)
fl = df.loc[(df['state'] == 'fl'), 'year'].value_counts()
wa = df.loc[(df['state'] == 'wa'), 'year'].value_counts()
tx = df.loc[(df['state'] == 'tx'), 'year'].value_counts()
ny = df.loc[(df['state'] == 'ny'), 'year'].value_counts()

fl.sort_index(inplace=True)
wa.sort_index(inplace=True)
tx.sort_index(inplace=True)
ny.sort_index(inplace=True)

fig, ax = plt.subplots(figsize = (12,8))

ax.plot(ca, label='CA')
ax.plot(fl, label='FL')
ax.plot(wa, label='WA')
ax.plot(tx, label='TX')
ax.plot(ny, label='NY')

legend = ax.legend(loc = 'upper left')
plt.title("State-wise UFO Sightings over the period of years")
plt.show()

ca = df.loc[df['state'] == 'ca']
fl = df.loc[(df['state'] == 'fl')]
wa = df.loc[(df['state'] == 'wa')]
tx = df.loc[(df['state'] == 'tx')]
ny = df.loc[(df['state'] == 'ny')]


fig = plt.figure(figsize=(20,15))
m = Basemap(projection='merc',lat_0=0,lon_0=0, \
			llcrnrlat=26,urcrnrlat= 50,\
			llcrnrlon=-125,urcrnrlon=-40, resolution='h')
			#,area_thresh=10000)
m.etopo()
#m.shadedrelief()
m.drawcoastlines()
m.drawstates()
#m.drawcountries()

#draw parallels
parallels = np.arange(0.,90,10.)
m.drawparallels(parallels,labels=[1,1,1,1],fontsize=10)
#draw meridians
meridians = np.arange(0.,360.,10.)
m.drawmeridians(meridians,labels=[1,1,1,1],fontsize=10)

#x, y = m(  list(df3['latitude'].astype('double')), list(df3['longitude '].astype('double')))
x, y =   m(list(df['longitude '].astype('double')),list(df['latitude'].astype('double')), inverse=False)
m.plot(x, y, "ro", markersize = 2, alpha = 0.5)
plt.title("UFO Sightings over the map of United States")
plt.show()

plt.figure(figsize=(12,8))
CA = Basemap(projection='mill', llcrnrlat = 31, urcrnrlat = 40.0, llcrnrlon = -120.5, urcrnrlon = -114, 
             resolution = 'h')
CA.drawcoastlines()
#CA.drawcountries()
CA.drawstates()
a, b = CA(list(ca['longitude '].astype(float)), list(ca['latitude'].astype(float)), inverse=False)
CA.plot(a, b, "go", markersize = 4, alpha = 0.8, color = "green")

plt.title('UFO Sightings in California')
plt.show()

plt.figure(figsize=(12,8))
FL = Basemap(projection='mill', llcrnrlat = 24, urcrnrlat = 31.5, llcrnrlon = -88, urcrnrlon = -80, 
             resolution = 'h')
FL.drawcoastlines()
#FL.drawcountries()
FL.drawstates()
a, b = FL(list(fl['longitude '].astype(float)), list(fl['latitude'].astype(float)), inverse=False)
FL.plot(a, b, "bo", markersize = 4, alpha = 0.8, color = "green")

plt.title('UFO Sightings in Florida')
plt.show()


plt.figure(figsize=(12,8))
NY = Basemap(projection='mill', llcrnrlat = 40, urcrnrlat = 45.5, llcrnrlon = -80, urcrnrlon = -71.75, 
             resolution = 'h')
NY.drawcoastlines()
#NY.drawcountries()
NY.drawstates()
a, b = NY(list(ny['longitude '].astype(float)), list(ny['latitude'].astype(float)), inverse=False)
NY.plot(a, b, "bo", markersize = 4, alpha = 0.8, color = "blue")

plt.title('UFO Sightings in NewYork')
plt.show()

plt.figure(figsize=(12,8))
WA = Basemap(projection='mill', llcrnrlat = 44.4, urcrnrlat = 49.4, llcrnrlon = -125.0, urcrnrlon = -116, 
              resolution = 'h')

#TX = Basemap(projection='mill', lon_0= -97.7253865, lat_0= 30.30, height= 804672, width=1644749.5)


WA.drawcoastlines() 
#WA.drawcountries()
WA.drawstates()
a, b = WA(list(wa['longitude '].astype(float)), list(wa['latitude'].astype(float)), inverse=False)
WA.plot(a, b, "bo", markersize = 4, alpha = 0.8, color = "blue")

plt.title('UFO Sightings in Washington')
plt.show()

print("SCRIPT SUCCESSFULLY RUN")

