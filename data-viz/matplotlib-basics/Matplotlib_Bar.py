from matplotlib import pyplot as plt
import numpy as np
import csv
from collections import Counter
import pandas as pd

plt.style.use("fivethirtyeight")

# with open('data.txt') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

data = pd.read_csv('data.txt')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

language = []
popularity = []

for item in language_counter.most_common(100):
    language.append(item[0])
    popularity.append(item[1])

language.reverse()
popularity.reverse()

plt.barh(language, popularity)

plt.title("Most Popular Languages")
# plt.ylabel('Programming Languages')
plt.xlabel('Number of People Who Use')

plt.tight_layout()

plt.show()
