#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

all_stats = pd.read_csv('../scHiC_Review/AllStatistics_ForBoxplot_ForPython_09_01_2024.csv', header=0)
all_stats['Cis/Trans'] = ((all_stats['Cis_Contacts'])/(all_stats['Total_Contacts']-all_stats['Cis_Contacts'] + 0.0000000000001))
dataset_names = list(set(all_stats['Authors'].tolist()))
additional_stats = ['Flyamer et al. 2017','Li et al 2023','Lee et al 2019']
dataset_names = [x for x in dataset_names if x not in additional_stats] 
stats = pd.DataFrame(columns = ['Dataset', 'Ref_Genome','Cells','Average_TotalContacts','Median_TotalContacts', 'Average_CisTotal','Median_CisTotal','Average_CisTrans','Median_CisTrans'])

for item in dataset_names:
    one_stats = all_stats[all_stats['Authors'] == item] 
    mean_total = one_stats['Total_Contacts'].mean()
    median_total = one_stats['Total_Contacts'].median()
    mean_cistotal = one_stats['Cis/Total'].mean()
    median_cistotal = one_stats['Cis/Total'].median()
    cell_num = len(one_stats)
    one_stats = one_stats.drop(one_stats[one_stats['Cis/Trans'] >=10000].index)
    mean_cistrans = one_stats['Cis/Trans'].mean()
    median_cistrans = one_stats['Cis/Trans'].median()
    genome = one_stats['Reference_Genome'].head(n=1).item()
    stats.loc[len(stats.index)] = [item, genome, cell_num, mean_total, median_total, mean_cistotal, median_cistotal,mean_cistrans, median_cistrans] 

for item in additional_stats: 
    one_stats = all_stats[all_stats['Authors'] == item]
    genomes = list(set(one_stats['Reference_Genome'].tolist()))
    for genome in genomes: 
        two_stats = one_stats[one_stats['Reference_Genome'] == genome]
        mean_total = two_stats['Total_Contacts'].mean()
        median_total = two_stats['Total_Contacts'].median()
        mean_cistotal = two_stats['Cis/Total'].mean()
        median_cistotal = two_stats['Cis/Total'].median()
        cell_num = len(two_stats)
        two_stats = two_stats.drop(two_stats[two_stats['Cis/Trans'] >=10000].index)
        mean_cistrans = two_stats['Cis/Trans'].mean()
        median_cistrans = two_stats['Cis/Trans'].median()
        stats.loc[len(stats.index)] = [item, genome, cell_num, mean_total, median_total, mean_cistotal, median_cistotal,mean_cistrans, median_cistrans] 

stats.to_csv('stats.csv')
