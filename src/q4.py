"""
Performs data analysis to respond to our research question 4:
'How does educational attainment relate to internet access?'
Creates a bar chart visualization of 5 urban and 5 rural counties' rates
of attaining a Bachelor's Degree and proportion of no internet access.
Urban and rural counties are pre-determined based on population density.
"""
import altair as alt
import pandas as pd


def clean(data, counties):
    """
    Takes in a Dataframe data containing information about the population,
    educational attainment, and internet access for U.S. counties.
    Takes in a list counties specifying the order of the counties.
    Cleans given data by filtering to only the necessary rows (counties)
    and columns.
    Returns filtered data.
    """
    # Filter to necessary rows/columns
    is_county = data['county'].isin(counties)
    data = data.loc[is_county, ['county', 'P_total', 'P_bachelor_and_above',
                                'percent_no_internet']]
    return data


def calculate_percentage(data):
    """
    Takes in a DataFrame data and calculates the proportion of counties'
    populations that do not have access to the internet.
    Further filters data and implements an order of 5 urban counties
    then 5 rural counties.
    Returns data with this additional information.
    """
    # Calculate proportion with bachelor's degree
    data['percent_bachelor'] = data['P_bachelor_and_above'] / data['P_total'] \
        * 100

    # Filter to necessary columns
    data = data.loc[:, ['county', 'percent_no_internet', 'percent_bachelor']]
    data = data.rename(
        columns={'county': 'County',
                 'percent_no_internet': 'Percent No Internet',
                 'percent_bachelor': "Percent Bachelor's Degree"}
    )
    # Reorder rows: urban first, then rural (same order as counties list)
    data = data.reindex([504, 55, 208, 700, 38, 477, 321, 771, 271, 288])

    # Combine both percent columns
    data = data.melt('County')
    data = data.rename(
        columns={'variable': 'Statistic', 'value': 'Percentage'}
    )

    return data


def plot(data):
    """
    Takes in a Dataframe data containing information about the population,
    educational attainment, and internet access for U.S. counties.
    Plots a grouped bar chart visualization comparing 5 urban and 5 rural
    counties, and the relationship between attaining a Bachelor's Degree
    and lacking internet access for these counties.
    """
    counties = ['New York County', 'Los Angeles County', 'Cook County',
                'Harris County', 'Maricopa County', 'Chaves County',
                'Aroostook County', 'Clallam County', 'McCracken County',
                'St. Landry Parish']

    data = clean(data, counties)
    data = calculate_percentage(data)

    # Plot
    q4_chart = alt.Chart(data).mark_bar().encode(
        x=alt.X(
            'Statistic',
            type='nominal',
            sort=counties,
            title=None,
            axis=alt.Axis(labels=False)
        ),
        y='Percentage:Q',
        color=alt.Color(
            'Statistic:N',
            scale=alt.Scale(range=['#96ceb4', '#ffcc5c']),
            title=None
        ),
        column=alt.Column(
            'County:N',
            sort=counties,
            header=alt.Header(
                titleOrient='bottom',
                labelOrient='bottom',
                labelAngle=-90,
                labelPadding=90,
                labelBaseline='middle'
            )
        )
    ).properties(
      title={
          'text': ['Internet Access and Education Attainment in Urban vs. ' +
                   'Rural Counties (2016)'],
          'subtitle': ['', '.         Urban         Urban         Urban      '
                       + '   Urban         Urban         Rural          Rural'
                       + '          Rural          Rural          Rural'],
          'subtitlePadding': 10
      }
    ).configure_title(
        fontSize=18,
        orient='top',
        offset=12,
        anchor='start'
    ).configure_axisX(
        labelPadding=100
    )

    q4_chart.save('q4_chart.html')


def main():
    # Load in data for testing
    data_3 = pd.read_csv('data/dataset-3.csv')

    counties = ['New York County', 'Chaves County']
    cleaned = clean(data_3, counties)
    cleaned = calculate_percentage(cleaned)

    plot(data_3)

    # TESTING: check that percentages align with those plotted
    #   on the choropleth map
    # Refer to this file for testing examples:
    # https://docs.google.com/document/d/14rtCMhIXMW44TkX39KNcnKG_bM1Tr416BuGcN1sZrzE/edit?usp=sharing

    print(cleaned[cleaned['County'] == 'New York County']['Percentage'])
    print(cleaned[cleaned['County'] == 'Chaves County']['Percentage'])


if __name__ == '__main__':
    main()
