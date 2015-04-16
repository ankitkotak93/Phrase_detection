import nltk
#from nltk.classify.naivebayes import NaiveBayesClassifier
nltk.usage(nltk.classify.ClassifierI)
l = ['NP','VGF','BLK','CCP','JJP','VGNN']
f=open('small_train')
for i in f:
	line = i.split()
	if line:
		l.append(line[1])
l1=[]
f.close()
d={}
f1=open('small_train')
for i in f1:
	line=i.split()
	d={}
#	for j in l:
#	d[j]=0
	if line:
		line1=line[0].split('-')
		d['a']=line[1]
		l1.append((d,line1[0]))
f1.close()
f2=open('small_train')
l2=[]
for i in f2:
	line=i.split()
	d={}
#	for j in l:
#		d[j]=0
	if line:
		line1=line[0].split('-')
		d['a']=line[1]
		l2.append((d))
f2.close()
print l2[-1]
print " "
print l1[-1]
classifier = nltk.classify.NaiveBayesClassifier.train(l1)
#classifier = NaiveBayesClassifier.train(l1)
#print classifier
sorted(classifier.labels())
classifier.classify_many(l2)
#classifier.classify(l2)
#print(nltk.classify.accuracy(classifier, l2))
