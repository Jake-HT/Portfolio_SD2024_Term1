import pandas as sadnap 
from sortingAlgorithms import bubble_sort

weight = sadnap.read_csv('kiwi_data.csv')
kiwiList = weight['Weight(kg)'].tolist()

kiwiListSorted = sorted(kiwiList)

