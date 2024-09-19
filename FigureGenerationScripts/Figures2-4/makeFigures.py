#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

all_stats = pd.read_csv('./AllStatistics_ForBoxplot_09_01_2024.csv', header=0)
all_stats['Cis_Contacts'] = all_stats['Cis_Contacts'].astype(int)
all_stats['Cis/Total']=all_stats['Cis_Contacts']/all_stats['Total_Contacts']
dataset_names = list(set(all_stats['Authors'].tolist()))
all_stats['Cis/Trans'] = ((all_stats['Cis_Contacts'])/(all_stats['Total_Contacts']-all_stats['Cis_Contacts'] + 0.0000000000001))
 
#%% Separate data by reference genome
mm9 = all_stats[(all_stats['Reference_Genome'] == "mm9") ]
rgap7 = all_stats[all_stats['Reference_Genome'] == "rgap7"]
dm3 = all_stats[all_stats['Reference_Genome'] == "dm3"]
mm10 = all_stats[(all_stats['Reference_Genome'] == "mm10")]
hg19 = all_stats[(all_stats['Reference_Genome'] == "hg19")]
hg38 = all_stats[(all_stats['Reference_Genome'] == "hg38")] 

#%% Total contacts - Figure 2
fig, axes = plt.subplots(2, 3,  figsize=(20,22), constrained_layout=True, gridspec_kw={'width_ratios': [1.5, 1, 0.25]})
sns.set()
#fig.suptitle('Single-Cell Chromatin Interaction Total Contacts for Single-Cells by Reference Genome')
sns.boxplot(ax=axes[0, 0], data=mm9, x='Authors', y='Total_Contacts',log_scale=True, width = 0.5, color = '#8c564b').set(title= 'Mouse (mm9)',xlabel=None, ylabel='Total Contacts')
sns.boxplot(ax=axes[1, 0], data=mm10, x='Authors', y='Total_Contacts', log_scale=True,width=0.6, color = '#9467bd').set(title = 'Mouse (mm10)',xlabel=None, ylabel ='Total Contacts')
sns.boxplot(ax=axes[0, 2], data=rgap7, x='Authors', y='Total_Contacts', log_scale=True,width=0.3, color = '#e377c2').set(title='Rice (rgap7)', xlabel=None, ylabel = None)
sns.boxplot(ax=axes[1, 1], data=hg19, x='Authors', y='Total_Contacts', log_scale=True,width=0.5, color = '#ff7f0e').set(title='Human (hg19)', xlabel=None, ylabel=None)
sns.boxplot(ax=axes[0, 1], data=hg38, x='Authors', y='Total_Contacts', log_scale=True,width=0.4, color = '#d62728').set(title='Human (hg38)',xlabel=None, ylabel=None)
sns.boxplot(ax=axes[1, 2], data=dm3, x='Authors', y='Total_Contacts', log_scale=True,width=0.3, color = '#1f77b4').set(title = 'Fruit Fly (dm3)',xlabel=None, ylabel=None)

