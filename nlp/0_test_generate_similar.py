# -*- coding: utf-8 -*-

import jieba

# step1, generate corpus
def generate_corpus(file_path, save_path):
    print('ok')
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print('ok')
    with open(save_path, 'w', encoding='utf-8-sig') as f1:
        for line in lines:
            words = jieba.cut(line, cut_all=False)
            for word in words:
                f1.writelines(word+'  ')

if __name__ == '__main__':
    file_path = './samples/20191209_labeled.txt'
    save_path = './samples/20191209_corpus.txt'



# from gensim.models import Word2Vec
# from gensim.models.word2vec import LineSentence
# import logging
#
# # 配置再设置时log的格式
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#
# def train_word2vec():
#     corpus = open('./samples/0_test_gensim_1.txt', 'r', encoding='utf-8')  # 'unicode_escape'
#     model = Word2Vec(LineSentence(corpus), sg=0, size=192, window=5, min_count=5, workers=9)
#     model.save('train.word2vec')
#
# if __name__ == '__main__':
#     train_word2vec()



# coding=utf-8
# import gensim
# def count_similarity():
#     model = gensim.models.Word2Vec.load('./train.word2vec')
#
#     print(model.similarity('茶杯', '水杯'))
#     #
#     # word = '中国'
#     # if word in model.wv.index2word:
#     #     print(model.most_similar(word))
#
# if __name__ == '__main__':
#     count_similarity()