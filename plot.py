
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as pgd
from  shapely.geometry import Point

def polt_on_map(datafile, mapfile,start_point):
    df = pd.read_csv(datafile)
    start_point_y = df['Longitude'].iloc[0]
    start_point_x = df['Latitude'].iloc[0]



    Longtitude_err = start_point_y - start_point[1]
    Latitude_err =  start_point_x - start_point[0]
    df['Longtitude_new'] = (-1)* (df['Longitude'] - Longtitude_err) /100.0
    df['Latitude_new'] =  (df['Latitude'] - Latitude_err) /100.0

    street_map = pgd.read_file(mapfile)
    fig, ax = plt.subplots(figsize=(15, 15))
    street_map.plot(ax=ax)
    geometry = [Point(xy) for xy in zip(df['Longtitude_new'], df['Latitude_new'])]
    crs = {'init', 'epsg:4326'}
    geo_df = pgd.GeoDataFrame(df,
                              crs = crs,
                              geometry = geometry)
    fig, ax = plt.subplots(figsize=(15, 15))
    street_map.plot(ax=ax ,alpha=0.4,color = 'gray')
    geo_df.plot(ax=ax,markersize = 20, color = 'blue')
    plt.show()


if __name__ == '__main__':

    polt_on_map('out.csv','michigan_highway.shp',[4273.2089, 8321.8809] )