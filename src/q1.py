"""
Q1: How has internet access in US households, based on race,
    changed from 2015 to 2019?
For this question, we use data visualization to determine
    how internet access in US households, based on race, has
    changed from 2015 to 2019 by creating a line graph to examine
    the overall behavior and growth trends for each race.
"""
import altair as alt
import pandas as pd


def filter_data(data_2015, data_2016, data_2017, data_2018, data_2019):
    """
    - parameters: data_2015, data_2016, data_2017, data_2018,
        data_2019 -- all of which are dataframes
    - returns: "data" dataframe, combined from all filtered parameter
        dataframes to be used in creating line graph
    """
    # Load in datasets and filter
    datasets = [data_2015, data_2016, data_2017, data_2018, data_2019]
    data = {'2015': [], '2016': [], '2017': [], '2018': [], '2019': []}
    column_name = 'United States!!With a computer !!Percent  Broadband ' \
                  'Internet Subscription!!Estimate'
    year = 2015

    for dataset in datasets:
        dataset = dataset.loc[6:14, column_name].to_frame()
        for element in dataset[column_name]:
            data[str(year)].append(element)
        year += 1

    # Clean up dataframe and restructure
    df = pd.DataFrame(data)
    df = df.rename(index={0: "White",
                          1: "Black or African American",
                          2: "American Indian and Alaska Native",
                          3: "Asian",
                          4: "Native Hawaiian and Other Pacific Islander",
                          5: "Some other race",
                          6: "Two or more races",
                          7: "Hispanic or Latino origin (of any race)",
                          8: "White alone, not Hispanic or Latino"})
    df = df.T
    df.index.name = "Year"

    data = df.reset_index().melt('Year')
    data['value'] = data['value'].apply(lambda v: float(v[:-1]))
    data = data.rename(columns={'value': 'Percentage', 'variable': 'Race'})

    return data


def plot(data_2015, data_2016, data_2017, data_2018, data_2019):
    """
    - parameter: "data" dataframe, to be graphed
    - creates: "q1.html" line graph that shows the overall trends and behavior
        of how internet access in US households (based on race) has changed
        over the years 2015-2019
    """
    data = filter_data(data_2015, data_2016, data_2017, data_2018, data_2019)

    combined = alt.Chart(data).mark_line().encode(
        x='Year',
        y=alt.Y('Percentage', scale=alt.Scale(domain=[50, 100])),
        color='Race'
    ).properties(
        width=500,
        height=300,
        title='Internet Access in the US Across Races (2015-2019)'
    )

    # Selection that chooses nearest point and selects based on year
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
                            fields=['Year'])
    # Transparent selectors across chart: tells us x-value of cursor
    selectors = alt.Chart().mark_point().encode(
        x="Year:O",
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )
    # Text labels near points, displays percentage
    text = combined.mark_text(align='left', dx=3, dy=-3).encode(
        text=alt.condition(nearest, 'Percentage', alt.value(' '))
    )

    combined = alt.layer(combined, selectors, text, data=data)
    combined.save('q1_chart.html')


def main():
    # Load in data for testing purposes
    data_2015 = pd.read_csv('data/dataset-1-2015.csv')
    data_2016 = pd.read_csv('data/dataset-1-2016.csv')
    data_2017 = pd.read_csv('data/dataset-1-2017.csv')
    data_2018 = pd.read_csv('data/dataset-1-2018.csv')
    data_2019 = pd.read_csv('data/dataset-1-2019.csv')

    data = filter_data(data_2015, data_2016, data_2017, data_2018, data_2019)
    plot(data_2015, data_2016, data_2017, data_2018, data_2019)

    # TESTING: check that percentages align with those plotted on line graph
    # Refer to this file for testing documentation:
    # https://docs.google.com/document/d/14rtCMhIXMW44TkX39KNcnKG_bM1Tr416BuGcN1sZrzE/edit?usp=sharing

    print(data)

    print(data.loc[0, 'Percentage'])
    # refer to screenshot 1.1

    print(data.loc[6, 'Percentage'])
    # refer to screenshot 1.2

    print(data.loc[14, 'Percentage'])
    # refer to screenshot 1.3


if __name__ == '__main__':
    main()
