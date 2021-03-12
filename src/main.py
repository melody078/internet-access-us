"""
Melody Zhu and Kristy Nhan
CSE 163 Final Project
This program performs various operations and data analysis on data regarding
internet access in the U.S. across different demographics. Creates plots
involving said data to examine these disparities in access to the internet.
"""
import pandas as pd
import geopandas as gpd
import q1
import q2
import q3
import q4
import q5


def main():
    # Load in data from csv/geojson files
    data_1_2015 = pd.read_csv('data/dataset-1-2015.csv')
    data_1_2016 = pd.read_csv('data/dataset-1-2016.csv')
    data_1_2017 = pd.read_csv('data/dataset-1-2017.csv')
    data_1_2018 = pd.read_csv('data/dataset-1-2018.csv')
    data_1_2019 = pd.read_csv('data/dataset-1-2019.csv')

    data_2_2015 = pd.read_csv('data/dataset-2-2015.csv')
    data_2_2016 = pd.read_csv('data/dataset-2-2016.csv')
    data_2_2017 = pd.read_csv('data/dataset-2-2017.csv')
    data_2_2018 = pd.read_csv('data/dataset-2-2018.csv')
    data_2_2019 = pd.read_csv('data/dataset-2-2019.csv')

    data_3 = pd.read_csv('data/dataset-3.csv')

    data_4 = pd.read_csv('data/dataset-4.csv')

    data_5 = gpd.read_file('data/dataset-5.geojson')

    data_6 = gpd.read_file('data/dataset-6.geojson')

    # Pass data to corresponding research question method
    q1.plot(data_1_2015, data_1_2016, data_1_2017, data_1_2018, data_1_2019)
    q2.plot(data_3, data_5)
    q3.plot(data_6, data_4)
    q4.plot(data_3)
    q5.plot(data_2_2015, data_2_2016, data_2_2017, data_2_2018, data_2_2019)


if __name__ == '__main__':
    main()
