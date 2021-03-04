import pandas as pd
# import research question python files
import q1

def main():
  # load in data from csv files
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
  data_5 = pd.read_csv('data/dataset-5.csv')

  # clean up datasets

  # pass data to corresponding research question method
  print('test')
  print(q1.test(data_1_2015))

if __name__ == '__main__':
  main()