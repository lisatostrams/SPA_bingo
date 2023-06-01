# -*- coding: utf-8 -*-
"""
Created on Wed May 31 13:05:36 2023

@author: tostraml
"""

import shutil

import pandas as pd

import os

df = pd.read_csv('bingo.csv')

dedup = df.drop_duplicates(subset=['Soort_sim'])

def safe_copy(file_path, out_dir, dst = None):
    """Safely copy a file to the specified directory. If a file with the same name already 
    exists, the copied file name is altered to preserve both.

    :param str file_path: Path to the file to copy.
    :param str out_dir: Directory to copy the file into.
    :param str dst: New name for the copied file. If None, use the name of the original
        file.
    """
    name = dst or os.path.basename(file_path)
    if not os.path.exists(os.path.join(out_dir, name)):
        shutil.copy(file_path, os.path.join(out_dir, name))
    else:
        base, extension = os.path.splitext(name)
        i = 1
        while os.path.exists(os.path.join(out_dir, '{}_{}{}'.format(base, i, extension))):
            i += 1
        shutil.copy(file_path, os.path.join(out_dir, '{}_{}{}'.format(base, i, extension)))

for i in range(1,11):
    
    sample = dedup.sample(16,weights='rel_counts')
    
    for j in range(0,16):
        row_sample=sample.iloc[j]
        df_sample = df[df.Soort_sim==row_sample.Soort_sim]
        text = ''
        for a in df_sample.index:
            row=df_sample.loc[a]
            text = text+row.Tekst
            if row.Soort == 'Agrostis capillaris':
                source_dir = f'APP\\{row.Soortgroep}\\{row.Taxa}\\Gewoon struisgras'
            else:
                source_dir = f'APP\\{row.Soortgroep}\\{row.Taxa}\\{row.Soort}'
            dest_dir = f'team_{i}\\{row.Soortgroep}\\{row.Soort_sim}'
            if not os.path.isdir(dest_dir):
                
                dest = shutil.copytree(source_dir, dest_dir,copy_function = shutil.copy,dirs_exist_ok=True)
            else:
                
                files = os.listdir(source_dir)
                for f in files:
                    file_path = os.path.join(source_dir,f)
                    safe_copy(file_path,dest_dir)
        with open(r'{}/omschrijving.txt'.format(dest_dir), 'w',encoding="utf-8") as fp:
            fp.write(text)
    
    
    
    
