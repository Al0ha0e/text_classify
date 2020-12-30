import os
import math
import jieba
import re

category_cnt = []
category_sum = 0
category_p = []

with open('category_cnt', 'r', encoding='utf-8') as f:
    s = f.read().split()
    for i in range(0, len(s), 2):
        category_cnt.append((s[i], int(s[i + 1])))
        category_sum += int(s[i + 1])

category_dict = []

for i in range(0, len(category_cnt)):
    category_p.append(math.log10(
        category_cnt[i][1]) - math.log10(category_sum))
    cdict = {}
    with open('./possib/' + category_cnt[i][0] + '.txt', 'r', encoding='utf-8') as f:
        s = f.read().split()
        for j in range(0, len(s), 2):
            cdict[s[j]] = float(s[j + 1])
        category_dict.append(cdict)


def classify(text):
    text = re.sub(r'[^\u4e00-\u9fa5]*', '', text)
    text = re.sub(r'[a-zA-Z0-9]*', '', text)
    text = jieba.cut(text)
    text = list(set(text))
    max_possib = -100000000
    max_cate = 0
    for i in range(0, len(category_cnt)):
        possib = category_p[i]
        for word in text:
            if word in category_dict[i]:
                possib += category_dict[i][word]
        if possib > max_possib:
            max_possib = possib
            max_cate = i
    return max_cate


for home, dirs, files in os.walk('./thu/test'):
    if len(files) < 1:
        continue

    i = 1
    cat = home.split('\\')
    category = ''
    if len(cat) > 1:
        category = cat[1]
    print(category)
    tot = 0
    true_cnt = 0
    outcome = ""
    for f in files:
        tot += 1
        print('./thu/test/' + category + '/' + f)
        with open('./thu/test/' + category + '/' + f, 'r', encoding='utf-8', errors='ignore') as file:
            s = file.read()
            ans = classify(s)
            outcome += "classify: " + \
                category_cnt[ans][0] + " std: " + category + "\n"
            if category_cnt[ans][0] == category:
                true_cnt += 1
    outcome += "tot: " + str(tot) + " true: " + str(true_cnt) + \
        " rate: " + str(true_cnt / tot) + "\n"
    with open("./outcome/" + category + ".txt", "w", encoding='utf-8') as file:
        file.write(outcome)
