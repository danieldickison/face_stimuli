import os
from datetime import datetime
import smtplib

def txt_time(start_time, user, pswd, from_user, txt_num):
    end_time = datetime.now() - start_time
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(user,pswd)
    msg = "Running time for EyeMask: "+str(end_time)
    server.sendmail(from_user, txt_num, msg)

def pregen(f):
	outdir = '/Users/almaskebekbayev/Documents/research/internal_testing/internal_out/'
	for i in xrange(len(f)):
		for j in xrange(len(f)):
			if f[i] != f[j]:
				bash_command = "convert "+str(f[i])+" "+str(f[j])+" EyeMask.jpg -composite "+outdir+str(f[i])+'+'+str(f[j])+"+EyeMask.jpg"
				os.system(bash_command)

def main():
	f = []
	dir = '/Users/almaskebekbayev/Documents/research/internal_testing'
	for dirpath, subdirs,filenames in os.walk(dir):
		for i in filenames:
			if i.endswith(".jpg"):
				if i != 'EyeMask.jpg':
					f.append(i)
	#pregen(f)

	internal_eyes = f[:8]
	internal_faces = list(internal_eyes)

	for j in xrange(1):
		first = internal_faces[0]
		internal_faces = internal_faces[1:]
		internal_faces.append(first)

	#myfile = open('participant_001.txt', 'w')	
	temp = []
	for i in xrange(len(internal_eyes)):
		temp.append(internal_eyes[i])
		temp.append(internal_faces[i])

	#for ii in temp:
	#	myfile.write("%s\n" % ii)

	external_eyes = f[8:16]
	external_faces = list(external_eyes)

	for l in xrange(1):
		first = external_faces[0]
		external_faces = external_faces[1:]
		external_faces.append(first)

	ll = []
	for jj in xrange(len(external_eyes)):
		ll.append(external_eyes[jj])
		ll.append(external_faces[jj])

	#for k in ll:
	#	myfile.write("%s\n" % k)

	high_internal_eyes = f[16:24]
	high_internal_faces = list(high_internal_eyes)

	ss = []
	for i in range(len(high_internal_eyes)):
		for j in range(len(high_internal_faces)):
			if high_internal_eyes[i] != high_internal_faces[j]:
				ss.append(high_internal_eyes[i])
				ss.append(high_internal_faces[j])
	#print "size of high internal combination is:", len(ss)/2, 'not 48'

	high_external_eyes = f[24:32]
	high_external_faces = list(high_external_eyes)

	#same issue not 48, but 56
	kk = []
	for i in range(len(high_external_eyes)):
		for j in range(len(high_external_faces)):
			if high_external_eyes[i] != high_external_faces[j]:
				kk.append(high_internal_eyes[i])
				kk.append(high_external_faces[j])

	oldLowInternal = temp[:8]
	oldLowExternal = ll[:8]
	oldHighInternal = ss[:56]
	oldHighExternal = kk[:56]
	newLowInternal = temp[8:]


if __name__=='__main__':
	start_time = datetime.now()
	main()
	user = ''
	pswd = ''
	from_user = ''
	to_user = ''
	txt_num = '@tmomail.net'
	#txt_time(start_time, user, pswd, from_user, txt_num)