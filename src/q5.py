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
    combined = prepare(data_2015, data_2016, data_2017, data_2018, data_2019)

    # Plot
    q5_chart = alt.Chart(combined).mark_line(point=True).encode(
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
        title='Internet Access of Different Household Income Levels'
    ).configure_title(
        fontSize=15,
        orient='top',
        offset=14,
        anchor='middle'
    ).configure_axisY(
        labelPadding=15
    )

    q5_chart.save('q5_chart.html')
