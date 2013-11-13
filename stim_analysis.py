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
		final = [
				float(matrix[0][0])/4, 
				float(matrix[1][0])/4,
				float(sorted(tp_time)[len(tp_time)//2]), #median RTs
				float(sorted(tn_time)[len(tn_time)//2]) #median RTs
				]
		
		#014DaisyKim.txt median error due to 0 in TP
		"""
		if status == 'ls':
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					0, #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
		else:
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
		"""

		#013TionnaLake median error due to 0 in TN
		"""
		if status == 'hs':
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					0 #median RTs
					]
		else:
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
		"""
		#005EmilyClapp median error due to value 0 in TP
		"""
		if status == 'ls':
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					0, #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
		else:
			final = [
					float(matrix[0][0])/4, 
					float(matrix[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
		"""
	if fan == 'hf':
		final = [
				float(matrix[0][0])/24, 
				float(matrix[1][0])/24,
				float(sorted(tp_time)[len(tp_time)//2]), #median RTs
				float(sorted(tn_time)[len(tn_time)//2]) #median RTs
				]

		#013TionnaLake median error due to 0 in TN
		"""
		if status == 'hs':
			final = [
					float(matrix[0][0])/24, 
					float(matrix[1][0])/24,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					0 #median RTs
					]
		else:
			final = [
					float(matrix[0][0])/24, 
					float(matrix[1][0])/24,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
		"""
	return final

def main():
	"""
	November 13, 2013
	Notes: 
	1. graph master data -> histogram per column
	"""
	#NOTE: PATH NEEDS TO BE CHANGED!!!
	#subject's data
	subject_data = list(csv.reader(open('/path/to/<filename>.txt','rb'), delimiter='\t'))
	#master data
	master_test = DataFrame(pd.read_csv('/path/to/stim/s<###>/master-test.csv'))

	#only TEST data
	"""
	Based on subject's csv the df_data is:
	df_data = DataFrame(subject_data[2028:2473:4])
	or 
	df_data = DataFrame(subject_data[2029:2474:4])
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
	df_data['master_test'] = master_test['test']

	#output [HighStatusLFHits, HighStatusLFFAs, HighStatusLFHitsRTs, HighStatusLFCRsRTs]
	hslf_data = confusion_matrix(df_list=df_data.values.tolist(), status='hs', fan='lf')
	
	#output: [HighStatusHFHits, HighStatusHFFAs, HighStatusHFHitsRTs, HighStatusHFCRsRTs]
	hshf_data = confusion_matrix(df_list=df_data.values.tolist(), status='hs', fan='hf')

	#output: [LowStatusLFHits, LowStatusLFFAs, LowStatusLFHitsRTs, LowStatusLFCRsRTs]
	lslf_data = confusion_matrix(df_list=df_data.values.tolist(), status='ls', fan='lf')

	#output: [LowStatusHFHits, LowStatusHFFAs, LowStatusHFHitsRTs, LowStatusHFCRsRTs]
	lshf_data = confusion_matrix(df_list=df_data.values.tolist(), status='ls', fan='hf')

	out = csv.writer(open('/path/to/csv_outs/<filename>_csv.txt', 'w'), delimiter=',')
	out.writerow(sum([hslf_data, hshf_data, lslf_data, lshf_data], []))
	
if __name__ == '__main__':
	main()
