import os
import jieba
import re

stop_words = {}

with open('./stop_words.txt') as f:
    stop_list = f.read().split()
    stop_words = set(stop_list)


def pre(filename, count):
    with open(filename, 'r', encoding='utf-8') as f:
        s = f.read()
        s = re.sub(r'[^\u4e00-\u9fa5]*', '', s)
        s = re.sub(r'[a-zA-Z0-9]*', '', s)
        cs = jieba.cut(s)
        # os = ""
        for word in cs:
            word = word.strip()
            if len(word) > 0 and word not in stop_words and not word.isnumeric():
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
                # os += sb + '\n'
        # with open('./ans2.txt', 'w') as f:
        #     f.write(os)


def cnt2file(pth, outpth):
    count = {}
    pre(pth, count)
    with open(outpth, 'w', encoding='utf-8') as f:
        s = ""
        for sb in count.items():
            if len(sb[0]) <= 1:
                continue
            s += sb[0] + ' ' + str(sb[1]) + '\n'
        f.write(s)


for home, dirs, files in os.walk('./fudan/train'):
    i = 1
    cat = home.split('\\')
    category = ''
    if len(cat) > 1:
        category = cat[1]
    print(category)
    for f in files:
        print(i, './tmp_train/' + category + '/' + f)
        cnt2file('./tmp_train/' + category + '_' + str(i) + '.txt',
                 './tmp_train/' + category + '_' + str(i) + '.txt')
        i += 1

cats = ""

for home, dirs, files in os.walk('./fudan/train'):
    cat = home.split('\\')
    category = ''
    if len(cat) > 1:
        category = cat[1]
        cats += category + " " + str(len(files)) + '\n'

with open('./category_cnt', 'w') as f:
    f.write(cats)
