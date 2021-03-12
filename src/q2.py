"""
Performs data analysis to respond to our research question 2:
'Where in the U.S. is access to the internet least prevalent?'
Creates a map visualization of the counties in the U.S and their
proportion of a lack of internet access within the county.
"""
import altair as alt
import pandas as pd
import geopandas as gpd


def plot(internet_data, counties_data):
    """
    Takes in a DataFrame internet_data, containing data concerning U.S.
    counties' access to internet, and a GeoDataFrame counties_data, containing
    data to plot the U.S. counties on a map.
    Creates a choropoleth map visualization of the counties in the U.S.,
    displaying which counties have higher or lower percentages of households
    without access to the internet. Counties with missing data are
    colored gray.
    """
    # Shorten internet_data GEOID (ie 05000US02020 -> 02020)
    internet_data['GEOID'] = internet_data['GEOID'].apply(lambda v: v[-5:])

    # Base U.S. counties plot
    base = alt.Chart(counties_data).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).project('albersUsa').properties(
        width=750,
        height=450
    )

    # Choropleth map
    choro = alt.Chart(counties_data).mark_geoshape().encode(
        color='percent_no_internet:Q'
    ).transform_lookup(
        lookup='geoid',
        from_=alt.LookupData(internet_data, 'GEOID', ['percent_no_internet'])
    ).project(
        type='albersUsa'
    ).properties(
        width=750,
        height=450,
        title='Percentage of Households Without Internet in the U.S. (2016)'
    )

    q2_chart = base + choro
    q2_chart.save('q2_chart.html')


def main():
    # Load in data for testing
    data_5 = gpd.read_file('data/dataset-5.geojson')
    data_3 = pd.read_csv('data/dataset-3.csv')

    plot(data_3, data_5)

    # TESTING: check that percentages align with those plotted
    #   on the choropleth map
    # Refer to this file for testing examples:
    # https://docs.google.com/document/d/14rtCMhIXMW44TkX39KNcnKG_bM1Tr416BuGcN1sZrzE/edit?usp=sharing

    print(data_3[data_3['county'] == 'Wood County']['percent_no_internet'])
    print(data_3[data_3['county'] == 'Baldwin County']['percent_no_internet'])
    print(data_3[data_3['county'] == 'Natrona County']['percent_no_internet'])


if __name__ == '__main__':
    main()
