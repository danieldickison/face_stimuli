import csv
import pandas as pd
from pandas import DataFrame


def hslf(df_list):
	#matrix: [[TP, FN], [FP, TN]]
	tp_time = []
	tn_time = []
	matrix_hs_lf = [[0,0],[0,0]]
	for i in df_list:
		if i[1] == 'yes-test':
			if i[4] == 'lf' and i[5] == 'hs':
				if i[3] == i[6]:
					#TP
					matrix_hs_lf[0][0] += 1 
					#tp_time
					tp_time.append(i[2])
				else:
					#FP
					matrix_hs_lf[1][0] += 1
		if i[1] == 'no-test':
			if i[4] == 'lf' and i[5] == 'hs':
				if i[3] == i[6]:
					#TN
					matrix_hs_lf[1][1] += 1
					#tn_time
					tn_time.append(i[2])
				else:
					#FN
					matrix_hs_lf[0][1] += 1
	
	final_hs_lf	= [
					float(matrix_hs_lf[0][0])/4, 
					float(matrix_hs_lf[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
	return final_hs_lf

def hshf(df_list):
	#matrix: [[TP, FN], [FP, TN]]
	tp_time = []
	tn_time = []
	matrix_hs_hf = [[0,0],[0,0]]
	for i in df_list:
		if i[1] == 'yes-test':
			if i[4] == 'hf' and i[5] == 'hs':
				if i[3] == i[6]:
					#TP
					matrix_hs_hf[0][0] += 1 
					#tp_time
					tp_time.append(i[2])
				else:
					#FP
					matrix_hs_hf[1][0] += 1
		if i[1] == 'no-test':
			if i[4] == 'hf' and i[5] == 'hs':
				if i[3] == i[6]:
					#TN
					matrix_hs_hf[1][1] += 1
					#tn_time
					tn_time.append(i[2])
				else:
					#FN
					matrix_hs_hf[0][1] += 1

	final_hs_hf	= [
					float(matrix_hs_hf[0][0])/24, 
					float(matrix_hs_hf[1][0])/24,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
	return final_hs_hf

def lslf(df_list):
	#matrix: [[TP, FN], [FP, TN]]
	tp_time = []
	tn_time = []
	matrix_ls_lf = [[0,0],[0,0]]
	for i in df_list:
		if i[1] == 'yes-test':
			if i[4] == 'lf' and i[5] == 'ls':
				if i[3] == i[6]:
					#TP
					matrix_ls_lf[0][0] += 1 
					#tp_time
					tp_time.append(i[2])
				else:
					#FP
					matrix_ls_lf[1][0] += 1
		if i[1] == 'no-test':
			if i[4] == 'lf' and i[5] == 'ls':
				if i[3] == i[6]:
					#TN
					matrix_ls_lf[1][1] += 1
					#tn_time
					tn_time.append(i[2])
				else:
					#FN
					matrix_ls_lf[0][1] += 1
	
	final_ls_lf	= [
					float(matrix_ls_lf[0][0])/4, 
					float(matrix_ls_lf[1][0])/4,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
	return final_ls_lf

def lshf(df_list):
	#matrix: [[TP, FN], [FP, TN]]
	tp_time = []
	tn_time = []
	matrix_ls_hf = [[0,0],[0,0]]
	for i in df_list:
		if i[1] == 'yes-test':
			if i[4] == 'hf' and i[5] == 'ls':
				if i[3] == i[6]:
					#TP
					matrix_ls_hf[0][0] += 1 
					#tp_time
					tp_time.append(i[2])
				else:
					#FP
					matrix_ls_hf[1][0] += 1
		if i[1] == 'no-test':
			if i[4] == 'hf' and i[5] == 'ls':
				if i[3] == i[6]:
					#TN
					matrix_ls_hf[1][1] += 1
					#tn_time
					tn_time.append(i[2])
				else:
					#FN
					matrix_ls_hf[0][1] += 1
	
	final_ls_hf	= [
					float(matrix_ls_hf[0][0])/24, 
					float(matrix_ls_hf[1][0])/24,
					float(sorted(tp_time)[len(tp_time)//2]), #median RTs
					float(sorted(tn_time)[len(tn_time)//2]) #median RTs
					]
	return final_ls_hf

def main():
	#NOTE: PATH NEEDS TO BE CHANGED
	#subject's data
	subject_data = list(csv.reader(open('/path/to/<file>.txt','rb'), delimiter='\t'))
	#master data
	master_test = DataFrame(pd.read_csv('/path/to/master-test.csv'))

	#only TEST data
	df_data = DataFrame(subject_data[2028:2473:4])
	
	#remaining cols: 5,6,11
	df_data = df_data.drop([x for x in range(13) if x not in (5,6,11)], axis=1)
	cols = ['occupation', 'test_resp', 'time']
	df_data.columns = cols
	
	#parsing occupation data. NOTE: bus driver is shown as 'bus'
	df_data['occupation'] = [x.split()[2].replace(")","") for x in df_data['occupation'].values.tolist()]

	#replacing yes-test and no-test values with old and new accordingly -> for later comparison
	df_data['test_resp_cmp'] = [x.replace("yes-test", "old") for x in df_data['test_resp'].values.tolist()]
	df_data['test_resp_cmp'] = [x.replace("no-test", "new") for x in df_data['test_resp_cmp'].values.tolist()]

	#adding master data
	df_data['fan'] = master_test['fan']
	df_data['status'] = master_test['status']
	df_data['master_test'] = master_test['test']
	
	#output: [HighStatusLFHits, HighStatusLFFAs, HighStatusLFHitsRTs, HighStatusLFCRsRTs]
	hslf_data = hslf(df_data.values.tolist())

	#output: [HighStatusHFHits, HighStatusHFFAs, HighStatusHFHitsRTs, HighStatusHFCRsRTs]
	hshf_data = hshf(df_data.values.tolist())

	#output: [LowStatusLFHits, LowStatusLFFAs, LowStatusLFHitsRTs, LowStatusLFCRsRTs]
	lslf_data = lslf(df_data.values.tolist())

	#output: [LowStatusHFHits, LowStatusHFFAs, LowStatusHFHitsRTs, LowStatusHFCRsRTs]
	lshf_data = lshf(df_data.values.tolist())

	#sum([hslf_data, hshf_data, lslf_data, lshf_data], [])
	out = csv.writer(open('<file>.txt', 'w'), delimiter=',')
	out.writerow(sum([hslf_data, hshf_data, lslf_data, lshf_data], []))

	

if __name__ == '__main__':
	main()
