f=open('small_train')
f1 = open('small_train_parsed_words','w')
for i in f:
	line = i.split()
	if line:
		f1.write(line[1]+','+line[1])
f.close()
f1.close()	
