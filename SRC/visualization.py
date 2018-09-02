

## Visualization

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


#### Maps visualizations #### 
from mpl_toolkits.basemap import Basemap, cm

latcorners = nc.variables['lat'][:]
loncorners = -nc.variables['lon'][:]
lon_0 = -nc.variables['true_lon'].getValue()
lat_0 = nc.variables['true_lat'].getValue()
# create figure and axes instances
fig = plt.figure(figsize=(8,8))
ax = fig.add_axes([0.1,0.1,0.8,0.8])
# create polar stereographic Basemap instance.
m = Basemap(projection='stere',lat_0=90.,lon_0=0, \
            llcrnrlat=latcorners[0],urcrnrlat=latcorners[2],\
            llcrnrlon=loncorners[0],urcrnrlon=loncorners[2], resolution='l',area_thresh=10000)


m.drawcoastlines()
m.drawstates()
m.drawcountries()
# draw parallels.
parallels = np.arange(0.,90,10.)
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
# draw meridians
meridians = np.arange(180.,360.,10.)
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
ny = df3.shape[0]; nx = df3.shape[1]
lons, lats = m.makegrid(nx, ny) 

### State wise plots


plt.figure(figsize=(12,8))
OH = Basemap(projection='mill', llcrnrlat = 38, urcrnrlat = 42.5, llcrnrlon = -85.5, urcrnrlon = -80, 
             resolution = 'h')
OH.drawcoastlines()
OH.drawcountries()
OH.drawstates()
a, b = OH(list(df3['longitude '].astype(float)), list(df3['latitude'].astype(float)), inverse=False)
OH.plot(a, b, "go", markersize = 4, alpha = 0.8, color = "green")

plt.title('UFO Sightings in Ohio')
plt.show()


### Mesh Grid

nx, ny = 10, 3

lon_bins = numpy.linspace(lons.min(), lons.max(), nx+1)
lat_bins = numpy.linspace(lats.min(), lats.max(), ny+1)

density, _, _ = numpy.histogram2d(lats, lons, [lat_bins, lon_bins])
lon_bins_2d, lat_bins_2d = numpy.meshgrid(lon_bins, lat_bins)

xs, ys = m(lon_bins_2d, lat_bins_2d)
plt.pcolormesh(xs, ys, density)
plt.colorbar(orientation='horizontal')
plt.scatter(*m(lons, lats))

plt.show()





pvt_tbl = pd.crosstab(df3['shape'], df3['dow_sighting'])
pvt_tbl.head()

pvt_tbl = pvt_tbl[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]

fig, ax = plt.subplots(figsize= (14,10))
yticks_lbl = ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

sns_plot_mon_shape = sns.heatmap(pvt_tbl, cmap= "RdPu", linewidths=.5, linecolor="grey")
plt.title("How the Shape of the Sightings varies across the day of the week")
#fig.suptitle("How the Shape of the Sightings varies across the months", fontsize = 12)
plt.show()
