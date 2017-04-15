# -*- encoding:utf-8 -*-
#from __future__ import unicode_literals
#主程序
import jieba.analyse
from os import path
from scipy.misc import imread
import matplotlib as mpl 
import matplotlib.pyplot as plt  
import re
from gensim.models import KeyedVectors
import numpy as np  
from sklearn.cluster import KMeans
def get_stopWords(stopWords_fn):
    with open(stopWords_fn, 'rb') as f:
        stopWords_set = {line.strip('\r\t').decode('utf-8') for line in f}
    return stopWords_set

def my_cluster(in_list):
    model = KeyedVectors.load_word2vec_format('D:\\machine-learning\\20170414-shouhu-news-word2vec.bin', binary=True);   
    all_names = np.array(filter(lambda c: c in model, (in_list)))
    print '输入：'
    print all_names
    word_vectors = np.array(map(lambda c: model[c], all_names))    
    N = 7
    print '\n输出：'
    label = KMeans(N).fit(word_vectors).labels_
    for c in range(N):
        print "\n类别{}：".format(c+1)
        tmp_ls = []
        for idx, name in enumerate(all_names[label==c]):
            tmp_ls.insert(0,name)
            print name,           
            if idx % 10 == 9:
                print 
        print
    
if __name__ == "__main__":


    content = open("yuai.pure.sep.txt","rb").read()
    # tags extraction based on TF-IDF algorithm
    tags = jieba.analyse.extract_tags(content, topK=300, withWeight=False)
    stopWords_fn = 'all_stopword.txt'
    stopWords_set = get_stopWords(stopWords_fn)
    tags = filter(lambda x: not x.isdigit() and x not in stopWords_set,tags)
    while (len(tags) > 200):
        tags.pop()
    text ="\n".join(tags)
    text = unicode(text)
    
    #print text
    my_cluster(tags)