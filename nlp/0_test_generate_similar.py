# -*- coding: utf-8 -*-

# step1, generate corpus

import jieba
import re

def generate_corpus(file_path, save_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(save_path, 'w', encoding='utf-8-sig') as f1:
        for line in lines:
            if not re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line):
                words = jieba.cut(line, cut_all=False)
                for word in words:
                    f1.writelines(word+'  ')

# if __name__ == '__main__':
#     file_path = './samples/20191209_labeled.txt'
#     save_path = './samples/20191209_corpus.txt'
#     generate_corpus(file_path, save_path)


# step2, word2vec train vec

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

# 配置再设置时log的格式
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def train_word2vec(file_path, model_path):
    corpus = open(file_path, 'r', encoding='utf-8')  # 'unicode_escape'
    model = Word2Vec(LineSentence(corpus), sg=0, size=192, window=5, min_count=5, workers=9)
    model.save(model_path)

# if __name__ == '__main__':
#     file_path = './samples/20191209_corpus.txt'
#     model_path = './models/20191209_corpus.word2vec'
#     train_word2vec(file_path, model_path)


# step 3, calculate similarity

import gensim
def count_similarity(model_path):
    model = gensim.models.Word2Vec.load(model_path)

    print(model.similarity('半年', '一年'))

    word = '半年'
    if word in model.wv.index2word:
        print(model.most_similar(word))

if __name__ == '__main__':
    model_path = './models/20191209_corpus.word2vec'
    count_similarity(model_path)

