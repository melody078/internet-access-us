"""
Q3: How does access to the internet in the U.S. compare with
    global internet access?
For this question, we use data visualization to determine
    how internet access in the US compares with other countries,
    globally, by creating a choropleth map to examine
    the global distribution of internet access.
"""
import altair as alt
import geopandas as gpd
import pandas as pd


def merge_data(world_map, data_4):
    """
    - parameters: world_map GeoDataFrame, data_4 DataFrame
    - returns: "merged" DataFrame that combines world_map and
        data_4 via country names
    """
    merged = world_map.merge(data_4, left_on='name',
                             right_on='Country or Area', how='left')
    merged['Percentage'] = merged['Percentage'].fillna("0%")
    merged['Percentage'] = merged['Percentage'].apply(lambda v: str(v))
    merged['Percentage'] = merged['Percentage'].apply(
      lambda v: float(v.split('%')[0])
    )

    return merged


def plot(world_map, data_4):
    """
    - parameter: "merged" DataFrame that contains country names,
        percentage of internet access per country, and country geometries
    - creates "q3_map.html" choropleth map,
        shaded based on the percentage of population with internet
        access per country; darker shades = higher percentages;
        lighter shades = lower percentages; unavailable data = 0%
    """
    # Clean data
    merged = merge_data(world_map, data_4)

    # Plot
    q3_map = alt.Chart(merged).mark_geoshape().encode(
        color=alt.Color('Percentage:Q'),
        tooltip=['name', 'Percentage']
    ).properties(
        title='Percentage of People with Internet Access by Country (2018)'
    ).configure_view(
        height=600,
        width=800
    )

    q3_map.save('q3_chart.html')


def main():
    # Load in data for testing
    world_map = gpd.read_file("data/dataset-6.geojson")
    data_4 = pd.read_csv("data/dataset-4.csv")

    merged = merge_data(world_map, data_4)
    print(merged)

    plot(world_map, data_4)

    # TESTING: check that percentages align with those plotted
    #   on the choropleth map
    # Refer to this file for testing documentation:
    # https://docs.google.com/document/d/14rtCMhIXMW44TkX39KNcnKG_bM1Tr416BuGcN1sZrzE/edit?usp=sharing

    america_percent = merged[merged['name'] == "United States"]['Percentage']
    print(america_percent)
    # refer to screenshot 3.1

    chad_percent = merged[merged['name'] == "Chad"]['Percentage']
    print(chad_percent)
    # refer to screenshot 3.2

    mongolia_percent = merged[merged['name'] == "Mongolia"]['Percentage']
    print(mongolia_percent)
    # refer to screenshot 3.3


if __name__ == '__main__':
    main()
