"""
Performs data analysis to respond to our research question 5:
'How has internet access to U.S. households, based on income, changed from
2015 to 2019?'
Creates a line chart visualization of 3 different income levels, and their
access to internet across the years 2015-2019.
"""
import altair as alt
import pandas as pd


def prepare(data_2015, data_2016, data_2017, data_2018, data_2019):
    """
    Takes in 5 datasets, each corresponding to one year between 2015-2019,
    and each containing information about internet acess at different
    household income levels.
    Prepares these 5 datasets for plotting by combining desired data regarding
    percentage of households with internet access for 3 income levels
    into one dataset.
    Returns this combined dataset as a DataFrame.
    """
    # Get percentage of pop with internet for each income level
    datasets = [data_2015, data_2016, data_2017, data_2018, data_2019]

    combined = pd.DataFrame(columns=['Income', 'Year', 'Percent Internet'])

    # Combine into main dataframe
    year = 2015
    income_levels = ['Less than $20,000', '$20,000 to $74,999',
                     '$75,000 or more']
    income_indices = [24, 28, 32]
    # By year
    for dataset in datasets:
        # Get each income level's internet data
        for i, income in enumerate(income_levels):
            percent = dataset.loc[income_indices[i],
                                  'United States!!Percent!!Estimate']
            # Remove percent sign
            percent = percent[:-1]
            # Add to df
            combined = combined.append(
                {'Year': year, 'Income': income,
                 'Percent Internet': float(percent)},
                ignore_index=True)
        year += 1

    return combined


def plot(data_2015, data_2016, data_2017, data_2018, data_2019):
    """
    Takes in 5 datasets, each corresponding to one year between 2015-2019,
    and each containing information about internet acess at different
    household income levels.
    Plots a line chart visualization with each line representing a household
    income level, displaying how the percentage of households with internet
    for these income levels has changed over the years 2015-2019.
    """
    data = prepare(data_2015, data_2016, data_2017, data_2018, data_2019)

    # Initial layer
    chart = alt.Chart(data).mark_line(point=True).encode(
        x=alt.X('Year:O'),
        y=alt.Y(
            'Percent Internet',
            title='Percentage Households with Internet'),
        color=alt.Color(
            'Income:N',
            scale=alt.Scale(range=['#96ceb4', '#ffcc5c', '#ff6f69']),
            sort=None
        )
    ).properties(
        width=500,
        height=300,
        title='Internet Access of Different Household Income Levels' +
              ' (2015-2019)'
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
    # Labels near points, displaying percent with internet access per income
    text = chart.mark_text(align='left', dx=3, dy=-3).encode(
        text=alt.condition(nearest, 'Percent Internet', alt.value(' '))
    )

    # Combine layers and plot
    combined = alt.layer(chart, selectors, text, data=data).configure_title(
        fontSize=15,
        orient='top',
        offset=14,
        anchor='middle'
    ).configure_axisY(
        labelPadding=15
    )

    combined.save('q5_chart.html')


def main():
    # Load in data for testing purposes
    data_2015 = pd.read_csv('data/dataset-2-2015.csv')
    data_2016 = pd.read_csv('data/dataset-2-2016.csv')
    data_2017 = pd.read_csv('data/dataset-2-2017.csv')
    data_2018 = pd.read_csv('data/dataset-2-2018.csv')
    data_2019 = pd.read_csv('data/dataset-2-2019.csv')

    data = prepare(data_2015, data_2016, data_2017, data_2018, data_2019)
    plot(data_2015, data_2016, data_2017, data_2018, data_2019)

    # TESTING: check that percentages align with those plotted on line graph
    # Refer to this file for testing documentation:
    # https://docs.google.com/document/d/14rtCMhIXMW44TkX39KNcnKG_bM1Tr416BuGcN1sZrzE/edit?usp=sharing

    print(data)

    print(data.loc[0, 'Percent Internet'])
    print(data.loc[6, 'Percent Internet'])
    print(data.loc[14, 'Percent Internet'])


if __name__ == '__main__':
    main()
