import pandas as pd
import os

fn = os.path.abspath('../HD_mRNASeq_sample_info.csv')
fl = os.path.abspath('../../samples/all_salmon_quant_rrna.tsv')
sample_info = pd.read_csv(fn, comment='#')
df = pd.read_csv(fl, sep="\t")

# To get HD or control means
dataset_ids = sample_info['Dataset.dataset_id'].tolist()
control_ids = [ _ for _ in dataset_ids if _.startswith('C')]
HD_ids = [ _ for _ in dataset_ids if _.startswith('H')]

# Filtered file
df['avg_control'] = df[control_ids].mean(axis=1)
df['avg_HD'] = df[HD_ids].mean(axis=1)

# Drops rows if both avg_HD and avg_control is less than 5
df = df[(df.avg_control > 5) & (df.avg_HD > 5)]
# Drop the 2 columns
df = df.drop('avg_control', axis=1)
df = df.drop('avg_HD', axis=1)
df.to_csv("all_salmon_filter.csv", index=False)
