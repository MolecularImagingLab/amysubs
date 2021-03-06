#!/usr/bin/env python
""" This script inputs data from summarystats.sh to check for intrasubject nuclei size order for the 3
largest amygdala nuclei. Then, creates a boxplot of all amygdala subnuclei volumes and saves them in
both a plot and text file."""
def main():
	# Import libraries
	import pandas as pd
	import matplotlib.pyplot as plt
	import seaborn as sns
	import scipy.stats as sps
	import os
	import numpy as np
	# Import summary stats files generated by summarystats.sh
	summ_stats = {'left':'/media/lauri/heinrich/My_Computer/Documents/sync_me/AMY-HCP/reports/lh.amygdalar-nuclei._allsubjects.txt',
		     'right':'/media/lauri/heinrich/My_Computer/Documents/sync_me/AMY-HCP/reports/rh.amygdalar-nuclei._allsubjects.txt',
		     'whole':'/media/lauri/heinrich/My_Computer/Documents/sync_me/AMY-HCP/reports/all.regions_allsubjects.txt'}
	left = pd.read_csv(summ_stats['left'], header=0, sep='\t')
	left.rename(columns={'Measure:volume':'Subject'}, inplace = True)
	right = pd.read_csv(summ_stats['right'], header=0, sep='\t')
	right.rename(columns={'Measure:volume':'Subject'}, inplace = True)
	whole = pd.read_csv(summ_stats['whole'], header=0, sep='\t')
	whole.rename(columns={'Measure:volume':'Subject'}, inplace = True)
	avg = pd.concat([left,right])
	avg = avg.groupby('Subject').mean()
	avg = avg.reset_index()
	# Checks intrasubject nuclei size order for the 3 largest amygdala subnuclei
	sides = {'lh':left, 'rh':right, 'avg':avg}
	for side in sides.values():
	    for i in range(0,182): #range equal to number of subjects
		if side.iloc[i]['Lateral-nucleus'] < side.iloc[i]['Basal-nucleus']:
		    print(side.iloc[i]['Subject'],"Left Basal > Lateral Error")
		elif side.iloc[i]['Basal-nucleus'] < side.iloc[i]['Accessory-Basal-nucleus']:
		    print(side.iloc[i]['Subject'],"Left Accessory Basal > Basal Error")
		else:
		    continue
	print("Intrasubjet nuceli error detection complete.")
	# Checks for outliers in the data
	sides = {'lh':left, 'rh':right, 'avg':avg}
	fig_dims = (12, 6)
	fig, ax = plt.subplots(figsize=fig_dims)
	for side in sides.keys():
	    boxplot = sns.boxplot(data=sides[side], width=0.5, linewidth=2.5, orient='h')
	    file_name = os.path.join('/home/lauri/Downloads/',side+'_boxplot.jpg')
	    print(file_name)
	    plt.tight_layout()
	    plt.savefig(file_name, dpi=300)
	    plt.clf()
	# Extracts outliers to list
	from matplotlib.cbook import boxplot_stats
	sides = {'avg':avg} # May include left and right sides 
	master_list = []
	detailed_list = []
	regions = (left.columns[1:]).to_list()
	for side in sides.keys():
	    for region in regions:
		side_name = (sides[side])
		outliers = [y for stat in boxplot_stats(side_name[region]) for y in stat['fliers']]
		for outlier in outliers:
		    list_of_outliers = (side_name.loc[side_name[region] == outlier, 'Subject']).to_list()
		    for subject in list_of_outliers:
		        detailed_list.append([side,region,subject])
		        if subject not in master_list:
		            master_list.append(subject)
	final_detailed = pd.DataFrame.from_records(detailed_list, columns=['Hemisphere','Region','Subject'])
	final_master = pd.DataFrame(master_list, columns=['Subject'])
	# Save outliers in a text file
	final_master.to_csv('/media/lauri/heinrich/My_Computer/Documents/sync_me/AMY-HCP/reports/outliers_master.csv')
	final_detailed.to_csv('/media/lauri/heinrich/My_Computer/Documents/sync_me/AMY-HCP/reports/outliers_detailed.csv')
if __name__ == "__main__":
    # execute only if run as a script
    main()
