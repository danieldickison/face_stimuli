import csv
import pandas as pd
from pandas import DataFrame

def confusion_matrix(df_list, fan, status):
	#matrix: [[TP, FN], [FP, TN]]
	tp_time = []
	tn_time = []
	matrix = [[0,0],[0,0]]
	for i in df_list:
		if i[1] == 'yes-test':
			if i[4] == fan and i[5] == status:
				if i[3] == i[6]:
					#TP
					matrix[0][0] += 1 
					#adding tp_time to the list
					tp_time.append(i[2])
				else:
					#FP
					matrix[1][0] += 1
		if i[1] == 'no-test':
			if i[4] == fan and i[5] == status:
				if i[3] == i[6]:
					#TN
					matrix[1][1] += 1
					#addting tn_time to the list
					tn_time.append(i[2])
				else:
					#FN
					matrix[0][1] += 1

	if fan == 'lf':
		if status == 'ls':
			
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs for TP times
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs for TN times
					]
			
		else:
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
			
	if fan == 'hf':
		if status == 'hs':
			final = [
					float(matrix[0][0])/24, 
					float(matrix[1][0])/24,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
		else:
			final = [
					float(matrix[0][0])/24, 
					float(matrix[1][0])/24,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
	print matrix
	#returns final, total TPs, total FPs
	return final, matrix[0][0], matrix[1][0]
	
def conversion(hf_data):
	final_test = []
	for x in hf_data:
		if x[1] == 'hf' and x[6] == 'old':
			x[6] = 'new'
			final_test.append(x[6])
		elif x[1] == 'hf' and x[6] == 'new':
			x[6] = 'old'
			final_test.append(x[6])
		else:
			final_test.append(x[6])
	return final_test

def main():
	#NOTE: PATH NEEDS TO BE CHANGED!!!
	#subject's data
	subject_data = list(csv.reader(open('/Users/almaskebekbayev/Dropbox/Exp 1 Face Fan Data/Raw Data/051OliviaBrodovsky.txt','rb'), delimiter='\t'))
	#master data
	master_test = DataFrame(pd.read_csv('/Users/almaskebekbayev/Dropbox/Exp 1 Face Fan Data/stim/s051/master-test.csv'))

	#only TEST data
	"""
	Based on subject's csv the df_data is:
	df_data = DataFrame(subject_data[2028:2473:4])
	or 
	df_data = DataFrame(subject_data[2029:2474:4])]
	"""
	df_data = DataFrame(subject_data[2028:2473:4])
	#df_data = DataFrame(subject_data[2029:2474:4])

	#remaining cols: 5,6,11  
	df_data = df_data.drop([x for x in range(13) if x not in (5,6,11)], axis=1)
	cols = ['occupation', 'test_resp', 'time']
	df_data.columns = cols
	
	#parsing occupation data. NOTE: bus driver is shown as 'bus'
	df_data['occupation'] = [x.split()[2].replace(")","") for x in df_data['occupation'].values.tolist()]

	#replacing yes-test and no-test values with old and new accordingly -> for later comparison
	df_data['test_resp_cmp'] = [x.replace("yes-test", "old") for x in df_data['test_resp'].values.tolist()]
	df_data['test_resp_cmp'] = [x.replace("no-test", "new") for x in df_data['test_resp_cmp'].values.tolist()]

	#RTs - 250 due to cue timing
	df_data['time'] = [int(x)-250 for x in df_data['time'].values.tolist()]
	
	#adding master data
	df_data['fan'] = master_test['fan']
	df_data['status'] = master_test['status']

	#conversion: old -> new, new -> old
	df_data['master_test'] = conversion(master_test.values.tolist())

	#output [HighStatusLFHits, HighStatusLFFAs, HighStatusLFHitsRTs, HighStatusLFCRsRTs]
	hslf_data, hslf_tp_total, hslf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), status='hs', fan='lf')

	#output: [HighStatusHFHits, HighStatusHFFAs, HighStatusHFHitsRTs, HighStatusHFCRsRTs]
	hshf_data, hshf_tp_total, hshf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), status='hs', fan='hf')
	#print hshf_tp_total, hshf_fp_total

	#output: [LowStatusLFHits, LowStatusLFFAs, LowStatusLFHitsRTs, LowStatusLFCRsRTs]
	lslf_data, lslf_tp_total, lslf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), status='ls', fan='lf')

	#output: [LowStatusHFHits, LowStatusHFFAs, LowStatusHFHitsRTs, LowStatusHFCRsRTs]
	lshf_data, lshf_tp_total, lshf_fp_total = confusion_matrix(df_list=df_data.values.tolist(), status='ls', fan='hf')
	

	"""
	out = csv.writer(open('/Users/almaskebekbayev/Desktop/raw_data/git_data/csv_files_final/051OliviaBrodovsky.csv', 'w'), delimiter=',')
	out.writerow(sum([hslf_data,hshf_data,lslf_data,lshf_data, 
		[hslf_tp_total+hshf_tp_total+lslf_tp_total+lshf_tp_total/float(56)], #total TPs
		[hslf_fp_total+hshf_fp_total+lslf_fp_total+lshf_fp_total/float(56)]], [])) #total FPs
	"""
if __name__ == '__main__': 
	main()
