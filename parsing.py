f=open('small_train')
f1 = open('small_train_parsed','w')
for i in f:
	line = i.split()
	if line:
		f1.write(line[0][0]+'\t'+line[1]+'\n')
f.close()
f1.close()	
