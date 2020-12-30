import os
import jieba
import re
import time
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

stop_words = {}

with open('./stop_words.txt') as f:
    stop_list = f.read().split()
    stop_words = set(stop_list)


def pre(filename):
    ret = ""
    with open(filename, 'r', encoding='utf-8') as f:
        s = f.read()
        s = re.sub(r'[^\u4e00-\u9fa5]*', '', s)
        s = re.sub(r'[a-zA-Z0-9]*', '', s)
        cs = jieba.cut(s)
        for word in cs:
            word = word.strip()
            if len(word) > 0 and word not in stop_words and not word.isnumeric():
                ret += word + " "
    return ret


def pre_theme(tp, sample_cnt):
    texts = []
    categories = []
    for home, dirs, files in os.walk('./thu/' + tp):
        i = 1
        cat = home.split('\\')
        category = ''
        if len(cat) > 1:
            category = cat[1]
            categories.append(category)
        print(category)
        for f in files:
            if i > sample_cnt:
                break
            print(i, './thu/' + tp + '/' + category + '/' + f)
            texts.append(pre('./thu/' + tp + '/' + category + '/' + f))
            i += 1

    texts = np.array(texts)
    Tf = TfidfVectorizer(use_idf=True)
    Tf.fit(texts)
    vocs = Tf.get_feature_names()
    corpus_array = Tf.transform(texts).toarray()
    corpus_norm_df = pd.DataFrame(corpus_array, columns=vocs)
    with open('tfidf_' + tp, 'w', encoding='utf-8') as f:
        s = ""
        id = 0
        for line in corpus_array:
            print("SB", id)
            s += str(id // sample_cnt + 1) + ' '
            i = 1
            id += 1
            for item in line:
                s += str(i) + ':' + str(item) + ' '
                i += 1
            s += '\n'
        f.write(s)
    # st = time.process_time()
    # LDA = LatentDirichletAllocation(
    #     n_components=50, max_iter=100, random_state=42)
    # sblda = LDA.fit_transform(corpus_array)
    # print("LDA", sblda.shape, "TIME CONSUMED: ", time.process_time() - st)
    # with open('lda_' + tp + '_theme_distrib', 'w', encoding='utf-8') as f:
    #     s = ""
    #     linecnt = 0
    #     for line in sblda:
    #         i = 1
    #         s += str(linecnt // 50 + 1) + ' '
    #         for item in line:
    #             s += str(i) + ':' + str(item) + ' '
    #             i += 1
    #         s += '\n'
    #         linecnt += 1
    #     f.write(s)

    print("DONE")


pre_theme('train', 100)
pre_theme('test', 100)

# sb_s = ""

# tt_matrix = LDA.components_
# for tt_m in tt_matrix:
#     tt_dict = [(name, tt) for name, tt in zip(vocs, tt_m)]
#     tt_dict = sorted(tt_dict, key=lambda x: x[1], reverse=True)
#     for tt_threshold in tt_dict:
#         sb_s += tt_threshold[0] + " " + str(tt_threshold[1]) + ' '
#     sb_s += '\n'

# with open("theme_word_distrib.txt", "w", encoding='utf-8') as f:
#     f.write(sb_s)
