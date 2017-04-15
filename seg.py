#!/usr/bin/env python
#-*- coding:utf-8 -*-
#分词
import jieba
import jieba.analyse
import jieba.posseg as pseg
def cut_words(sentence):
    #print sentence
    return " ".join(jieba.cut(sentence)).encode('utf-8')
f = open("yuai.pure.txt")
target = open("yuai.pure.sep.txt", 'a+')
print 'open files'
line = f.readlines(100000)
while line:
    curr = []
    for oneline in line:
        curr.append(oneline)
    after_cut = map(cut_words, curr)
    target.writelines(after_cut)
    print 'saved 100000 articles'
    line = f.readlines(100000)
f.close()
target.close()