import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv', sep=";")


# Initialize the background map
plt.figure(figsize=(8, 10))
m=Basemap(llcrnrlon=-160, llcrnrlat=-75,urcrnrlon=160,urcrnrlat=80)

# Draw boundaries, continents and coastlins
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
m.drawcoastlines(linewidth=0.1, color="white")

# Add a point per position
m.scatter(
    data["homelon"],
    data["homelat"],
    s=data["n"]/10,
    c="#cf6925"
)

plt.text(-150, -75,
         'Proportion of cloud storage "areas", AWS\n\n',
         ha='left', va='bottom', size=9, color='#555555')


plt.show()