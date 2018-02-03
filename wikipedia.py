# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:00:27 2018

@author: Johnny Wong
"""
   
import wikipedia
import matplotlib.pyplot as plt
import pandas as pd

trump = wikipedia.page('Donald Trump presidential campaign, 2016')

word_list = trump.content.lower().rstrip().replace('/n', ''
								   ).replace('[^a-z\s]','').split()

freq_dict = {}

for word in word_list:
	if word in freq_dict:
		freq_dict[word] += 1
	else:
		freq_dict[word] = 1

df = pd.DataFrame(list(freq_dict.items()), columns = ['word', 'count']).sort_values(
		'count', ascending = [False])

df['rank'] = list(range(1, df.shape[0]+1))
df['frequency'] = df['count']/df['count'].sum()
plt.scatter(df['rank'], df.frequency)

df