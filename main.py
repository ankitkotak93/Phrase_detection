import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier
from nltk.classify import maxent

l = ['NP','VGF','BLK','CCP','JJP','VGNN']
f=open('org')
for i in f:
	line = i.split()
	if line:
		line1=line[0].split('-')
		if line1[1] not in l:
			l.append(line1[1])
l1=[]
f.close()
d={}
f1=open('out1')
line2=''
for i in f1:
	line=i.split()
	d={}
	for j in l:
		d[j]=0
	if line:
		line1=line[0].split('-')
		d[line1[2]]=1
		d[line[1]]=1
		d['previous']=line2		
		line2=line[1]
		d[line1[1]]=1
		l1.append((d,line1[0]))
f1.close()
f2=open('out2')
l2=[]
l3=[]
line2=''
for i in f2:
	line=i.split()
	d={}
	for j in l:
		d[j]=0
	if line:
		line1=line[0].split('-')
		d[line1[2]]=1
		d[line[1]]=1
		d['previous']=line2
		line2=line[1]
		d[line1[1]]=1
		l2.append((d))
		l3.append((d,line1[0]))
f2.close()
'''print l2[0]
print " "
print l1[0]'''
classifier = nltk.classify.NaiveBayesClassifier.train(l1)
#classifier = NaiveBayesClassifier.train(l1)
sorted(classifier.labels())
#print classifier.classify_many(l2)
classifier.show_most_informative_features()
print (nltk.classify.util.accuracy(classifier, l3))
print nltk.classify.util.log_likelihood(classifier, l3)
#cm = nltk.ConfusionMatrix(l3, l2)
#print(cm.pp(sort_by_count=True, show_percents=True, truncate=9))
'''classifier2 = nltk.classify.DecisionTreeClassifier.train(l1,entropy_cutoff=0,support_cutoff=0)
sorted(classifier2.labels())
classifier2.show_most_informative_features()
print (nltk.classify.util.accuracy(classifier2, l3))'''
encoding = maxent.TypedMaxentFeatureEncoding.train(l1,count_cutoff=3, alwayson_features=True)
classifier2 = maxent.MaxentClassifier.train(l1,bernoulli=False, encoding=encoding, trace=0)
sorted(classifier2.labels())
classifier2.show_most_informative_features()
print (nltk.classify.util.accuracy(classifier2, l3))
