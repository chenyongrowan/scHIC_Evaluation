#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.ticker import EngFormatter
from matplotlib.colors import LogNorm
import os, glob, cooler,random

bp_formatter = EngFormatter('b')
def format_ticks(ax, x=True, y=True, rotate=True):
    if y:
        ax.yaxis.set_major_formatter(bp_formatter)
    if x:
        ax.xaxis.set_major_formatter(bp_formatter)
        ax.xaxis.tick_bottom()
    if rotate:
        ax.tick_params(axis='x',rotation=45)

resolutions = ['50kb','100kb','250kb','500kb','1Mb']
#noCells = ['EHP','unk']

cellStages = ['1CSE','64CSE']
fileList = []
for cellStage in cellStages:
    globPhrase = f'./{resolutions[0]}/{cellStage}_*.cool'
    files = glob.glob(globPhrase)
    files = random.sample(files,5)
    fileList.extend(files)
files = []
for file in fileList:
    file = file.split('/')[2].split('_')[0] + '_' + file.split('/')[2].split('_')[1]
    files.append(file)



f, axs = plt.subplots(figsize=(40,55), ncols=5, nrows=10)
subplot_index = 0

for file in files:
    for resolution in resolutions: 
        filename = './' + resolution + '/' + file + '_' + resolution + '.cool'
        clr = cooler.Cooler(filename)
        chromstarts = []
        for i in clr.chromnames:
            chromstarts.append(clr.extent(i)[0])
        cellType = file.split('_')[0]
        cellNum = file.split('_')[1]

        if resolution == '50kb':
            vmax = 10
        elif resolution == '100kb':
            vmax = 12
        elif resolution == '250kb':
            vmax = 15
        elif resolution == '500kb':
            vmax = 20
        elif resolution == '1Mb':
            vmax = 100   
        else: 
            print(f'{resolution} failed')
        
        # Plotting
        ax = axs[subplot_index // 5, subplot_index % 5]
        im = ax.matshow(
            clr.matrix(balance=False).fetch('chr1'),
            extent=(0, clr.chromsizes['chr1'], clr.chromsizes['chr1'], 0),
            norm = LogNorm(vmin=0.000000001, vmax=vmax),
            cmap='YlOrBr'
        )
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label='raw counts')
        ax.set_title(f'Human Chr1 | Bin Size - {resolution}\n Cell Type - {cellType} | Cell Number - {cellNum}', y=1.08)
        ax.set_ylabel('position, Mb')
        format_ticks(ax)
        
        # Increment the subplot index
        subplot_index += 1
        
plt.tight_layout()
plt.show()

f.savefig('Collombetetal_2020_Chrom1_BinSizes.svg', format='svg', dpi=300)
f.savefig('Collombetetal_2020_Chrom1_BinSizes.svg', format='pdf', dpi=300)