plt.setp(axes[0,0].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[0,1].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[0,2].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[1,1].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[1,0].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[1,2].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")

ymin,y = axes[0,0].get_ylim()
y,ymax=axes[0,1].get_ylim()
axes[0,0].set_ylim(ymin,ymax)
axes[0,1].set_ylim(ymin,ymax)
axes[0,2].set_ylim(ymin,ymax)
axes[1,2].set_ylim(ymin,ymax)
axes[1,0].set_ylim(ymin,ymax)
axes[1,1].set_ylim(ymin,ymax)

#%% Cis/Trans Ratio - Figure 3
fig, axes = plt.subplots(2, 3,  figsize=(20,22), constrained_layout=True, gridspec_kw={'width_ratios': [1.5, 1, 0.25]})
sns.set()
#fig.suptitle('Single-Cell Chromatin Interaction Cis/Trans for Single-Cells by Reference Genome')
sns.boxplot(ax=axes[0, 0], data=mm9, x='Authors', y='Cis/Trans', width = 0.4,color = '#8c564b').set(title= 'Mouse (mm9)',xlabel=None,ylabel='Cis/Trans')
sns.boxplot(ax=axes[1, 0], data=mm10, x='Authors', y='Cis/Trans', width=0.5, color = '#9467bd').set(title = 'Mouse (mm10)',xlabel=None,ylabel='Cis/Trans')
sns.boxplot(ax=axes[0, 2], data=rgap7, x='Authors', y='Cis/Trans',width=0.3, color = '#e377c2').set(title='Rice (rgap7)', xlabel=None,ylabel=None)
sns.boxplot(ax=axes[1, 1], data=hg19, x='Authors', y='Cis/Trans', width=0.4, color = '#ff7f0e').set(title='Human (hg19)', xlabel=None,ylabel=None)
sns.boxplot(ax=axes[0, 1], data=hg38, x='Authors', y='Cis/Trans',width=0.3, color = '#d62728').set(title='Human (hg38)',xlabel=None,ylabel=None)
sns.boxplot(ax=axes[1, 2], data=dm3, x='Authors', y='Cis/Trans', width=0.3, color = '#1f77b4').set(title = 'Fruit Fly (dm3)',xlabel=None,ylabel=None)

plt.setp(axes[0,0].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[0,1].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[0,2].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[1,1].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[1,0].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")
plt.setp(axes[1,2].get_xticklabels(), rotation=-30, ha="left",rotation_mode="anchor")

ymax=50
ymin=0
axes[0,0].set_ylim(ymin,ymax)
axes[0,1].set_ylim(ymin,ymax)
axes[0,2].set_ylim(ymin,ymax)
axes[1,1].set_ylim(ymin,ymax)
axes[1,0].set_ylim(ymin,ymax)
axes[1,2].set_ylim(ymin,ymax)

plt.show()

#%% Make scatterplot for each dataset with total contacts and cis/trans ratio - Figure 4
import matplotlib.ticker as ticker
import numpy as np
all_stats = all_stats[all_stats['Reference_Genome']!='hg38/mm10']
all_stats_sorted=all_stats.sort_values('Authors')
plt.rcParams["figure.figsize"] = (1500,900)
sns.set(font_scale=0.75)
g = sns.FacetGrid(all_stats_sorted, col="Authors", hue="Reference_Genome", hue_kws={'color': ['#8c564b', '#9467bd','#ff7f0e','#d62728','#1f77b4','#e377c2']}, col_wrap=4, ylim = (0,100), xlim = (0,3000000))
g.map(sns.scatterplot, "Total_Contacts", "Cis/Trans",s=4)
g.set_titles(col_template = '{col_name}')
g.set_xlabels('Total Contacts')
g.tick_params(axis='x')#labelbottom=False
def scientific_format(x, pos):
    if x == 0:
        return '0'
    exponent = int(np.floor(np.log10(np.abs(x))))
    base = x / (10**exponent)
    superscript_map = {
        0: r'$^0$', 1: r'$^1$', 2: r'$^2$', 3: r'$^3$', 4:r'$^4$', 5: r'$^5$', 6: r'$^6$', 7: r'$^7$', 8: r'$^8$', 9: r'$^9$'}
    def to_superscript(n):
        return ''.join(superscript_map[int(digit)] for digit in str(n))
    exponent_str = to_superscript(exponent)
    return f'{base:.1f}×10{exponent_str}'
for ax in g.axes.flat:
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(scientific_format))
    ax.set_xlabel(ax.get_xlabel(), fontsize=10)
for ax in g.axes.flat:
    plt.setp(ax.get_xticklabels(), rotation=-45, ha='left')

g.fig.tight_layout(w_pad=1)
g.add_legend(title='Legend', bbox_to_anchor=(0.8, 0.05), loc='lower center')
    median_cistotal = two['Cis/Total'].median()
    stats.loc[dataset] = [mean_total,median_total,mean_cistrans,median_cistrans,mean_cistotal, median_cistotal] 
    
