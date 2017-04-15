# -*- encoding:utf-8 -*-
#聚类测试
from __future__ import unicode_literals
from gensim.models import KeyedVectors
import numpy as np  
from sklearn.cluster import KMeans

#model = KeyedVectors.load_word2vec_format('D:\\zh\\vectors.bin', binary=True);   
model = KeyedVectors.load_word2vec_format('D:\\machine-learning\\20170414-shouhu-news-word2vec.bin', binary=True);   
#all_names = np.array(filter(lambda c: c in model, ('chess','black','peach','purple','pink','apple','golf','swimming','banana','green','red','blue','basketball','football','orange','grape','yellow','kiwi')))
#all_names = np.array(filter(lambda c: c in model, ('buddhism','islam','beijing','shanghai','amsterdam','sad','glad','confucianism','london','confuse','surprise','exciting','taoism','sydney','tokyo')))
all_names = np.array(filter(lambda c: c in model, ('三星','北京','天津','琼中','琼山','儋州','苹果','小米','华为','广州','成都','万宁','文昌','陵水')))
print '输入：'
print all_names
word_vectors = np.array(map(lambda c: model[c], all_names))    
N = 3
print '\n输出：'
label = KMeans(N).fit(word_vectors).labels_
for c in range(N):
    print "\n类别{}：".format(c+1)
    for idx, name in enumerate(all_names[label==c]):
        print name,
        if idx % 10 == 9:
            print 
    print